import arcpy
import os

def main():

    # Assign current project
    aprx = arcpy.mp.ArcGISProject("CURRENT")

    # Assign active map
    m = aprx.activeMap

    # Error catch
    if not m:
        arcpy.AddError("No active map found.") 
        return

    # Just assigns pdf_path variable to pdf input
    pdf_path = arcpy.GetParameterAsText(0)

    # Gets spatial reference of active map
    spatialRef = m.spatialReference

    # Creates new tif path from pdf
    tif_path = makeTifPathFromPDFPath(pdf_path)
   
   # Converts pdf to tif (raster)
    arcpy.conversion.PDFToTIFF(
        in_pdf_file=pdf_path,
        out_tiff_file=tif_path,
        pdf_page_number=1,
        resolution=300
    )

    # Adds the tif
    platLayer = m.addDataFromPath(tif_path)

    # Sets tif to active map projection
    arcpy.management.DefineProjection(tif_path, spatialRef)

    # Sets transparency; edit in method.
    setTransparencyTo25(platLayer)

    # Prints message if successful
    arcpy.AddMessage("PDF added successfully")

# Method to define transparency. Change number value to desired transparency if needed.
def setTransparencyTo25(platLayer):
    if platLayer:
        platLayer.transparency = 25


# Converts PDF path to Tif path while retaining directory info to later export to TIFF folder in Plat Database
def makeTifPathFromPDFPath(pdf_path):

    # Edit this path to own project temp tif folder
    tif_folder = r"C:\Users\jcberkey\Documents\ArcGIS\Projects\DOTROW_JACK_GEOREF\TempTIFFsForAutomation"
    
    pdf_folder = os.path.dirname(pdf_path)
    parent_folder = os.path.dirname(pdf_folder)
   
    # Since the parent folders for the project should remain constant, and we wont shif from SE for a while,
    # this path should always work. File strucutre must remain constant. If we switch regions, edit SE to region name in file.
    project_relative = os.path.relpath(parent_folder, r"Z:\PROJECTS\DOT_ROW\Plat Database\SE") 
    folder_code = project_relative.replace(os.sep, "_")
    
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    tif_name = f"{pdf_name}__FOLDER__{folder_code}.tif"

  
    tif_path = os.path.join(tif_folder, tif_name)

    return tif_path


if __name__ == "__main__":
    main()