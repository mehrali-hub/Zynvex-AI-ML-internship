# 🍷 Wine Quality EDA 

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-2ea44f.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Project%20Ready-success)]()

An energetic, notebook-driven exploratory data analysis of the Wine Quality dataset. This project explores what shapes wine quality, how the features relate to one another, and which measurements stand out most strongly when looking for patterns that matter.

## What this project does

- Loads and inspects the Wine Quality dataset
- Checks for missing values, duplicates, and data quality issues
- Visualizes feature distributions and outliers
- Compares wine chemistry against quality ratings
- Builds a correlation view of the full dataset
- Summarizes the most important insights for next-step modeling

## Why it matters

Wine quality is influenced by a mix of acidity, sugar, alcohol, sulfur dioxide, and other chemical properties. This notebook helps turn raw measurements into readable insight, making it easier to understand which features are most associated with stronger wine ratings.

## Dataset

The dataset in this repository contains **1,143 wine samples** and **13 columns** in total.

### Columns in the CSV

| Column | Description |
|---|---|
| `fixed acidity` | Non-volatile acids in wine |
| `volatile acidity` | Acetic acid level |
| `citric acid` | Citric acid content |
| `residual sugar` | Sugar remaining after fermentation |
| `chlorides` | Salt content |
| `free sulfur dioxide` | Free SO₂ amount |
| `total sulfur dioxide` | Total SO₂ amount |
| `density` | Wine density |
| `pH` | Acidity scale |
| `sulphates` | Sulphate content |
| `alcohol` | Alcohol percentage |
| `quality` | Wine quality score |
| `Id` | Row identifier |

## Project Files

```text
Wine Quality EDA/
├── README.md
├── LICENSE
├── requirements.txt
├── WineQT.csv
├── WineQuality_EDA_MehraliHub.ipynb
├── WineQuality_Mehrali-hub.ipynb
├── run_winequality_eda.py
├── execute_winequality_notebook.py
├── validate_eda.py
├── eda_summary.py
└── CONTRIBUTING.md
```

## Notebook Highlights

### `WineQuality_EDA_MehraliHub.ipynb`
This is the main notebook and the best place to start. It covers:

1. Library setup and plotting configuration
2. Dataset loading and preview
3. Shape, info, and summary statistics
4. Cleaning checks and column standardization
5. Univariate analysis for core variables
6. Bivariate analysis using scatter plots and boxplots
7. Pairplot exploration for selected features
8. Correlation analysis and ranking of drivers of quality

### `WineQuality_Mehrali-hub.ipynb`
This notebook provides an alternate EDA flow with a similar analysis style and supporting visualizations.

## Key Insights

- **Alcohol** shows the strongest positive association with wine quality.
- **Volatile acidity** is negatively related to quality, which makes it an important signal to watch.
- **Residual sugar** is present, but its relationship with quality is weaker and more skewed.
- **pH** and acidity-related features help add context, especially in the correlation view.
- The dataset is clean, complete, and ready for analysis or lightweight modeling.

## Quick Start

### Install dependencies

```bash
pip install -r requirements.txt
```

### Open the notebook in Jupyter

```bash
jupyter notebook
```

Then open:

- `WineQuality_EDA_MehraliHub.ipynb`
- `WineQuality_Mehrali-hub.ipynb`

### Run the project scripts

```bash
python run_winequality_eda.py
python execute_winequality_notebook.py
python validate_eda.py
python eda_summary.py
```

## Installation Notes

- Python 3.8 or newer is recommended.
- Use a virtual environment if you want a clean local setup.
- The dataset file `WineQT.csv` should stay in the project root.

## Dependencies

The project uses the packages listed in [requirements.txt](requirements.txt):

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `nbclient`
- `nbformat`

## Author

**Mehr Ali**

## License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for the full text.

## Acknowledgment

Built for EDA practice and presentation on the Wine Quality dataset. The goal is to keep the analysis clean, readable, and useful for future modeling work.
