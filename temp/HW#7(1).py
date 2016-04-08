#####################################################################
# Raster Tool
#
# Utilities:
# - performs a hillshade on a raster file
# - performs a slope process on the raster file
#
# Programmer: Jesspher Mesia
#
# Date: 03/ 21/ 2016
#
#####################################################################

import arcpy # imports the arcpy library
from arcpy import env # imports the env library 
from arcpy.sa import * # imports all arcpy functions
arcpy.CheckOutExtension("Spatial") # activates the Spatial extension under arcmap
arcpy.env.overwriteOutput=True # overwriting files is enabled

InputRaster=arcpy.GetParameterAsText(0) # gets the first parameter from the input
TheAspectOutput=arcpy.GetParameterAsText(1) # gets the second parameter from the input
TheHillshadeOutput=arcpy.GetParameterAsText(2) # gets the third parameter from the input
    
FirstFunction=arcpy.sa.Aspect(InputRaster) # runs the aspect tool
FirstFunction.save(TheAspectOutput+"Aspect.tif") # saves the output of the aspect
  
SecondFunction=arcpy.sa.Hillshade(InputRaster,"315","45") # runs the hillshade tool
SecondFunction.save(TheHillshadeOutput+"Hillshade.tif") # saves the hillshade output 

