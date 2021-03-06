#!/usr/bin/env python
import errno
import os
import shutil
import sys

from gimpfu import *
from gimpfu import pdb

import config as cfg
import tracks


def scale_crop(image, x, y):
    print image.width
    print image.height

    if image.width < x:
        dx = float(x) / image.width
        image.scale(int(x), int(image.height * dx))

    if image.height < y:
        dy = float(y) / image.height
        image.scale(int(image.width * dy), int(y))

    dx = float(x) / image.width
    dy = float(y) / image.height

    print dx, dy
    if dx > dy:
        image.scale(int(x), int(image.height * dx))
    else:
        image.scale(int(image.width * dy), int(y))
    center_x = image.width / 2
    center_y = image.height / 2
    print image.width
    print image.height
    image.crop(int(x), int(y), int(center_x - x / 2), int(center_y - y / 2))


def crop_circle(image):
    pdb.gimp_ellipse_select(image, 0, 0, image.width, image.height, CHANNEL_OP_REPLACE, True, True, 2)
    mask = pdb.gimp_layer_create_mask(image.active_layer, ADD_MASK_SELECTION)
    pdb.gimp_layer_add_mask(image.active_layer, mask)
    pdb.gimp_layer_remove_mask(image.active_layer, MASK_APPLY)


def save_image(drawable, image, new_name):
    outfile = os.path.join(get_image_dir(), new_name)
    pdb.gimp_file_save(image, drawable, outfile, '?')


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


def copy_directories():
    try:
        shutil.rmtree(os.path.join(cfg.Config().config ["winamp_root"], cfg.Config().config["image_dir"]))
    except:
        print "ok, nothing to delete on target"
    try:
        shutil.rmtree(os.path.join(cfg.Config().config["winamp_root"], cfg.Config().config["text_dir"]))
    except:
        print "ok, nothing to delete on target"
    copyanything(get_image_dir(), os.path.join(cfg.Config().config["winamp_root"], cfg.Config().config["image_dir"]))
    copyanything(get_text_dir(), os.path.join(cfg.Config().config["winamp_root"], cfg.Config().config["text_dir"]))


def get_text_image_file_name(name):
    return os.path.join(get_text_dir(), name + ".png")


def get_text_dir():
    directory = os.path.join(get_root_dir(), cfg.Config().config["text_dir"])
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def get_image_dir():
    directory = os.path.join(get_root_dir(), cfg.Config().config["image_dir"])
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def get_root_dir():
    return tracks.Track().get_root_dir()


def get_processed_image_name():
    return cfg.Config().config["process_image"]["name"]


def get_processed_image_file_name():
    return get_pic_image_file_name(get_processed_image_name())


def get_processed_image_fx():
    return cfg.Config().config["process_image"]["fx"]["value"]


def is_processed_image_fx_enabled():
    return cfg.Config().config["process_image"]["fx"]["enable"]


def get_pic_image_file_name(name,soffix = "png"):
    infile = os.path.join(get_image_dir(), name + "." + soffix)
    return infile


def set_std_output():
    sys.stderr = open("C:/temp/python-fu-output.txt", 'a')
    sys.stdout = sys.stderr  # So that they both go to the same file


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]