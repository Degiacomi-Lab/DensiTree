# DensiTree 
Prediction of protein density using Random Forest Regressors. Released under GNU General Public License v3.0.

## DensiTree.py 
Contains classes for sequence and structure which allow for the easy estimation of protein density from sequences (either from PDB files, FASTA files, three-letter code sequence strings or one-letter code sequence strings) or structure-derived charactieristics (from PDB files). Automatically calculates the relevant features for the protein structure or sequence at a selected temperature (300K or 310.15K) 

## DensiTree.ipynb
Provides an easy-to-use interface for the use of DensiTree.py designed for use with [Google Colab](https://colab.research.google.com/), which allows for file uploads and text input of sequences. All dependencies are installed to create a conda environment consistent with itself and the trained random forest regressors to allow for easy prediction of protein density.

