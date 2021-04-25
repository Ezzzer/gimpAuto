#!/usr/bin/python

import errno
import os
import shutil
import sys
import time

from gimpfu import *

import config as cfg
import createTextImages
from createSitesImages import create_images
from utils import scale_crop


def create_new_image(hue, file_name, new_name, images_dir, scale_x=None, scale_y=None):
    print('Running on image: ' + file_name)
    start = time.time()
    print 'Processing file %s ' % file_name
    image = pdb.gimp_file_load(file_name, file_name, run_mode=RUN_NONINTERACTIVE)
    print "File %s loaded OK" % file_name
    if (scale_x != None):
        scale_crop(image, scale_x, scale_y)
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
    pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, hue, -25, 10, 100)
    pdb.plug_in_gmic_qt(image, drawable, 1, 0, "fx_dreamsmooth  1,1,1,0.8,0,0.8,1,24,0.0")
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


def copytree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)


def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:  # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


def create_all():
    start = time.time()
    sys.stderr = open("C:/temp/python-fu-output.txt", 'a')
    sys.stdout = sys.stderr  # So that they both go to the same file
    create_new_image(30, os.path.join(cfg.config["root_dir"], cfg.config["input_image"]),
                     cfg.config["processed_image"],
                     cfg.config["image_dir"])
    for i in range(0, 18):
        create_new_image(-180 + i * 10, os.path.join(cfg.config["root_dir"], cfg.config["input_image"]),
                         str(i) + ".png",
                         cfg.config["image_dir"], 512, 512)
    createTextImages.create_text_images(os.path.join(cfg.config["root_dir"], cfg.config["input_text_file"]))
    create_images(os.path.join(cfg.config["root_dir"], cfg.config["image_dir"], cfg.config["processed_image"]))
    try:
        shutil.rmtree(os.path.join(cfg.config["winamp_root"], cfg.config["image_dir"]))
    except:
        print "asd"
    try:
        shutil.rmtree(os.path.join(cfg.config["winamp_root"], cfg.config["text_dir"]))
    except:
        print "asd"

    copyanything(os.path.join(cfg.config["root_dir"], cfg.config["image_dir"]),
                 os.path.join(cfg.config["winamp_root"], cfg.config["image_dir"]))
    copyanything(os.path.join(cfg.config["root_dir"], cfg.config["text_dir"]),
                 os.path.join(cfg.config["winamp_root"], cfg.config["text_dir"]))
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)
