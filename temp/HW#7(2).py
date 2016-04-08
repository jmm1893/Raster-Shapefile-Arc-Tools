#####################################################################
# Shapefile Tool
#
# Utilities:
# - Collects a value from an attribute table and outputs it as text
# 
# Programmer: Jesspher Mesia
#
# Date: 03/ 22/ 2016
#
#####################################################################

import arcpy
from arcpy import env # imports the env library from the arcpy library
from arcpy.sa import * # imports all arcpy functionalities
arcpy.CheckOutExtension("Spatial") # enables the Spatial extension 
arcpy.env.overwriteOutput=True # enables file overwriting

try:
    TheInputLayer=arcpy.GetParameterAsText(0) # path for the input file
    TheAttribute=arcpy.GetParameterAsText(1) # attribute for the tool

    arcpy.AddMessage("The Input Layer="+TheInputLayer)
    arcpy.AddMessage("The Attribute="+TheAttribute)
    
    List= [row[0] for row in arcpy.da.SearchCursor(TheInputLayer, TheAttribute)] # searches for the attribute values and inserts them into a list
    TheSum= sum(List) # summs the list values
    Count= len(List) # counts how many values there are in the list
    Average= TheSum/Count # calculates the average 
    
    arcpy.AddMessage("Number of Values= "+str(Count)) # prints the number of values
    arcpy.AddMessage("Sum of Values= "+ str(TheSum)) # prints the sum value
    arcpy.AddMessage("The Average= "+ str(Average)) # prints the average value
        
except:
    arcpy.AddMessage("Error: Inputs invalid")