# Aptamer-ML 

This repository contains a complete computational framework for analyzing DNA/RNA aptamer sequences and predicting their binding properties using machine learning and chemical data. The goal is to make the workflow clear and accessible even for users without a bioinformatics background.

The project integrates sequence analysis, chemical feature extraction, machine learning models, and external database APIs into a single structured pipeline.

---

## What this project does

This repository enables the user to:

1. Process aptamer sequences and calculate their biological properties  
   (secondary structure, minimum free energy, loop counts, free base counts)
2. Convert experimental data into machine-learning compatible formats
3. Train models to predict binding affinity using sequence information
4. Use DeepChem to model high-dimensional sequence representations
5. Retrieve chemical information directly from the PubChem database
6. Classify small molecules from SMILES strings into functional categories

The entire pipeline is modular. Each component can be used independently or integrated with the others.

---

## Repository Structure Overview

```
Aptamer-ML-Project/
├── README.md
├── requirements.txt
├── Sequence_Processing/
│   rnafold_mfe.py
│   calculate_zscores.py
│   loop_count.py
│   free_base_count.py
├── DeepChem_Work/
│   numpy_array_conversion.py
│   deepchem_training_kmers_PCA.py
├── Binding_Affinity_Prediction/
│   RandomForest_Aptamer_Model.py
│   predict_binding_affinity.py
├── PubChem/
│   fetch_cids_pubchempy.py
│   fetch_properties_from_pubchem.py
└── SMILES_Classification/
    target_type_classification.py
```

Each folder corresponds to a major stage of the workflow.

---

## Installation and Requirements

It is recommended to use a virtual environment.

```
python -m venv venv
source venv/bin/activate          # Linux / macOS
venv\Scripts\activate             # Windows
```

Install dependencies:

```
pip install -r requirements.txt
```

For `rnafold_mfe.py`, the ViennaRNA package must be installed separately.

---

## How to run each module

| Purpose | Script | Summary |
|--------|--------|---------|
| Predict secondary structure and MFE values | `rnafold_mfe.py` | Uses RNAfold to compute folding energy |
| Calculate Z-scores based on MFE results | `calculate_zscores.py` | Performs statistical normalization |
| Count structural loops | `loop_count.py` | Measures paired-region loops from dot-bracket notation |
| Count free/unpaired bases | `free_base_count.py` | Measures structural flexibility |
| Convert Excel to NumPy for ML | `numpy_array_conversion.py` | Converts experimental tables to ML-ready format |
| Train DeepChem PCA-based regression | `deepchem_training_kmers_PCA.py` | Uses k-mers + PCA to predict molecular weight |
| Train RandomForest binding affinity model | `RandomForest_Aptamer_Model.py` | Predicts binding affinity from sequence | 
| Predict affinity using a trained model | `predict_binding_affinity.py` | Takes a new sequence as input |
| Get PubChem CID from chemical name | `fetch_cids_pubchempy.py` | Queries PubChem automatically |
| Retrieve molecular properties using CID | `fetch_properties_from_pubchem.py` | Fetches physicochemical parameters |
| Classify small molecules from SMILES | `target_type_classification.py` | Predicts functional class (e.g., antibiotic) |

Each script contains internal comments and can be executed independently.

---

## When to use this repository

This project is suitable for:

- Students and researchers working with aptamers
- Chemoinformatics and bioinformatics users
- Machine learning practitioners interested in biological sequence data
- Anyone exploring the interaction of small molecules with nucleic acids

Users do **not** need deep biological expertise to run the pipeline. All data transformations and model training steps are automated inside the scripts.

---

## Citation and Use

This project is made available for academic and research purposes.  
Users are requested to acknowledge the author if this repository contributes to any publication or academic submission.

