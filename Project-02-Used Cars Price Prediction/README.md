<div align="center">
🚗 Used Car Price Prediction
An End-to-End Regression Pipeline for Predicting Used Car Prices
![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Pipeline-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)
<img src="https://images.unsplash.com/photo-1494976388531-d1058494cdd8?auto=format&fit=crop&w=1200&q=80" alt="Used cars banner" width="100%">
</div>
---
📑 Table of Contents
Overview
Objectives
Project Structure
Dataset
Pipeline Walkthrough
Results
Installation
Usage
Tech Stack
Roadmap
Contributing
License
Author
Acknowledgments
---
📌 Overview
This project applies a complete, leakage-free regression pipeline to predict the price of a used car from its specifications — covering everything from raw data to a deployable model:
> **EDA → Cleaning & Preprocessing → Multi-Model Training → Cross-Validated Selection → Final Test Evaluation → Model Deployment**
The golden rule throughout: the test set is never touched until the very last step. Every modeling decision — which algorithm, which hyperparameters — is made using cross-validation on the training data only.
---
🎯 Objectives
[x] Apply a complete regression pipeline independently to a new dataset
[x] Perform data exploration, preprocessing, model training, and evaluation
[x] Select the best model based on cross-validated R²
[x] Persist the final model with `joblib` for future use
---
🗂️ Project Structure
```
used-car-price-prediction/
│
├── used_car_price_prediction.ipynb   # Full polished notebook (EDA → Deployment)
├── used_cars.csv                     # Dataset
├── used_cars_model.pkl               # Final trained & serialized model
├── LICENSE                           # MIT License
└── README.md                         # Project documentation
```
---
📊 Dataset
`used_cars.csv` contains 2,000 listings with the following features:
Feature	Type	Description
`brand`	categorical	Car manufacturer
`model`	categorical	Model name
`year`	numeric	Manufacturing year
`mileage_km`	numeric	Total kilometers driven
`fuel_type`	categorical	Petrol / Diesel / Hybrid / Electric
`transmission`	categorical	Automatic / Manual
`engine_cc`	numeric	Engine displacement (cc)
`owners`	numeric	Number of previous owners
`city`	categorical	Listing city
`color`	categorical	Exterior color
`accident_history`	binary	Whether the car has a recorded accident (0/1)
`price_thousand_pkr`	target	Price in thousand PKR
The dataset includes realistic noise: missing values in `mileage_km`, `engine_cc`, and `fuel_type`, a right-skewed price distribution, and genuine correlations between age, mileage, engine size, brand, and price.
---
🔬 Pipeline Walkthrough
<table>
<tr><td width="50%" valign="top">
1️⃣ Exploratory Data Analysis
Target & feature distributions
Categorical breakdowns by brand, fuel, transmission, city
Price vs. year / mileage scatter analysis
Correlation heatmap
2️⃣ Preprocessing
`SimpleImputer` for missing numeric & categorical values
`OneHotEncoder` for categorical features
`StandardScaler` for numeric features
All wrapped in a leakage-free `ColumnTransformer` + `Pipeline`
</td><td width="50%" valign="top">
3️⃣ Model Training
Baseline Linear Regression
Polynomial Regression (degree 2)
Ridge Regression — tuned via `GridSearchCV`
Lasso Regression — tuned via `GridSearchCV`
5-fold cross-validation throughout
4️⃣ Selection & Deployment
Compared models on mean CV R²
Final evaluation on untouched test set
Best pipeline saved via `joblib.dump()`
</td></tr>
</table>
---
🏆 Results
Model	Mean CV R²
Polynomial Regression (deg=2)	🥇 Winner
Ridge (tuned)	Competitive
Linear Regression	Baseline
Lasso (tuned)	Competitive
Final Test Set Performance (Polynomial Regression):
Metric	Score

R²	0.8949
RMSE	920.04 (thousand PKR)
> The model explains ~89.5% of the variance in used car prices on completely unseen data — a strong result for a linear-family model applied to a real-world-style pricing problem.
---
💻 Installation
```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/used-car-price-prediction.git
cd used-car-price-prediction

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn joblib jupyter
```
---
🚀 Usage
Run the notebook
```bash
jupyter notebook used_car_price_prediction.ipynb
```
Use the saved model directly
```python
import joblib
import pandas as pd

model = joblib.load("used_cars_model.pkl")

sample = pd.DataFrame([{
    "brand": "Toyota", "model": "Corolla", "year": 2020,
    "mileage_km": 35000, "fuel_type": "Petrol", "transmission": "Automatic",
    "engine_cc": 1600, "owners": 1, "city": "Lahore",
    "color": "White", "accident_history": 0
}])

predicted_price = model.predict(sample)
print(f"Predicted price: {predicted_price[0]:.1f} thousand PKR")
```
---
🧰 Tech Stack
`Python` · `Pandas` · `NumPy` · `scikit-learn` · `Matplotlib` · `Seaborn` · `joblib` · `Jupyter Notebook`
---
🗺️ Roadmap
[ ] Add tree-based models (Random Forest, XGBoost) for comparison
[ ] Build a simple Streamlit/Flask app for live predictions
[ ] Expand dataset with real-world scraped listings
[ ] Add SHAP-based feature importance explanations
---
🤝 Contributing
Contributions, issues, and feature requests are welcome!
Fork the repository
Create your feature branch (`git checkout -b feature/amazing-feature`)
Commit your changes (`git commit -m 'Add some amazing feature'`)
Push to the branch (`git push origin feature/amazing-feature`)
Open a Pull Request
---
📄 License
This project is licensed under the MIT License — see the LICENSE file for full details.
```
MIT License

Copyright (c) 2026 Mehr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```
---
👤 Author
Mehr
B.S. Computer Science (4th Semester) — FAST NUCES Peshawar
Kaggle Notebook Expert (Top 2% Global) · Aspiring Kaggle Grandmaster · Aspiring GitHub Campus Ambassador
<p>
<a href="https://www.kaggle.com/"><img src="https://img.shields.io/badge/Kaggle-View%20Profile-20BEFF?style=flat-square&logo=kaggle&logoColor=white"></a>
<a href="https://github.com/"><img src="https://img.shields.io/badge/GitHub-View%20Profile-181717?style=flat-square&logo=github&logoColor=white"></a>
</p>
---
🙏 Acknowledgments
Workflow adapted from an applied regression-pipeline assignment (insurance charges project)
Banner image via Unsplash
Built with scikit-learn
---
<div align="center">
<sub>⭐ If you found this project useful, consider giving it a star!</sub>
</div>
