# GPS–RTK Survey Analysis Dashboard

A Python-based desktop application for entering, processing, visualizing, and comparing GPS and RTK survey coordinates.

The project provides a lightweight environment for analyzing survey point datasets, calculating geometric properties, and examining coordinate differences between GPS and RTK measurements.

![Application Screenshot](docs/screenshot.png)

## Overview

GPS and RTK surveying produce geographic coordinate measurements that can differ due to positioning accuracy, measurement conditions, and other sources of error.

This project provides a simple workflow for:

- Entering GPS and RTK coordinates
- Converting geographic coordinates into a local Cartesian coordinate system
- Comparing corresponding GPS and RTK points
- Calculating coordinate differences
- Computing polygon area and perimeter
- Visualizing survey boundaries in 3D
- Editing, deleting, and reordering survey points
- Dynamically updating calculations and visualizations

The application is currently designed as a **desktop prototype for survey data analysis**, with future development focused on direct GNSS/RTK hardware integration and more advanced positioning analysis.

## Features

### Coordinate Processing

- Manual latitude, longitude, and altitude input
- Local X/Y/Z coordinate conversion
- Shared reference point for local coordinate calculations
- Separate GPS and RTK datasets

### GPS–RTK Comparison

For corresponding points, the application calculates:

- ΔX
- ΔY
- ΔZ

These values provide a basic representation of the positional difference between GPS and RTK measurements.

### Survey Geometry

The application calculates:

- Polygon area using the shoelace formula
- 3D perimeter using Euclidean distance
- Separate geometric measurements for GPS and RTK datasets

### Visualization

Survey points are displayed using an interactive Matplotlib 3D plot.

The visualization currently distinguishes:

- GPS points
- RTK points
- Survey boundaries

The plot is regenerated when the underlying point data is modified.

### Point Editing

Users can:

- Add points
- Delete selected points
- Select multiple points
- Swap the order of selected points

Point ordering is important because polygon area and perimeter calculations depend on the sequence of vertices.

## Technical Approach

### Coordinate Transformation

Geographic coordinates are converted into a local Cartesian system relative to the first reference point.

The current implementation uses an Earth-radius approximation:

```text
X ≈ Δlongitude × R × cos(reference latitude)
Y ≈ Δlatitude × R
Z = Δaltitude
```

where `R` is the approximate Earth radius.

This provides a convenient local coordinate representation for small survey areas.

> This implementation is intended for local analysis and is not currently a replacement for a rigorous geodetic coordinate reference system transformation.

### Area Calculation

Polygon area is calculated using the shoelace formula:

```text
A = 1/2 |Σ(xᵢyᵢ₊₁ − xᵢ₊₁yᵢ)|
```

The calculation assumes that the survey points are provided in the correct polygon order.

### Perimeter Calculation

The current perimeter calculation uses 3D Euclidean distance:

```text
d = √((x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²)
```

The distances between consecutive vertices are summed, including the closing segment between the final and first points.

### Error Calculation

For corresponding GPS and RTK points:

```text
Error = GPS − RTK
```

This produces a three-dimensional error vector:

```text
[ΔX, ΔY, ΔZ]
```

Future versions will extend this into horizontal error, 3D positional error, RMSE, and statistical analysis.

## Architecture

```text
User Input
    │
    ▼
Tkinter Interface
    │
    ├── GPS Dataset
    │
    ├── RTK Dataset
    │
    └── Point Editing
            │
            ▼
     Coordinate Processing
            │
            ├── Local X/Y/Z Conversion
            ├── GPS–RTK Differences
            ├── Area Calculation
            └── Perimeter Calculation
            │
            ▼
       Matplotlib 3D Plot
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| GUI | Tkinter |
| Numerical Processing | NumPy |
| Visualization | Matplotlib |
| Coordinate Processing | Python / NumPy |
| Development Environment | Linux / Windows compatible |

## Project Structure

```text
GPS-RTK/
│
├── dashboard/
│   ├── main.py
│   └── Project_screen.py
│
├── docs/
│   └── screenshot.png
│
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd GPS-RTK
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install numpy matplotlib
```

Tkinter may need to be installed separately depending on the operating system.

## Running the Application

From the project directory:

```bash
python dashboard/Project_screen.py
```

## Workflow

A typical analysis follows this sequence:

1. Enter GPS latitude, longitude, and altitude.
2. Add the GPS point.
3. Enter the corresponding RTK coordinates.
4. Add the RTK point.
5. Repeat for additional survey points.
6. Inspect the GPS and RTK datasets.
7. Compare coordinate differences.
8. View the generated 3D survey geometry.
9. Examine calculated area and perimeter.
10. Edit or reorder points when required.

## Current Limitations

The current implementation is intentionally lightweight and has several limitations:

- Coordinates are entered manually.
- No direct GNSS receiver connection.
- No NMEA parsing.
- No NTRIP/RTCM support.
- No formal CRS transformation.
- Limited statistical error analysis.
- No persistent project file format.
- No CSV/GeoJSON/KML import and export.
- Polygon validity and self-intersection are not currently validated.
- The current coordinate conversion is intended for relatively small local areas.

## Development Roadmap

### Data Analysis

- Horizontal positional error
- 3D positional error
- RMSE for X, Y, and Z
- Mean and maximum error
- Standard deviation
- Error distribution plots
- GPS–RTK error vectors

### Data Management

- CSV import/export
- Project save/load
- Survey metadata
- GeoJSON export
- KML export

### Visualization

- 2D survey map
- Improved point labels
- Error vector visualization
- Interactive point movement
- Better plot controls

### GNSS / RTK Integration

- Serial GNSS communication
- NMEA parsing
- Bluetooth GNSS receivers
- Live coordinate acquisition
- RTK FIX / FLOAT / SINGLE status
- Satellite and DOP information
- NTRIP client support
- RTCM correction data

### Geospatial Processing

- Proper coordinate reference systems
- Projection support
- Geodetic transformations
- Polygon validity checks
- GIS layer support

## Academic Context

This project explores the application of **Python-based computational methods to GNSS and RTK survey data analysis**.

The current implementation focuses on the processing pipeline:

```text
Geographic Coordinates
        ↓
Local Coordinate Transformation
        ↓
Survey Point Dataset
        ↓
Geometric Analysis
        ↓
GPS–RTK Comparison
        ↓
Visualization
```

The project can serve as a foundation for studying positioning accuracy, coordinate transformations, survey geometry, and GNSS/RTK error characteristics.

Future experimental work can evaluate positioning differences under different environments, measurement conditions, and receiver configurations.

## Future Research Direction

A more advanced version of the project could investigate:

- GPS versus RTK positioning accuracy
- RTK FIX versus FLOAT positioning
- Error behaviour under different satellite geometries
- Horizontal versus vertical positioning accuracy
- Environmental effects on GNSS measurements
- Statistical characterization of positioning errors
- Real-time GNSS data processing
- Integration of GNSS observations with GIS

## Status

**Current status:** Prototype / active development

The current version demonstrates the core survey analysis workflow. Hardware integration, advanced error statistics, geospatial standards, and real-time GNSS processing are planned extensions.

## Author

**Mohammed Shaheer**

B.Tech Artificial Intelligence  
SKUAST-K / IIT Mandi

## License

This project is currently intended for educational, academic, and experimental development.

A formal open-source license can be added as the project matures.
