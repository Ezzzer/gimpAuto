#!/usr/bin/python

import time

from gimpfu import *

import config as cfg
from utils import get_text_image_file_name, set_std_output


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

        background = gimp.Layer(img, "Background0", layer.width, layer.height, RGB_IMAGE, 100.0,
                                LAYER_MODE_NORMAL)
        pdb.plug_in_gmic_qt(img, layer, 1, 0, fx)
        img.add_layer(background, 1)
        if file_name is None:
            file_name = "text" + str(index)
        outfile = get_text_image_file_name(file_name)
        pdb.gimp_file_save(img, layer, outfile, '?')
    pdb.gimp_context_pop()
    pdb.gimp_image_delete(img)


def create_text_images():
    start = time.time()
    index = 1
    texts_list = cfg.Config().config["text_list_for_video"]
    for line in texts_list:
        create_text_image(index, line)
        index += 1

    index = -1
    texts_list = cfg.Config().config["text_list"]
    for line in texts_list:
        name = line.pop(0)
        create_text_image(index, line, name)
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)


