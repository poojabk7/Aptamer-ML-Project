"""
predict_molecule_category.py

Predicts the functional category of a small molecule from its SMILES notation
using a pretrained model and fingerprint vectorizer.

Requirements:
    • model.pkl           (trained RandomForest model)
    • label_encoder.pkl   (class name encoder)
    • These are generated during training if saved explicitly.

Example:
    python predict_molecule_category.py
"""

import joblib
from rdkit import Chem
from rdkit.Chem import AllChem


def smiles_to_fingerprint(smiles, radius=2, n_bits=2048):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=n_bits)
    return list(fp)


def predict_category(smiles):
    model = joblib.load("model.pkl")
    label_encoder = joblib.load("label_encoder.pkl")

    fingerprint = smiles_to_fingerprint(smiles)
    if fingerprint is None:
        return "Invalid SMILES input"

    prediction = model.predict([fingerprint])[0]
    decoded_label = label_encoder.inverse_transform([prediction])[0]
    return decoded_label


if __name__ == "__main__":
    input_smiles = "CCOC(=O)C1=CC=CC=C1"  # Example molecule — replace with your SMILES
    result = predict_category(input_smiles)
    print(f"Predicted category: {result}")
