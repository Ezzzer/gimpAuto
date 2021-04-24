import sys;

# extend the python path to include the plug-ins directory
sys.path=[gimp.directory+'/plug-ins']+sys.path

#import the plugin
import main

# Call the function: note that the function name is prefixed with the module name
run(",/images")

reload(plugin)