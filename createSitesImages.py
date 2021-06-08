#!/usr/bin/python

import time

from utils import *  # scale_crop, get_text_image_file_name, get_processed_image_name, set_std_output


def load_image(image, name):
    if name in cfg.Config().config:
        return pdb.gimp_file_load_layer(image, cfg.Config().config[name])
    return pdb.gimp_file_load_layer(image, get_text_image_file_name(name))


def add_image(image, new_image, offset_x, offset_y):
    pdb.gimp_image_add_layer(image, new_image, -1)
    pdb.gimp_layer_set_offsets(new_image, offset_x, offset_y)
    image.merge_visible_layers(CLIP_TO_IMAGE)


def process(sites_image_list):
    new_name = sites_image_list[0]
    soffix = sites_image_list[1]
    x = sites_image_list[2]
    y = sites_image_list[3]
    images_name_position = sites_image_list[4]

    infile = get_processed_image_file_name()
    image = pdb.gimp_file_load(infile, infile, run_mode=RUN_NONINTERACTIVE)
    scale_crop(image, x, y)
    logo_margin = cfg.Config().config["logo_margin"] * image.width
    for name, position in images_name_position:
        x_pos = 0
        y_pos = 0
        text_image = load_image(image, name)
        if position == "lowl":
            x_pos = logo_margin
            y_pos = image.height - text_image.height - logo_margin
        if position == "upl":
            x_pos = logo_margin
            y_pos = logo_margin
        if position == "lowr":
            x_pos = image.width - text_image.width - logo_margin
            y_pos = image.height - text_image.height - logo_margin
        if position == "upr":
            x_pos = image.width - text_image.width - logo_margin
            y_pos = logo_margin
        if position == "center":
            x_pos = image.width / 2 - text_image.width / 2
            y_pos = image.height / 2 - text_image.height / 2
        if position == "centeru":
            x_pos = image.width / 2 - text_image.width / 2
            y_pos = image.height / 3 - text_image.height / 2
        if position == "centerl":
            x_pos = image.width / 2 - text_image.width / 2
            y_pos = image.height * 2 / 3 - text_image.height / 2
        if position == "banner_centeru":
            x_pos = image.width / 2 - text_image.width / 2
            y_pos = image.height / 2 - 2.3 * text_image.height
        add_image(image, text_image, int(x_pos), int(y_pos))
    drawable = image.active_layer
    pdb.gimp_file_save(image, drawable, get_pic_image_file_name(new_name, soffix), '?')
    pdb.gimp_image_delete(image)


def create_images():
    start = time.time()
    set_std_output()
    for line in cfg.Config().config["site_image_list"]:
        process(line)
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)
