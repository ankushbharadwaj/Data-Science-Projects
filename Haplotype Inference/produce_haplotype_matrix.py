#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:57:41 2020

@author: ankushbharadwaj
"""
import numpy as np
import pandas as pd

def fill_in_heterozygous_haplotypes(haplotypes):
    new_haplotypes = haplotypes
    for row in range(len(haplotypes)):
        for individual in range(len(haplotypes.iloc[row])):
            if int(haplotypes.iloc[row][individual]) == -1:
                if individual == 0:
                    new_haplotypes.iloc[row][individual] = np.where(haplotypes.iloc[row] != -1)[0][0]
                    if new_haplotypes.iloc[row][individual] == 1:
                        new_haplotypes.iloc[row][individual+1] = 0
                    else:
                        new_haplotypes.iloc[row][individual+1] = 1
                else:
                    closest_val_arr = np.where(haplotypes.iloc[row] != -1)[0]
                    distances_away_arr = abs(closest_val_arr - individual)
                    distances_away_val = min(abs(closest_val_arr - individual))
                    closest_val_index = np.where(distances_away_arr == distances_away_val)[0][0]
                    new_haplotypes.iloc[row][individual] = haplotypes.iloc[row][closest_val_index]
                    if new_haplotypes.iloc[row][individual] == 1:
                        new_haplotypes.iloc[row][individual+1] = 0
                    else:
                        new_haplotypes.iloc[row][individual+1] = 1
                individual = individual + 1
    return(new_haplotypes)
    
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
    haplotypes = fill_in_heterozygous_haplotypes(haplotypes)
    return(haplotypes)