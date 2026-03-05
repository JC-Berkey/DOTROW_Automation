import arcpy
import os

# This class is purely for creating the dropdown selection for the active layers
class ToolValidator(object):

    def __init__(self):
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        pass
    
    def updateParameters(self):
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        m = aprx.activeMap
        if m:
            # filter dropdown to only raster layers
            raster_layers = [lyr.name for lyr in m.listLayers() if lyr.isRasterLayer]
            self.params[0].filter.list = raster_layers

    def updateMessages(self):
        pass

def main():

    aprx = arcpy.mp.ArcGISProject("CURRENT")
    m = aprx.activeMap

    if not m:
        arcpy.AddError("No active map found")
        return

    layer = arcpy.GetParameter(0)
    pdf_path = layer.dataSource

    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    pdf_dir = os.path.dirname(pdf_path)
    pdf_folder_dir = os.path.dirname(pdf_dir)

    tiff_folder_path = os.path.join(pdf_folder_dir, "TIFF")

    #The TIFF folder should always exist so this shouldnt run. Just a catch case.
    os.makedirs(tiff_folder_path, exist_ok=True)

    full_path = os.path.join(tiff_folder_path, pdf_name + ".tif")

    # Copies the georeferenced tif to the TIFF folder using the cerated full path
    arcpy.management.CopyRaster(pdf_path, full_path)


if __name__ == "__main__":
    main()