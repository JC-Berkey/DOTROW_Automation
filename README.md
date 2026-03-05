# ArcGIS Pro Plat Automation Tools

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS-Pro-blue)
![Python](https://img.shields.io/badge/Python-ArcPy-green)
![Status](https://img.shields.io/badge/Status-Internal%20Tool-success)

Automates plat processing in ArcGIS Pro:

- **Import:** PDF → TIFF → Active Map  
- **Export:** Georeferenced TIFF → Structured Plat Database Folder  

Designed for:

```
Z:\PROJECTS\DOT_ROW\Plat Database\SE
```

---

## Workflow

### 1️⃣ Import Plat PDF
Run **Import Plat PDF**

- Select plat PDF  
- TIFF is created and added to active map  
- Projection matches map  
- Transparency set to 25%  
- Folder structure encoded in filename  

### 2️⃣ Georeference
Use standard ArcGIS Pro georeferencing tools.

### 3️⃣ Export Plat TIFF
Run **Export Plat TIFF**

- Select raster from dropdown  
- TIFF is copied to correct project `TIFF` folder  

✔ Done.

---

## One-Time Setup (Required)

### Import Script

Update temporary TIFF location (create a new temp folder in your ArcPro Project to hold created rasters; use that folder's path):

```python
tif_folder = r"C:\Your\Temp\TIFF\Folder"
```

Update region if not `SE`:

```python
r"Z:\PROJECTS\DOT_ROW\Plat Database\SE"
```

---

### Export Script

Update base project path if needed:

```python
project_base = r"Z:\PROJECTS\DOT_ROW\Plat Database\SE"
```

---

## Add Tools to ArcGIS Pro

### Add Import Tool

1. Open Toolbox  
2. Right-click → **New → Script**  
3. Name: `Import Plat PDF`  

Add parameter:

| Label    | Data Type | Direction |
|----------|----------|-----------|
| Plat PDF | File     | Input     |

---

### Add Export Tool

1. Right-click Toolbox → **New → Script**  
2. Name: `Export Plat TIFF`  

Add parameter:

| Label         | Data Type     | Direction |
|--------------|--------------|-----------|
| Raster Layer | Raster Layer | Input     |

After creating:

- Right-click tool → **Properties**
- Validation uses included `ToolValidator`
- Enables raster-only dropdown

---

## Naming Convention (Do Not Modify)

Import creates:

```
Plat123__FOLDER__County_Area_Block.tif
```

Export rebuilds:

```
...\County\Area\Block\TIFF\Plat123.tif
```

Changing this format will break export logic.

---

## Customization

| Setting | Location |
|----------|----------|
| Transparency | `platLayer.transparency = 25` |
| DPI | `PDFToTIFF(resolution=300)` |
| Region | Update `SE` in paths |

---

## Requirements

- ArcGIS Pro  
- Active map open  
- Standard Plat Database folder structure  
