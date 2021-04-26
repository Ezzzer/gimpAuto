#!/usr/bin/python

import os
import time

from gimpfu import *

import config as cfg
import createTextImages
from createSitesImages import create_images
from utils import scale_crop, crop_circle, save_image, copy_directories, set_std_output


def create_new_image(hue, file_name, new_name, scale_x=None, scale_y=None):
    print('Running on image: ' + file_name)
    start = time.time()
    print 'Processing file %s ' % file_name
    drawable, image = create_dream_image(file_name)
    if scale_x is not None:
        scale_crop(image, scale_x, scale_y)
    if cfg.config["circle"]:
        crop_circle(image)
    pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, hue, -25, 10, 100)
    save_image(drawable, image, new_name)

    pdb.gimp_image_delete(image)
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)


def create_dream_image(file_name):
    image = pdb.gimp_file_load(file_name, file_name, run_mode=RUN_NONINTERACTIVE)
    print "File %s loaded OK" % file_name
    drawable = image.active_layer
    pdb.gimp_context_set_gradient("FG to BG (HSV clockwise hue)")
    color = gimpcolor.RGB(255, 255, 255)  # integers in 0->255 range)
    pdb.gimp_palette_set_background(color)
    color = gimpcolor.RGB(250, 0, 0)  # Floats in 0.->1. range)
    pdb.gimp_palette_set_foreground(color)
    pdb.plug_in_gradmap(image, drawable)
    pdb.plug_in_gmic_qt(image, drawable, 1, 0, cfg.config["process_image_fx"])
    return drawable, image


def process_basic_image():
    process_image_hue_params = cfg.config["process_image_hue_params"]
    drawable, image = create_dream_image(get_basic_image_file_name())
    pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, process_image_hue_params[0], process_image_hue_params[1],
                                     process_image_hue_params[2], process_image_hue_params[3])
    save_image(drawable, image, cfg.config["processed_image"]+".png")
    pdb.gimp_image_delete(image)


def get_basic_image_file_name():
    return os.path.join(cfg.config["root_dir"], cfg.config["basic_image"])


def site_images():
    create_images()


def text_images():
    createTextImages.create_text_images()


def hue_images():
    scale = cfg.config["hue_scale"]
    process_image_hue_params = cfg.config["process_image_hue_params"]
    process_image_hue_intervals = cfg.config["process_image_hue_intervals"]
    drawable, image = create_dream_image(get_basic_image_file_name())
    if scale[0] is not None:
        scale_crop(image, scale[0], scale[1])
    if cfg.config["hue_circle"]:
        crop_circle(image)
    start_hue = process_image_hue_intervals[0]
    end_hue = process_image_hue_intervals[1]
    delta1 = (process_image_hue_params[0] - start_hue) / 9
    delta2 = (end_hue - process_image_hue_params[0]) / 9
    for i in range(0, 9):
        pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, start_hue + i * delta1, process_image_hue_params[1],
                                         process_image_hue_params[2], 100)
        save_image(drawable, image, str(i) + ".png")
        pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, 0, -process_image_hue_params[1],
                                         -process_image_hue_params[2], 100)

    for i in range(9, 18):
        pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, end_hue - (i - 9) * delta2,
                                         process_image_hue_params[1], process_image_hue_params[2], 100)
        save_image(drawable, image, str(i) + ".png")
        pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, 0, -process_image_hue_params[1],
                                         -process_image_hue_params[2], 100)


def create_all():
    start = time.time()
    set_std_output()
    actions = cfg.config["actions"]
    if "process_image" in actions:
        process_basic_image()
    if "hue_images" in actions:
        hue_images()
    if "text_images" in actions:
        text_images()
    if "site_images" in actions:
        site_images()
    if "copy_directories" in actions:
        copy_directories()
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)
