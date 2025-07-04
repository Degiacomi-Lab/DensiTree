# DensiTree 
Prediction of protein density using Random Forest Regressors. Released under GNU General Public License v3.0.

## DensiTree.py 
Contains classes for sequence and structure which allow for the easy estimation of protein density from sequences (either from PDB files, FASTA files, three-letter code sequence strings or one-letter code sequence strings) or structure-derived charactieristics (from PDB files). Automatically calculates the relevant features for the protein structure or sequence at a selected temperature (300K or 310.15K) 

## DensiTree.ipynb
Provides an easy-to-use interface for the use of DensiTree.py designed for use with [Google Colab](https://colab.research.google.com/), which allows for file uploads and text input of sequences. All dependencies are installed to create a conda environment consistent with itself and the trained random forest regressors to allow for easy prediction of protein density.

## Random Forests

(From random_forest/info.txt)

A range of random forest regressors trained on different features at both 310.15 K and 300 K are supplied here. When temperature is not noted, the temperature is 300 K as standard. The random forests are trained on 1ns simulations of proteins from a protein structure dataset derived from the Protein-Protein Docking Benchmark 5 (see: Vreven, Thom, Iain H. Moal, Anna Vangone, Brian G. Pierce, Panagiotis L. Kastritis, Mieczyslaw Torchala, Raphael Chaleil et al. "Updates to the integrated protein–protein interaction benchmarks: docking benchmark version 5 and affinity benchmark version 2." Journal of molecular biology 427, no. 19 (2015): 3031-3041.)
21 structures captured between 0 and 1 ns inclusive of a production run of an MD simulation for each protein structure are extracted.

 - RF_300_all is trained on the mean values of the mean values of all features (see figure S21 for a full list of features) for each protein in the 260-protein dataset.
 - RF_300_20 (AKA: struct_RF) is trained on the mean values of the 20 features found to be of the most importance by the ablation study (see figure S19 and S22).
 - RF_300_seq is trained on only the sequence data (the percentage composition of the protein sequence by residue) of each protein.

310.15K folder contains results obtained from 310.15 K simulations. The feature values consist of a range of physical characteristic values of a protein, ranging from the Solvent Accessible Surface Area to the percentage of residues in a coil configuration.

- RF_310_all is trained on all extracted features.
- RF_310_20 is trained on the mean values of the 20 features found to be of the most importance by the ablation study (see figure S19 and S22).
- RF_310_seq is trained on only the sequence data (the percentage composition of the protein sequence by residue) of each protein.
