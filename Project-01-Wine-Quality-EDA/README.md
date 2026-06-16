
# 🍷 Wine Quality Exploratory Data Analysis (EDA)

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A comprehensive exploratory data analysis of the Wine Quality dataset, uncovering patterns, relationships, and actionable insights about physicochemical properties that influence wine quality ratings.

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Key Analyses](#key-analyses)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Notebooks](#notebooks)
- [Key Findings](#key-findings)
- [Dependencies](#dependencies)
- [Author](#author)
- [License](#license)

## 🎯 Overview

This project performs an in-depth exploratory data analysis on the Wine Quality dataset, which contains physicochemical measurements of wine samples along with quality ratings. Through systematic analysis, we investigate:

- **Data Quality**: Missing values, duplicates, and data type consistency
- **Univariate Patterns**: Distributions of key features (alcohol, acidity, sugar, etc.)
- **Bivariate Relationships**: How chemical properties relate to quality
- **Correlation Analysis**: Identifying the strongest predictors of wine quality
- **Statistical Insights**: Understanding the characteristics of high vs. low-quality wines

The analysis provides a strong foundation for predictive modeling and demonstrates best practices in data exploration.

## 📊 Dataset

**Source**: Wine Quality Dataset  
**Total Records**: 1,143 wine samples  
**Features**: 12 physicochemical properties + 1 quality rating  

### Features Included:

| Feature | Description | Type |
|---------|-------------|------|
| **fixed_acidity** | Non-volatile acids | Numeric |
| **volatile_acidity** | Acetic acid content | Numeric |
| **citric_acid** | Citric acid content | Numeric |
| **residual_sugar** | Remaining sugar after fermentation | Numeric |
| **chlorides** | Salt concentration | Numeric |
| **free_sulfur_dioxide** | Free SO₂ content | Numeric |
| **total_sulfur_dioxide** | Total SO₂ content | Numeric |
| **density** | Wine density | Numeric |
| **pH** | Acidity level (0-14 scale) | Numeric |
| **sulphates** | Potassium sulphate content | Numeric |
| **alcohol** | Alcohol content (%) | Numeric |
| **quality** | Quality rating (3-8 scale) | Integer |

**Data Quality**: 100% complete with no missing values or duplicates

## 📁 Project Structure

```
wine-quality-eda/
├── README.md                              # This file
├── requirements.txt                       # Python dependencies
├── WineQT.csv                             # Main dataset
│
├── Notebooks (Jupyter):
│   ├── week1assignment.ipynb              # Primary comprehensive EDA
│   └── WineQuality_EDA_YourName.ipynb     # Secondary analysis notebook
│
├── Python Scripts:
│   ├── run_notebook.py                    # Execute notebooks programmatically
│   ├── run_week1.py                       # Run week1 assignment
│   ├── validate_eda.py                    # Validate analysis results
│   └── eda_summary.py                     # Generate summary statistics
```

## 🔍 Key Analyses

### 1. **Data Inspection & Cleaning**
   - Dataset shape and structure verification
   - Missing value detection (0 missing values found)
   - Duplicate row identification (0 duplicates found)
   - Data type validation and standardization
   - Column name normalization (spaces → underscores)

### 2. **Univariate Analysis**
   - **Distribution Analysis**: 
     - Quality ratings histogram (most wines rated 5-6)
     - Alcohol content distribution (right-skewed)
     - Residual sugar distribution (highly skewed)
     - Fixed acidity distribution
   - **Outlier Detection**: Boxplots reveal extreme values in:
     - Alcohol content (8.4%-14.9%)
     - Residual sugar (0.9-15.5%)
     - Sulphates and acidity metrics

### 3. **Bivariate Analysis**
   - **Scatter Plots**: Alcohol vs. Quality (positive correlation evident)
   - **Grouped Boxplots**: 
     - Volatile acidity decreases with higher quality
     - Fixed acidity patterns across quality levels
   - **Violin Plots**: Residual sugar distribution by quality category
   - **Pairplot**: Multi-variable relationship matrix
   - **Regression Analysis**: Fitted trend lines showing relationships

### 4. **Statistical Insights**
   - Descriptive statistics by quality tier
   - Correlation coefficients (computed during analysis)
   - Distribution shape analysis (skewness/kurtosis)

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/wine-quality-eda.git
cd wine-quality-eda
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 🏃 Quick Start

### Option 1: Run Jupyter Notebooks Interactively
```bash
# Start Jupyter
jupyter notebook

# Then open either:
# - week1assignment.ipynb (comprehensive main analysis)
# - WineQuality_EDA_YourName.ipynb (secondary analysis)
```

### Option 2: Run Python Scripts
```bash
# Execute the primary analysis
python run_week1.py

# Validate EDA results
python validate_eda.py

# Generate summary report
python eda_summary.py

# Run all notebooks
python run_notebook.py
```

## 📓 Notebooks

### `week1assignment.ipynb` (Primary)
**Sections Covered**:
1. ✅ Library Imports & Configuration
2. ✅ Data Loading & Initial Inspection
3. ✅ Dataset Structure Analysis
4. ✅ Data Cleaning & Standardization
5. ✅ Univariate Analysis (7 visualizations)
6. ✅ Bivariate Analysis (5 visualizations)
7. ✅ Statistical Summaries
8. ✅ Key Insights & Conclusions

**Visualizations**: 12+ high-quality charts
- Histograms with KDE curves
- Boxplots for outlier detection
- Scatter plots with regression lines
- Violin plots for distribution comparison
- Pairplot for multi-variable exploration

### `WineQuality_EDA_YourName.ipynb` (Secondary)
Alternative analysis approach with additional perspectives and visualizations.

## 💡 Key Findings

### Discovering Wine Quality Drivers

1. **Alcohol Content** ⭐⭐⭐⭐⭐
   - Strong positive correlation with quality
   - Ranges from 8.4% to 14.9%
   - Higher alcohol wines tend to receive better ratings

2. **Volatile Acidity** ⭐⭐⭐⭐
   - Inverse relationship with quality
   - Acceptable range: 0.12 - 1.58 g/dm³
   - Lower volatile acidity = better quality

3. **Residual Sugar** ⭐⭐
   - Weak correlation with quality
   - Highly skewed distribution (most wines are dry)
   - Range: 0.9 - 15.5 g/dm³

4. **Fixed Acidity** ⭐⭐⭐
   - Moderate positive effect on quality
   - Normal-like distribution
   - Important for wine stability

5. **Quality Distribution**
   - Most wines rated 5-6 (average quality)
   - Few 3s or 8s (extreme ratings)
   - Well-balanced dataset for modeling

### Statistical Summary
- **Dataset**: 1,143 wine samples, 100% complete
- **Quality Range**: 3 (poor) to 8 (excellent)
- **Average Quality**: 5.66 ± 0.81
- **Mean Alcohol**: 10.44% ± 1.08%

## 📦 Dependencies

```txt
pandas>=1.3.0          # Data manipulation & analysis
numpy>=1.21.0          # Numerical computing
matplotlib>=3.4.0      # Plotting & visualization
seaborn>=0.11.0        # Statistical data visualization
nbclient>=0.5.0        # Notebook client
nbformat>=5.1.0        # Notebook format support
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 👤 Author

**Mehr Ali**  
AI/ML Internship Program  
Submission Date: June 16, 2026

## 📧 Contact & Support

For questions, issues, or suggestions:
- Create an issue on GitHub
- Contact: sheikhmehrali5@gmail.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- Wine Quality Dataset: UCI Machine Learning Repository
- Analysis methodology: Best practices in EDA
- Tools: Python, Jupyter, pandas, matplotlib, seaborn

---

## 📈 Future Enhancements

- [ ] Predictive modeling (classification/regression)
- [ ] Advanced feature engineering
- [ ] Machine learning model comparison
- [ ] Interactive visualizations with Plotly
- [ ] Hypothesis testing (statistical inference)
- [ ] Time-series analysis (if temporal data available)

---

<div align="center">

**Made with ❤️ as part of AI/ML Internship**

[⬆ Back to Top](#-wine-quality-exploratory-data-analysis-eda)

</div>
