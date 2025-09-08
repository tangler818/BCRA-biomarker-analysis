# BCRA-biomarker-analysis
ML (Random Forest) guided biomarker identification 

This repo contains a Python script I created for identifying predictive breast cancer biomarkers using Random Forest and Recursive Feature Elimination (RFE), 
as well as the metadata CSV I compiled in Excel using data from GSE175692 on the Gene Expression Omnibus (GEO) via GEO2R.

# Project Overview

- Uses gene expression data to identify top features associated with breast cancer metastasis to different organs.
- Demonstrates basic data preprocessing, standardization, feature selection, and evaluation.

  # Instructions

  - Download 'PW1.csv'
  - Run the data sheet inside the BRCA_ML1.py script
  - Choose a target organ to run the model on - autmatically set to "Bone" - list includes Bone, Breast, Brain, Liver, Lung, Lymph Node, Muscle, Ovary, Pleura, Peritoneum, Skin
  - Can increase n_features_to_select if desired
  
    
