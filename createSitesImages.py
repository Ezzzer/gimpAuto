#!/usr/bin/python

import os
import sys
import time

from gimpfu import *

import config as cfg
from utils import scale_crop, get_text_image_file_name


def load_image(image, name):
    if (cfg.config[name] != None):
        return pdb.gimp_file_load_layer(image, cfg.config[name])
    return pdb.gimp_file_load_layer(image, get_text_image_file_name(name))


def add_image(image, new_image, offset_x, offset_y):
    pdb.gimp_image_add_layer(image, new_image, -1)
    pdb.gimp_layer_set_offsets(new_image, offset_x, offset_y)
    image.merge_visible_layers(CLIP_TO_IMAGE)


def process(infile, sites_image_list):
    new_name = sites_image_list[0]
    x = sites_image_list[1]
    y = sites_image_list[2]
    images_name_position = sites_image_list[3]

    print 'Processing file %s ' % infile
    image = pdb.gimp_file_load(infile, infile, run_mode=RUN_NONINTERACTIVE)
    print "File %s loaded OK" % infile
    scale_crop(image, x, y)

    logo_margin = cfg.config["logo_margin"] * image.width

    for name, position in images_name_position:
        x_pos = 0
        y_pos = 0
        new_image = load_image(image, name)
        if position == "lowl":
            x_pos = logo_margin
            y_pos = image.height - new_image.height - logo_margin
        if position == "upl":
            x_pos = logo_margin
            y_pos = logo_margin
        if position == "lowr":
            x_pos = image.width - new_image.width - logo_margin
            y_pos = image.height - new_image.height - logo_margin
        if position == "upr":
            x_pos = image.width - new_image.width - logo_margin
            y_pos = logo_margin
        if position == "center":
            x_pos = image.width / 2 - new_image.width / 2
            y_pos = image.height / 2 - new_image.height / 2
        if position == "centeru":
            x_pos = image.width / 2 - new_image.width / 2
            y_pos = image.height / 3 - new_image.height / 2
        if position == "centerl":
            x_pos = image.width / 2 - new_image.width / 2
            y_pos = image.height * 2 / 3 - new_image.height / 2
        add_image(image, new_image, int(x_pos), int(y_pos))
    drawable = image.active_layer
    directory = os.path.dirname(infile)
    if not os.path.exists(directory):
        os.makedirs(directory)
    outfile = os.path.join(directory, new_name + ".png")
    pdb.gimp_file_save(image, drawable, outfile, '?')
    pdb.gimp_image_delete(image)


def create_images(file_name):
    start = time.time()
    sys.stderr = open('C:/temp/python-fu-output.txt', 'a')
    sys.stdout = sys.stderr  # So that they both go to the same file
    print('Running on image: ' + file_name)
    for line in cfg.config["site_image_list"]:
        process(file_name, line)

    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)
