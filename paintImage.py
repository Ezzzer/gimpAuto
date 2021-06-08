#!/usr/bin/python

import os
import time

from gimpfu import *

import config as cfg
import createTextImages
from createSitesImages import create_images
from utils import scale_crop, crop_circle, save_image, get_processed_image_name, \
    get_processed_image_fx, is_processed_image_fx_enabled, get_root_dir


def create_new_image(hue, file_name, new_name, scale_x=None, scale_y=None):
    print('Running on image: ' + file_name)
    start = time.time()
    print 'Processing file %s ' % file_name
    drawable, image = create_dream_image(file_name)
    if scale_x is not None:
        scale_crop(image, scale_x, scale_y)
    if cfg.Config().config["circle"]:
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
    if get_processed_image_gradient_enabled():
        gradient_map(drawable, image)
    if is_processed_image_fx_enabled():
        pdb.plug_in_gmic_qt(image, drawable, 1, 0, get_processed_image_fx())
    if is_processed_image_hue_saturation_enabled():
        process_image_hue_params = get_processed_image_hue_saturation()
        pdb.gimp_drawable_hue_saturation(drawable, HUE_RANGE_ALL, process_image_hue_params[0],
                                         process_image_hue_params[1],
                                         process_image_hue_params[2], process_image_hue_params[3])
    if cfg.Config().config["circle"]:
        crop_circle(image)

    return drawable, image


def gradient_map(drawable, image):
    pdb.gimp_context_set_gradient(get_processed_image_gradient_name())
    color = get_processed_image_gradient_for_color()
    pdb.gimp_palette_set_background(color)
    color = get_processed_image_gradient_back_color()
    pdb.gimp_palette_set_foreground(color)
    pdb.plug_in_gradmap(image, drawable)


def get_processed_image_hue_saturation():
    return cfg.Config().config["process_image"]["hue_saturation"]["value"]


def is_processed_image_hue_saturation_enabled():
    return cfg.Config().config["process_image"]["hue_saturation"]["enable"]


def get_processed_image_gradient_name():
    return cfg.Config().config["process_image"]["gradient"]["name"]


def get_processed_image_gradient_enabled():
    return cfg.Config().config["process_image"]["gradient"]["enable"]


def get_processed_image_gradient_for_color():
    color = cfg.Config().config["process_image"]["gradient"]["forground_color"]
    return gimpcolor.RGB(color[0], color[1], color[2])


def get_processed_image_gradient_back_color():
    color = cfg.Config().config["process_image"]["gradient"]["background_color"]
    return gimpcolor.RGB(color[0], color[1], color[2])


def process_basic_image():
    drawable, image = create_dream_image(get_basic_image_file_name())
    save_image(drawable, image, get_processed_image_name() + ".png")
    pdb.gimp_image_delete(image)


def get_basic_image_file_name():
    return os.path.join(get_root_dir(), cfg.Config().config["basic_image"])


def get_hue_image_file_name():
    hue_path = os.path.join(get_root_dir(), cfg.Config().config["hue_image"])
    if os.path.exists(hue_path):
        return hue_path
    return get_basic_image_file_name()


def site_images():
    create_images()


def text_images():
    createTextImages.create_text_images()


def hue_images():
    scale = cfg.Config().config["hue_scale"]
    process_image_hue_params = cfg.Config().config["hue_params"]
    process_image_hue_intervals = cfg.Config().config["hue_intervals"]
    drawable, image = create_dream_image(get_hue_image_file_name())
    if scale[0] is not None:
        scale_crop(image, scale[0], scale[1])
    if cfg.Config().config["hue_circle"]:
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
