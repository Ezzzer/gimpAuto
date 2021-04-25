#!/usr/bin/python

import os
import sys
import time

from gimpfu import *

import config as cfg
from utils import scale_crop


def load_image(image, name):
    return pdb.gimp_file_load_layer(image, cfg.config[name])


def add_image(image, new_image, offset_x, offset_y):
    pdb.gimp_image_add_layer(image, new_image, -1)
    pdb.gimp_layer_set_offsets(new_image, offset_x, offset_y)
    image.merge_visible_layers(CLIP_TO_IMAGE)


def process(infile, new_name, x, y, names):
    print 'Processing file %s ' % infile
    image = pdb.gimp_file_load(infile, infile, run_mode=RUN_NONINTERACTIVE)
    print "File %s loaded OK" % infile
    scale_crop(image, x, y)

    for name in names:
        new_image = load_image(image, name)
        if name == "logo":
            add_image(image, new_image, image.width - new_image.width, image.height - new_image.height)
        if name == "dream":
            add_image(image, new_image, 0, image.height - new_image.height)
        if name == "composer":
            add_image(image, new_image, image.width / 2 - new_image.width / 2, image.height / 2 - new_image.height / 2)
        if name == "title":
            add_image(image, new_image, image.width / 2 - new_image.width / 2,
                      image.height * 2 / 3 - new_image.height / 2)
    # image.merge_visible_layers(NORMAL_MODE)
    drawable = image.active_layer
    directory = os.path.dirname(infile)
    # directory = os.path.join(directory, "images")
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
    process(file_name, "HDWithText", 1920.0, 1080.0, ["logo", "dream", "title", "composer"])
    process(file_name, "HD", 1920.0, 1080.0, [])
    process(file_name, "HD_verticalWithText", 1080.0, 1920.0, ["logo", "dream", "title", "composer"])
    process(file_name, "HD_vertical", 1080.0, 1920.0, [])
    process(file_name, "SoundCloudBanner", 2480.0, 520.0, [])
    process(file_name, "SoundCloudAlbumCoverAndBandCamp", 1400.0, 1400.0, ["logo", "dream", "title", "composer"])
    process(file_name, "SoundCloudAvatar", 800.0, 800.0, [])
    process(file_name, "YouTubeBanner", 2560.0, 1140.0, [])
    process(file_name, "YouTubeThumbnail", 1280.0, 720.0, ["logo", "dream", "title", "composer"])
    process(file_name, "SpotifyBanner", 2660.0, 1140.0, [])
    process(file_name, "SpotifyHeaderMax", 6000.0, 4000.0, [])
    process(file_name, "FacebookCoverPhoto", 820.0, 360.0, [])
    process(file_name, "FacebookProfilePic", 400.0, 400.0, [])
    process(file_name, "FacebookVideo", 1280.0, 720.0, [])
    process(file_name, "FacebookLinkShare", 1200.0, 630.0, [])
    process(file_name, "InstegramPic", 1080.0, 1350.0, [])
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)
