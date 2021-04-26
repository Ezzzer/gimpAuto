import errno
import os
import shutil

from gimpfu import *
from gimpfu import pdb

import config as cfg


def scale_crop(image, x, y):
    print image.width
    print image.height
    dx = 1.0
    dy = 1.0
    if image.width < x:
        dx = x / image.width
    if image.height < y:
        dy = y / image.height
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
        print image.width
        print image.height
        center_x = image.width / 2
        center_y = image.height / 2
        # image.crop(int(x), int(y), int(center_x - x / 2), int(center_y - y / 2))

        pdb.gimp_ellipse_select(image, 0, 0, image.width, image.height, CHANNEL_OP_REPLACE, True, True, 2)
        mask = pdb.gimp_layer_create_mask(image.active_layer, ADD_MASK_SELECTION)
        pdb.gimp_layer_add_mask(image.active_layer, mask)
        pdb.gimp_layer_remove_mask(image.active_layer, MASK_APPLY)


def save_image(drawable, file_name, image, images_dir, new_name):
    directory = os.path.dirname(file_name)
    directory = os.path.join(directory, images_dir)
    if not os.path.exists(directory):
        os.makedirs(directory)
    outfile = os.path.join(directory, new_name)
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


def get_text_image_file_name(file_name):
    directory = os.path.dirname(cfg.config["winamp_root"])
    outfile = os.path.join(directory, file_name + ".png")
    return outfile