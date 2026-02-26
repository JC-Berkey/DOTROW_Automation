import arcpy
import os

def main():

    aprx = arcpy.mp.ArcGISProject("CURRENT")

    m = aprx.activeMap

    if not m:
        arcpy.AddError("No active map found.") 
        return

    pdf_path = arcpy.GetParameterAsText(0)

    spatialRef = m.spatialReference

    tif_folder = r"C:\Users\jcberkey\Documents\ArcGIS\Projects\DOTROW_JACK_GEOREF\TempTIFFsForAutomation"
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    tif_path = os.path.join(tif_folder, f"{pdf_name}.tif")
   
    arcpy.conversion.PDFToTIFF(
        in_pdf_file=pdf_path,
        out_tiff_file=tif_path,
        pdf_page_number=1,
        resolution=300
    )

    platLayer = m.addDataFromPath(tif_path)

    arcpy.management.DefineProjection(tif_path, spatialRef)

    if platLayer:
        platLayer.transparency = 25

    arcpy.AddMessage("PDF added successfully")

if __name__ == "__main__":
    main()