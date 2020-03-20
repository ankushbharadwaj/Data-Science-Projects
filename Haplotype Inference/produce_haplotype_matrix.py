#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 04:24:38 2020

@author: ankushbharadwaj
"""
import pandas as pd
import numpy as np

def fill_in_heterozygous_haplotypes(hap_row):
    if (-1 not in hap_row.value_counts()):
        return
    for i in range(len(hap_row)):
        if int(hap_row[i]) == -1:
            if i == 0:
                hap_row[i] = hap_row[np.where(hap_row != -1)[0][0]]
                if hap_row[i] == 1:
                    hap_row[i+1] = 0
                else:
                    hap_row[i+1] = 1
            else:
                closest_val_arr = np.where(hap_row != -1)[0]
                distances_away_arr = abs(closest_val_arr - i)
                distances_away_val = min(abs(closest_val_arr - i))
                closest_val_index = np.where(distances_away_arr == distances_away_val)[0][0]
                hap_row[i] = hap_row[closest_val_index]
                if hap_row[i] == 1:
                    hap_row[i+1] = 0
                else:
                    hap_row[i+1] = 1
            i = i + 1
    return
    
def get_haplotypes(masked):
    haplotypes = pd.DataFrame(index = range(len(masked)), columns = range(2*masked.shape[1]))
    for row in range(len(masked)):
        array_for_current_row = []
        current_row = masked.iloc[row]
        if "*" in current_row.value_counts():
            unmask_genotype(masked.iloc[row])
        for i in range(len(current_row)):
            if int(current_row[i]) == 2:
                array_for_current_row.append(1)
                array_for_current_row.append(1)
            if int(current_row[i]) == 0:
                array_for_current_row.append(0)
                array_for_current_row.append(0)
            if int(current_row[i]) == 1:
                array_for_current_row.append(-1)
                array_for_current_row.append(-1)
        haplotypes.iloc[row] = array_for_current_row
        fill_in_heterozygous_haplotypes(haplotypes.iloc[row])
    return(haplotypes)