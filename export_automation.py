import arcpy
import os

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
    tif_path = layer.dataSource

    tif_file = os.path.splitext(os.path.basename(tif_path))[0]
    pdf_part, folder_part = tif_file.split("__FOLDER__")
    pdf_name = pdf_part
    folder_parts = folder_part.split("_")

    project_base = r"Z:\PROJECTS\DOT_ROW\Plat Database\SE"
    tiff_folder_path = os.path.join(project_base, *folder_parts, "TIFF")
    os.makedirs(tiff_folder_path, exist_ok=True)

    full_path = os.path.join(tiff_folder_path, pdf_name + ".tif")

    arcpy.AddMessage(f"Temp tif path: {tif_path}")
    arcpy.AddMessage(f"Export folder path: {tiff_folder_path}")
    arcpy.AddMessage(f"Final export path: {full_path}")

    arcpy.management.CopyRaster(tif_path, full_path)


if __name__ == "__main__":
    main()