@REM set %PATH%=%PATH%;"E:\gimp 2\bin" -idf

@REM gimp -i -b '(batch-unsharp-mask "*.png" 5.0 0.5 0)' -b '(gimp-quit 0)'
@REM gimp -idf --batch-interpreter python-fu-eval -b "import sys;sys.path=['.']+sys.path;import batch;batch.run('./images')" -b "pdb.gimp_quit(1)"
"E:\gimp 2\bin\gimp-console-2.10" --verbose -id --batch-interpreter python-fu-eval -b "import sys;sys.path.append('C:\Users/ezer/.gimp-2.8/plug-ins/batch');from batch import *;run('D:\MakingMusic/Automatic Music Machine/3.In Progress/Bit38_Budhaa Bell Acid/images/temp')" -b "pdb.gimp_quit(1)"