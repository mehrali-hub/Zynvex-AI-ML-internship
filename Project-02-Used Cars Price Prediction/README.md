# 🚗 Used Car Price Prediction

**An end-to-end regression pipeline that predicts used car resale prices from vehicle specifications.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-pipeline-orange.svg)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/status-complete-brightgreen.svg)]()

---

## Why this project exists

Most "regression tutorials" hand you a clean, thousand-row dataset and a model that just works. This one doesn't. `used_cars.csv` is **52 real-world scraped listings** across 6 brands, 15 models, and 27 raw attributes — small, messy, and full of high-cardinality categorical noise (a `model` column with as many unique values as there are rows in some folds). That makes it a far more honest test of a regression pipeline than a textbook dataset, and it's exactly why the results below are interesting: **an unregularized linear model doesn't just underperform here, it collapses**, while regularization rescues it almost entirely. That contrast is the whole point of this repo.

## What's inside

```
used_cars_project/
├── data/
│   └── used_cars.csv                       # raw dataset
├── notebooks/
│   └── used_cars_price_prediction.ipynb    # full, executed pipeline
├── models/
│   └── used_cars_model.pkl                 # final persisted model (joblib)
├── images/
│   └── *.png                               # exported EDA & evaluation plots
├── requirements.txt
├── LICENSE
└── README.md
```

## Pipeline

The notebook runs a single, leak-proof pipeline from raw CSV to a deployable artifact:

| Stage | What happens |
|---|---|
| **1. Explore** | Structure, dtypes, missingness audit, distribution plots, correlation heatmap, brand/engine-type price breakdowns |
| **2. Clean** | Drop `id`, `link` (no predictive signal), `condition` (98% missing), `type` (zero variance — every row is `sedan`) |
| **3. Preprocess** | `ColumnTransformer`: median imputation + `StandardScaler` for numeric features, most-frequent imputation + `OneHotEncoder` for categoricals (`brand`, `model`, `engine_type`) |
| **4. Split** | 80/20 train/test — **the test set is sealed here and never seen again until Section 7** |
| **5. Train** | Linear Regression (baseline), Polynomial Regression (degree 2), Ridge (`GridSearchCV` over 7 alphas), Lasso (`GridSearchCV` over 7 alphas) — all wrapped in `Pipeline` objects to prevent preprocessing leakage |
| **6. Compare** | 5-fold cross-validated R² for every candidate, summarized in a table and bar chart |
| **7. Evaluate** | Winning model scored once, on the held-out test set, with R² and RMSE |
| **8. Persist** | Final pipeline serialized with `joblib.dump()`, then reloaded and verified to produce identical predictions |

## Results

| Model | Mean CV R² | Std CV R² |
|---|---|---|
| Linear Regression (baseline) | **−1,208,593.96** | — |
| Polynomial Regression (deg=2) | −3.12 | 4.04 |
| **Ridge Regression (α=10)** | **0.452** | 0.189 |
| Lasso Regression (α=10) | 0.344 | 0.239 |

**Selected model: Ridge Regression**
**Held-out test performance: R² = 0.348, RMSE ≈ $1,986**

### Reading the baseline collapse correctly

That eight-figure-negative R² for plain Linear Regression isn't a bug — it's the model. One-hot encoding `brand` and `model` against ~41 training rows pushes the feature space close to (and at times past) the rank the data can support, so the unregularized normal-equation solution explodes on any fold where a category split unevenly. Polynomial expansion makes this worse before regularization fixes it. **This is precisely the scenario L2/L1 penalties exist for**, and the gap between −1.2M and 0.45 R² across the table is the clearest demonstration in this repo of why you never ship a baseline without comparing it against a regularized alternative.

## Running it yourself

```bash
# 1. Set up environment
pip install -r requirements.txt

# 2. Run the notebook top to bottom
jupyter notebook notebooks/used_cars_price_prediction.ipynb
```

## Using the saved model

```python
import joblib
import pandas as pd

model = joblib.load("models/used_cars_model.pkl")

# new_data must have the same raw columns the pipeline was trained on
# (minus id, link, condition, type, price — the pipeline handles
# imputation, scaling, and encoding internally)
predicted_price = model.predict(new_data)
```

## Methodology notes

- **No leakage**: every transformation (imputation, scaling, encoding) lives inside the `sklearn.Pipeline`/`ColumnTransformer`, fit only on training folds during cross-validation and refit on the full training set before touching the test set.
- **Model selection on CV, not test**: the test set is split off in Section 4 and not referenced again until Section 7 — selection is based purely on 5-fold cross-validated R² on training data.
- **Small-data caveat**: with 52 rows, single-digit-sized test folds mean these metrics carry real variance. The qualitative finding (regularization >> unregularized linear/polynomial models on high-cardinality, low-sample data) is the durable takeaway; treat the exact R²/RMSE as directional rather than final-product-grade.

## Author

**Mehr** — BS Computer Science (FAST NUCES Peshawar), Machine Learning & Data Science.

## License

Released under the [MIT License](LICENSE) — free to use, modify, and distribute.
