#!/usr/bin/python

import os
import sys
import time

from gimpfu import *

import config as cfg
from utils import get_text_image_file_name


def create_text_image(index, line, file_name=None):
    text = line[0]
    font = line[1]
    size = line[2]
    color = line[3]
    fx = line[4]
    # Make a new image. Size 10x10 for now -- we'll resize later.
    img = gimp.Image(1, 1, RGB)
    pdb.gimp_context_push()
    gimp.set_foreground(color)
    layer = pdb.gimp_text_fontname(img, None, 0, 0, text, 10, True, size, PIXELS, font)
    if layer is None:
        print 'Failed to handle '
    else:
        img.resize(layer.width, layer.height, 0, 0)

        if index >= 0:
            background = gimp.Layer(img, "Background" + str(index), layer.width, layer.height, RGB_IMAGE, 100.0,
                                    LAYER_MODE_NORMAL)
            pdb.plug_in_gmic_qt(img, layer, 1, 0, fx)
            img.add_layer(background, index)
            directory = os.path.dirname(cfg.config["root_dir"])
            directory = os.path.join(directory, cfg.config["text_dir"])
            if not os.path.exists(directory):
                os.makedirs(directory)
            outfile = os.path.join(directory, "text" + str(index) + ".png")
        else:
            background = gimp.Layer(img, "Background1", layer.width, layer.height, RGB_IMAGE, 100.0,
                                    LAYER_MODE_NORMAL)
            pdb.plug_in_gmic_qt(img, layer, 1, 0, fx)
            img.add_layer(background, 1)
            outfile = get_text_image_file_name(file_name)
        pdb.gimp_file_save(img, layer, outfile, '?')

    pdb.gimp_context_pop()

    pdb.gimp_image_delete(img)


def create_text_images():
    start = time.time()
    sys.stderr = open("C:/temp/python-fu-output.txt", 'a')
    sys.stdout = sys.stderr  # So that they both go to the same file
    index = 1
    texts_list = cfg.config["text_list_for_video"]
    for line in texts_list:
        create_text_image(index, line)
        index += 1

    index = -1
    texts_list = cfg.config["text_list"]
    for line in texts_list:
        name = line.pop(0)
        create_text_image(index, line, name)
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)
