# Similarity Analysis and Element Grouping App

## Overview

This Streamlit-based web application provides interactive data analysis tools for:

- **Similarity Analysis**: Visualizing similarity between elements based on a similarity matrix.
- **Elements Grouping**: Listing element groupings and calculating the number of members in each group.
- **Type Assignment**: Displaying element types with confidence percentages.


## Features

- **Upload CSV Files**: Users can upload their own similarity matrix for analysis.
- **Sample Data Option**: A preloaded sample dataset is available for testing.
- **Interactive Plots**: The app visualizes similarity data using bar plots.
- **Pagination**: Users can navigate through similarity results page by page.
- **CSV Download**: Filtered similarity data can be downloaded.

## Installation

### Prerequisites

```bash
pip install streamlit pandas seaborn matplotlib
```

## Usage

1. **Run the app**:
   ```bash
   streamlit run dashboard.py
   ```
2. **Upload Data**:
   - Upload a CSV file containing a similarity matrix.
   - Alternatively, use the provided sample dataset.
3. **Navigate Through Sections**:
   - **Similarity Analysis**: Choose an element, set a similarity threshold, and explore similar elements.
   - **Type Assignment**: View element types and confidence levels.
   - **Elements Grouping**: Check element groupings and member counts.

## File Format Requirements

- **Similarity Matrix CSV**:
  - Rows and columns should represent elements.
  - Values should indicate similarity scores (between 0 and 1).
- **Type Assignment CSV (`data/type.csv`)**:
  - Must contain columns: `element`, `type`, `confidence(%)`.
- **Elements Grouping CSV (`data/grouping.csv`)**:
  - Must contain columns: `group`, `members` (comma-separated list of members).

## Notes

- The app caches uploaded and sample data for efficiency.
- If issues arise with file loading, ensure the CSV file is correctly formatted.
