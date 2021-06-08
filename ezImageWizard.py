#!/usr/bin/env python
import os
import sys
import time
import traceback

import config as cfg
import tracks
from paintImage import process_basic_image, text_images, site_images, hue_images
from utils import set_std_output, copy_directories


def create_all(track_name=None):
    # prepare_running_on_gimp()
    set_std_output()
    try:
        if track_name is not None:
            print("Creating track: " + track_name)
            tracks.Track().set_current_track(track_name)

        if track_name == "all":
            print("Updating all tracks: " + track_name)
            for track in tracks.Track().get_map():
                tracks.Track().set_current_track(track)
                process_track()
        else:
            print("creating track: " + tracks.Track().get_title())
            process_track()

    except Exception as ex:
        print("Got an exception: " + ex.message)
        traceback.print_exc(file=sys.stdout)


def process_track():
    try:
        print ("Processing Track:" + tracks.Track().get_title())
        cfg.Config().update()
        start = time.time()

        actions = cfg.Config().config["actions"]
        if "process_image" in actions:
            process_basic_image()
        if "text_images" in actions:
            text_images()
        if "site_images" in actions:
            site_images()
        if "hue_images" in actions:
            hue_images()
        if "copy_directories" in actions:
            copy_directories()
        end = time.time()
        print "Finished, time: %.2f seconds" % (end - start)
    except Exception as ex:
        print("Got an exception: " + ex.message)
        traceback.print_exc(file=sys.stdout)


def prepare_running_on_gimp():
    sys.path.append(r'C:\Users/ezer/.gimp-2.8/plug-ins/batch')
    os.chdir(r'C:/Users/ezer/.gimp-2.8/plug-ins/batch')


def hello():
    set_std_output()
    print ("hello world")
    create_all("all")


if __name__ == "__main__":
    print("Running as __main__ with args: %s" % sys.argv)
