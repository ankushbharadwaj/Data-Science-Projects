#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:57:41 2020

@author: ankushbharadwaj
"""
import pandas as pd
import numpy as np

masked_genotype_1 = pd.read_csv("/Users/ankushbharadwaj/Desktop/assignment/example_data_1_masked.txt", sep = ' ', header = None)
masked_genotype_2 = pd.read_csv("/Users/ankushbharadwaj/Desktop/assignment/example_data_2_masked.txt", sep = ' ', header = None)

unmask_genotype(masked_genotype_1)
unmask_genotype(masked_genotype_2)

if verify_unmasking(masked_genotype_1):
    haplotypes_1 = get_haplotypes(masked_genotype_1)
    np.savetxt("/Users/ankushbharadwaj/Desktop/assignment/ex1_result.txt", haplotypes_1.values, fmt='%d')
else:
    print("Error in set 1")
    
if verify_unmasking(masked_genotype_2):
    haplotypes_2 = get_haplotypes(masked_genotype_2)
    np.savetxt("/Users/ankushbharadwaj/Desktop/assignment/ex2_result.txt", haplotypes_2.values, fmt='%d')
else:
    print("Error in set 2")

#for the test case:
masked_test = pd.read_csv("/Users/ankushbharadwaj/Desktop/assignment/test_data_masked.txt", sep = ' ', header = None)
unmask_genotype(masked_test)
if verify_unmasking(masked_test):
    haplotypes_test = get_haplotypes(masked_test)
    np.savetxt("/Users/ankushbharadwaj/Desktop/assignment/test_data_sol.txt", haplotypes_1.values, fmt='%d')
else:
    print("Error")