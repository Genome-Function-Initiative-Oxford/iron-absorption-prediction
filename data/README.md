# Data

The participant-level data are not distributed with this repository. De-identified data can be made
available from the corresponding author upon reasonable request after publication, subject to
institutional and ethics approvals and a signed data access agreement (see the Data sharing statement
of the article). To request access to the data, contact the corresponding author,
Prof Michael B Zimmermann (michael.zimmermann@rdm.ox.ac.uk).

To run the notebooks, save the data files in this folder under the following names:

| File | Content | Used by |
|---|---|---|
| `pooled_dataset.xls` | Pooled stable-isotope iron absorption measurements (5058 measurements; first sheet) | all notebooks |
| `study1_candidates.xlsx` | Screening data of the study 1 candidates | `06_study1_predictions.ipynb` |
| `study2_candidates.xlsx` | Screening data of the study 2 candidates | `07_study2_predictions.ipynb` |

`data_dictionary.csv` lists the variables of the pooled dataset and their units. The study 1 and
study 2 files contain the subset of these variables used by the corresponding models, plus height and
weight.
