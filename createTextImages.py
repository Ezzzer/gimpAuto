#!/usr/bin/python

import os
import sys
import time

from gimpfu import *

import config as cfg


def create_image(index, file_name, text, params):
    print 'create_image ' + file_name + " - " + text + "-" + params
    pa = params.split("|")
    font = pa[0]
    size = pa[1]
    temp = pa[2].split(',')
    color = (float(temp[0]), float(temp[1]), float(temp[2]))
    fx = pa[3]
    print "font = " + font
    print "size = " + size
    # //print "color = " + len(color)
    print "fx = " + fx
    # Make a new image. Size 10x10 for now -- we'll resize later.
    img = gimp.Image(1, 1, RGB)
    pdb.gimp_context_push()
    gimp.set_foreground(color)
    # Create a new text layer (-1 for the layer means create a new layer)
    layer = pdb.gimp_text_fontname(img, None, 0, 0, text, 10, True, size, PIXELS, font)
    if layer is None:
        print 'Failed to handle '
    else:
        # pdb.plug_in_gmic_qt(img, img.active_layer,1,0,"fx_dreamsmooth  3,1,1,0.8,0,0.8,1,24,0.0 ")
        img.resize(layer.width, layer.height, 0, 0)

        background = gimp.Layer(img, "Background" + str(index), layer.width, layer.height, RGB_IMAGE, 100.0,
                                LAYER_MODE_DISSOLVE)
        pdb.plug_in_gmic_qt(img, layer, 1, 0, fx)
        img.add_layer(background, index)
        directory = os.path.dirname(file_name)
        directory = os.path.join(directory, cfg.config["text_dir"])
        if not os.path.exists(directory):
            os.makedirs(directory)
        outfile = os.path.join(directory, "text" + str(index) + ".png")
        pdb.gimp_file_save(img, layer, outfile, '?')

    pdb.gimp_context_pop()
    layer = None
    pdb.gimp_image_delete(img)


def create_text_images(file_name):
    start = time.time()
    sys.stderr = open("C:/temp/python-fu-output.txt", 'a')
    sys.stdout = sys.stderr  # So that they both go to the same file
    print('Input filename:: ' + file_name)
    with open(file_name) as f:
        lines = f.read().splitlines()
        index = 1
        for i in range(0, len(lines), 2):
            text = lines[i]
            params = lines[i + 1]
            create_image(index, file_name, text, params)
            index += 1
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)
