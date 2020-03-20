#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:57:41 2020

@author: ankushbharadwaj
"""
import numpy as np
import pandas as pd

def fill_in_heterozygous_haplotypes(hap_row):
    for i in range(len(hap_row)):
        if int(hap_row[i]) == -1:
            if i == 0:
                hap_row[i] = np.where(hap_row != 1)[0][0]
                if hap_row[i] == 1:
                    hap_row[i+1] == 0
                else:
                    hap_row[i+1] == 1
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
    
def get_haplotypes(unmasked):
    haplotypes = pd.DataFrame(index = range(len(unmasked)), columns = range(2*unmasked.shape[1]))
    for row in range(len(unmasked)):
        array_for_current_row = []
        for i in unmasked.iloc[row]:
            if int(i) == 2:
                array_for_current_row.append(1)
                array_for_current_row.append(1)
            if int(i) == 0:
                array_for_current_row.append(0)
                array_for_current_row.append(0)
            elif int(i) == 1:
                array_for_current_row.append(-1)
                array_for_current_row.append(-1)
        haplotypes.iloc[row] = array_for_current_row
        if -1 in haplotypes.iloc[row].value_counts():
            fill_in_heterozygous_haplotypes(haplotypes.iloc[row])
    return(haplotypes)
