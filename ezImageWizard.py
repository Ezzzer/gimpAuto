import sys
import time

import config as cfg
from paintImage import process_basic_image, text_images, site_images, hue_images
from utils import set_std_output, copy_directories


def create_all():
    start = time.time()
    set_std_output()
    actions = cfg.config["actions"]
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


if __name__ == "__main__":
    print("Running as __main__ with args: %s" % sys.argv)
