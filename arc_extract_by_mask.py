import arcpy
arcpy.CheckOutExtension('Spatial')
from arcpy import env
from arcpy.sa import *
env.workspace = "J:/MODIS/MOD09A1/ceshi/GF1_WFV1_E112.5_N39.7_20170117_L1A0002127383"
outExtractByMask = ExtractByMask("MOD09A12017001.hdfout.sur_refl_b03.tif", "reproject.tif")
outExtractByMask.save("J:/MODIS/MOD09A1/ceshi/GF1_WFV1_E112.5_N39.7_20170117_L1A0002127383/maskextract.tif")
print "extractbymask successfully"
