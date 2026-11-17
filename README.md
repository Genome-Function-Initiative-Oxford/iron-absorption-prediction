# Iron absorption prediction

Analysis code and trained models for:

> Stoffel NU, Riva SG, Sanders E, Das KP, Thankachan P, Zimmermann MB. Iron absorption prediction and
> individualised oral iron supplementation in premenopausal women: a machine learning model development
> and validation study. *Lancet Haematol* 2026.

An Extreme Gradient Boosting (XGBoost) model predicts fractional iron absorption from physiological,
biochemical and dietary predictors, using pooled stable-isotope iron absorption measurements in women.

## Contents

```
notebooks/   analysis notebooks, run in numeric order (executed, with outputs)
models/      trained XGBoost models (native JSON format)
results/     tables written by the notebooks (CSV)
figures/     Supplementary Figures 1-5, their panels, and the script that assembles them
data/        data dictionary; participant-level data are not included (see data/README.md)
```

The participant-level data needed to run the notebooks are available on request from the
corresponding author, Prof Michael B Zimmermann (michael.zimmermann@rdm.ox.ac.uk).

| Notebook | Results in the article |
|---|---|
| `01_main_model.ipynb` | Table 3 (all studies); Supplementary Figures 1 and 4; `models/model.json` |
| `02_shap_xgboost_vs_linear.ipynb` | Supplementary Figure 3 |
| `03_sensitivity_extreme_values_vitaminC.ipynb` | Supplementary Table 4; Supplementary Figure 2 |
| `04_sensitivity_feature_selection.ipynb` | Supplementary Table 5 |
| `05_subgroup_performance.ipynb` | Supplementary Table 6; Supplementary Figure 5 |
| `06_study1_predictions.ipynb` | Predicted absorption of the study 1 candidates (`models/model_4studyA.json`) |
| `07_study2_predictions.ipynb` | Predicted absorption of the study 2 candidates (`models/model_4studyB_withoutHep.json`) |
| `08_table3_supplement_and_meal_studies.ipynb` | Table 3 (all studies, supplement studies, meal studies) |

Tables 1, 2 and 4 (descriptive statistics and multivariable linear regression, SPSS) and the
statistical comparisons of the two evaluation studies (Figure 1) are not produced by this code.

## Models

| File | Predictors | Training data |
|---|---|---|
| `model.json` | 17: age, isotope, meal type, iron compound, iron dose, vitamin C, calcium, zinc, polyphenols, phytic acid, C-reactive protein, hepcidin, serum ferritin, haemoglobin, BMI, blood volume, circulating iron | 4046 measurements (80% of 5058) |
| `model_4studyA.json` | 13: age, iron dose, blood volume, circulating iron, menstrual cycle length, menses duration, haemoglobin, hepcidin, serum ferritin, soluble transferrin receptor, C-reactive protein, α1-acid glycoprotein, iron compound | oral supplement measurements (80% of 1244) |
| `model_4studyB_withoutHep.json` | 12: as above, without hepcidin | oral supplement measurements (80% of 1244) |

The target is log10(1 + fractional iron absorption, %); predictions are back-transformed with
10^ŷ − 1. Categorical predictors are integer codes of the sorted categories in the pooled dataset
(eg, iron compound 9 = ferrous sulphate, meal type 36 = oral supplement). Missing predictor values are
handled natively by XGBoost.

```python
import xgboost as xgb
model = xgb.XGBRegressor()
model.load_model("models/model.json")
```

## Running the analysis

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# place the data files in data/ (see data/README.md)
cd notebooks && jupyter nbconvert --to notebook --execute --inplace 0*.ipynb
cd ../figures && python make_figures.py
```

xgboost 1.7.5 and scikit-learn 1.5.2 are needed to reproduce the reported values exactly.

## Licence

All rights reserved. The code and models are available for inspection and verification of the
published results only; any other use requires written permission (see `LICENSE`).

## Contact

Michael B Zimmermann, MRC Translational Immune Discovery Unit, MRC Weatherall Institute of Molecular
Medicine, University of Oxford (michael.zimmermann@rdm.ox.ac.uk).
