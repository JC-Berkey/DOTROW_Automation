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
    
    pdf_folder = os.path.dirname(pdf_path)
    parent_folder = os.path.dirname(pdf_folder)
   
    project_relative = os.path.relpath(parent_folder, r"Z:\PROJECTS\DOT_ROW\Plat Database\SE") 
    folder_code = project_relative.replace(os.sep, "_")
    
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    tif_name = f"{pdf_name}__FOLDER__{folder_code}.tif"

    os.makedirs(tif_path, exist_ok=True)
    tif_path = os.path.join(tif_folder, tif_name)
   
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