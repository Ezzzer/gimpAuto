#!/usr/bin/python

import os
import sys
import time
from gimpfu import *
import glob

# extend the python path to include the plug-ins directory
# sys.path=[gimp.directory+'/plug-ins']+sys.path
#
# sys.stderr = open('python-fu-output.txt','a')
# sys.stdout=sys.stderr

def hello_world(infile,initstr, font, size, color) :
    # First do a quick sanity check on the font
    if font == 'Comic Sans MS' :
        initstr = "Comic Sans? Are you sure?"

    # Make a new image. Size 10x10 for now -- we'll resize later.
    img = gimp.Image(1, 1, RGB)

    # Save the current foreground color:
    pdb.gimp_context_push()

    # Set the text color
    gimp.set_foreground(color)

    # Create a new text layer (-1 for the layer means create a new layer)
    layer = pdb.gimp_text_fontname(img, None, 0, 0, initstr, 10, True, size, PIXELS, font)

    if layer is None:
        print 'Failed to handle '

    else:
        pdb.plug_in_gmic_qt(img, img.active_layer,1,0,"fx_dreamsmooth  3,1,1,0.8,0,0.8,1,24,0.0 ")
        img.resize(layer.width, layer.height, 0, 0)
        layer.mode = LAYER_MODE_NORMAL
        layer.opacity = 10.0
        background = gimp.Layer(img, "Background", layer.width, layer.height, RGB_IMAGE, 100.0, LAYER_MODE_DISSOLVE)
        background.fill(LAYER_MODE_DISSOLVE)
        img.add_layer(background, 1)

        # fx_crayongraffiti2
        # 300, 50, 1, 0.4, 12, 1, 2, 2, 0
        #
        # fx_blockism
        # 3, 1.6, 0.5, 50, 0.5, 64, 0, 1, 0
        #
        # fx_Squiggly
        # 2, 12, 0.8, 0, 0.5, 1, 0, 0, 3, 0.2, 0.4, 0, 1, 1, 0
        #
        # fx_stencilbw
        # 10, 10, 0, 0, 0, 50, 50
        #
        # gcd_hsv_select
        # 0, 0.5, 1, 180, 0.5, 0.5, 2, 2, 18, 0, 0, 0
        #
        # fx_dog
        # 1.215, 0.985, 25.48, 0, 0, 0, 50, 50
        #
        # fx_circle_transform
        # 49.5868, 60.5178, 53.719, 90.2913, -2, -2, 0, 1, 3, 1
        #
        # fx_euclidean2polar
        # 30.5785, 79.9353, 1, 1, 0
        #
        # fisheye
        # 43.1818, 38.1877, 70, 1
        #
        # gui_rep_polkal
        # 2, 1, 0, 50, 50, 0, 0, 1, 2, 0, 1, 0.5, 2
        #
        # moon2panorama
        # 0, 0, 0, 360, 0, 0, 1, 0, 0
        #
        # deform
        # 10
        #
        # ripple
        # 3.4, 20, 2, 0, 0
        #
        # fx_map_sphere
        # 512, 512, 90, 0.5, 0, 0, 20, 0, 0, 0, 0.5
        #
        # fx_project_stereographic
        # 0, 50, 50, 50, 75, 0, 0, 0, 0, 0, 50, 50
        #
        # fx_wind
        # 20, 0, 0.7, 20, 1, 0, 0, 0, 50, 50
        #
        # fx_gaussian_blur
        # 3, 0, 0, 1, 0, 0, 0, 50, 50
        #
        # fx_gcd_crt
        # 1.8, 1.8, 0, 0
        outfile = os.path.join('processed2', os.path.basename(infile))
        outfile = os.path.join(os.path.dirname(infile), outfile)
        # //filepath = join(directory_base, filename)
        pdb.gimp_file_save(img, layer, outfile, '?')
        # pdb.file_xbm_save(RUN_NONINTERACTIVE, image, None, filename, filepath, '', 0, 0, 0)
        # find out how to properly call file_xbm_save so we can avoid this section

    pdb.gimp_image_delete(img)
    # Restore the old foreground color:
    pdb.gimp_context_pop()

register(
    "python_fu_hello_world",
    "Hello world image",
    "Create a new image with your text string",
    "Akkana Peck",
    "Akkana Peck",
    "2010",
    "Hello world (Py)...",
    "",      # Create a new image, don't work on an existing one
    [
        (PF_STRING, "string", "Text string", 'Hello, world!'),
        (PF_STRING, "string", "Text string", 'Hello, world!'),
        (PF_FONT, "font", "Font face", "Sans"),
        (PF_SPINNER, "size", "Font size", 50, (1, 3000, 1)),
        (PF_COLOR, "color", "Text color", (1.0, 0.0, 0.0))
    ],
    [],
    hello_world, menu="<Image>/File/Create")

def process(infile):
    print 'Processing file %s ' % infile
    hello_world(infile,"EZER", "Segoe UI Bold", 85, (0.8, 0.8, 1.0))
    # image = pdb.gimp_file_load(infile, infile, run_mode=RUN_NONINTERACTIVE)
    # drawable = image.active_layer
    # print "File %s loaded OK" % infile
    # pdb.plug_in_photocopy(image, drawable, 8., 0.8, 0.2, 0.2)
    # pdb.plug_in_cartoon(image, drawable, 7., 0.2)
    # outfile = os.path.join('processed', os.path.basename(infile))
    # outfile = os.path.join(os.path.dirname(infile), outfile)
    # print "Saving to %s" % outfile
    # pdb.file_jpeg_save(image, drawable, outfile, outfile, "0.5", 0, 1, 0, "", 0, 1, 0, 0)
    # print "Saved to %s" % outfile
    # pdb.gimp_image_delete(image)


def run(input_dir):
    start = time.time()
    sys.stderr = open('C:/temp/python-fu-output.txt', 'a')
    sys.stdout = sys.stderr  # So that they both go to the same file
    print('Running on directory: ' + input_dir)
    mypath = os.path.join(input_dir, '*.png')
    for infile in glob.glob(mypath):
        process(infile)
    end = time.time()
    print "Finished, time: %.2f seconds" % (end - start)


if __name__ == "__main__":
    print("Running as __main__ with args: %s" % sys.argv)
