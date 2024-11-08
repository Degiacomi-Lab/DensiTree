# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:34:35 2024

@author: hkwf34
"""

#%% Example usage
import Classes as Cs
import pickle

seq = Cs.Protein("ADTRYPGDDDDFFFAACC", "sequence") 

struct = Cs.Protein("sample_data/5pti_frame_0_nowater.pdb", "structure") 

seq_results = seq.predict()

struct_results = struct.predict()

with open("random_forests/RF_300_means.pickle", "rb") as r_file:
    RF_structure_means = pickle.load(r_file)
        
struct_results_means = struct.predict(RF_structure_means)
