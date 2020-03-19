HOW TO EXECUTE CODE TO INFER HAPLOTYPES FROM GENOTYPES

First, import the following libraries, as called at the top of the Python 3 file:
import pandas as pd
import numpy as np

Next, define the following functions, as implemented in the Python 3 file:
def decision(prob)
def unmask_genotype(masked)
def verify_unmasking(masked)
def fill_in_heterozygous_haplotypes(haplotypes)
def get_haplotypes(unmasked)

Finally, towards the bottom of the Python 3 file, you'll find my driver code that utilizes these functions to infer the haplotypes from masked genotypes. 
The block between the "for the provided examples:" comment and the "for the test case:" comment are for inferring the haplotypes from the example files provided; these can be ignored. Following the "for the test case:" comment, the location containing the text file for the masked genotype should be read into the masked_test variable, with the arguments that a whitespace is used to separate column values and that there is no header. 
The remaining lines can be executed in one block. The lines and their function are as follows:
The call to the function unmask_genotype(masked_test) is going to unmask the genotype matrix stored in the masked_test dataframe. 
The following if-statement verifies that the unmasking occurred as planned. If this statement prints "Error", that means a value in the masked genotype matrix was not unmasked. 
Assuming the unmasking proceded as planned, the haplotypes_test dataframe stores the haplotype matrix returned when the function get_haplotypes(masked_test) is run. 
The next line saves the produced haplotype dataframe at a specified location as a text file. 




    
