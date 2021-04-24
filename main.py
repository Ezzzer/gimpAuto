#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# gimp -idf --batch-interpreter python-fu-eval -b "import sys;sys.path=['.']+sys.path;import batch;batch.run('./images')" -b "pdb.gimp_quit(1)"

import os, glob, sys, time
from gimpfu import *
#
# theImage = gimp.image_list()[0]
# centerX = theImage.width/2
# centerY = theImage.height/2
# gridSpacing = max(theImage.width, theImage.height)/24
# pdb.gimp_image_grid_set_offset(theImage, centerX, centerY)
# pdb.gimp_image_grid_set_spacing(theImage, gridSpacing, gridSpacing)
# pdb.gimp_image_grid_set_style(theImage, GRID_ON_OFF_DASH)

import sys
sys.path.append('C:\Users/ezer/.gimp-2.8/plug-ins/batch')
sys.path
import os
os.chdir('C:\Users\ezer\.gimp-2.8\plug-ins/batch')
from batch import *
run('D:\MakingMusic/Automatic Music Machine/3.In Progress/Bit38_Budhaa Bell Acid/images/temp')

def process2(infile):
        print "Processing file %s " % infile
        image = pdb.gimp_file_load(infile, infile, run_mode=RUN_NONINTERACTIVE)
        drawable = image.active_layer

        pdb.gimp_image_grid_set_style(theImage, GRID_SOLID)

        print "File %s loaded OK" % infile
        pdb.plug_in_photocopy(image, drawable,8.,0.8,0.2,0.2)
        pdb.plug_in_cartoon(image, drawable, 7.,0.2)
        outfile=os.path.join('processed',os.path.basename(infile))
        outfile=os.path.join(os.path.dirname(infile),outfile)
        print "Saving to %s" % outfile
        pdb.file_jpeg_save(image, drawable, outfile, outfile, "0.5",0,1,0,"",0,1,0,0)
        print "Saved to %s" % outfile
        pdb.gimp_image_delete(image)


def run2(directory):
        start=time.time()
        print "Running on directory \"%s\"" % directory
#   os.mkdir(os.path.join(directory,'processed'))
        for infile in glob.glob(os.path.join(directory, '*.jpg')):
                process(infile)
        end=time.time()
        print "Finished, total processing time: %.2f seconds" % (end-start)


if __name__ == "__main__":
        print "Running as __main__ with args: %s" % sys.argv