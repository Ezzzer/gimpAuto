#!/usr/bin/python

import os
import sys
import time

from gimpfu import *

import config as cfg
import createTextImages
from createSitesImages import create_images


def create_new_image(file_name, new_name, images_dir):
    print('Running on image: ' + file_name)
    start = time.time()
    print 'Processing file %s ' % file_name
    image = pdb.gimp_file_load(file_name, file_name, run_mode=RUN_NONINTERACTIVE)
    print "File %s loaded OK" % file_name
    drawable = image.active_layer
    # pdb.plug_in_photocopy(image, drawable, 8., 0.8, 0.2, 0.2)
    # pdb.gimp_context_push()
    # pdb.gimp_context_set_gradient("Full saturation spectrum CCW")
    # num_gradients, gradient_list = pdb.gimp_gradients_get_list(None)
    # print gradient_list
    pdb.gimp_context_set_gradient("FG to BG (HSV clockwise hue)")
    color = gimpcolor.RGB(255, 255, 255)  # integers in 0->255 range)
    pdb.gimp_palette_set_background(color)
    color = gimpcolor.RGB(250, 0, 0)  # Floats in 0.->1. range)
    pdb.gimp_palette_set_foreground(color)
    pdb.plug_in_gradmap(image, drawable)
    pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, 30, -25, 10, 100)
    pdb.plug_in_gmic_qt(image, drawable, 1, 0, "fx_dreamsmooth  3,1,1,0.8,0,0.8,1,24,0.0")
    directory = os.path.dirname(file_name)
    directory = os.path.join(directory, images_dir)
    if not os.path.exists(directory):
        os.makedirs(directory)
    outfile = os.path.join(directory, new_name)
    pdb.gimp_file_save(image, drawable, outfile, '?')
    pdb.gimp_image_delete(image)
    # pdb.gimp_context_pop()
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)


def create_all():
    start = time.time()
    sys.stderr = open("C:/temp/python-fu-output.txt", 'a')
    sys.stdout = sys.stderr  # So that they both go to the same file
    create_new_image(os.path.join(cfg.config["root_dir"], cfg.config["input_image"]),
                     cfg.config["processed_image"],
                     cfg.config["image_dir"])
    # createTextImages.create_text_images(os.path.join(cfg.config["root_dir"], cfg.config["input_text_file"]))
    create_images(os.path.join(cfg.config["root_dir"], cfg.config["image_dir"], cfg.config["processed_image"]))
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)
