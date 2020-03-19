#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:57:40 2020

@author: ankushbharadwaj
"""

import numpy as np

def decision(prob):
    return(np.random.binomial(1,prob))

def unmask_genotype(masked):
    for row in range(len(masked)):
        value_counts = masked.iloc[row].value_counts()
        if ("0" in value_counts): 
            countsof0 = value_counts["0"] 
        else:
            countsof0 = 0
        if ("1" in value_counts): 
            countsof1 = value_counts["1"] 
        else:
            countsof1 = 0
        if ("2" in value_counts): 
            countsof2 = value_counts["2"] 
        else:
            countsof2 = 0
        totalcounts = countsof1 + countsof2 + countsof0
        probability_2 = countsof2/totalcounts
        for individual in range(len(masked.iloc[row])):
            if masked.iloc[row].iloc[individual] == "*":
                if decision(probability_2):
                    masked.iloc[row].iloc[individual] = 2
                else:
                    masked.iloc[row].iloc[individual] = 0
    return

def verify_unmasking(masked):
    for row in range(len(masked)):
        value_counts = masked.iloc[row].value_counts()
        if ("*" in value_counts):
            return(False)
    return(True)