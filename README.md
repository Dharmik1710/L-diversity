# L-diversity

Very simple and basic Implementation of k-diversity

The implementation of k-diversity is done in python.

Race is taken as the sensitive attribute in this data.

There are four parts of this algorithm

1) Read and store the data from the .data file into a python hash table with key as the attributes and their values as values from file.
2) Categories the given data into equivalent classes such  that they are k-diverse
3) Generalize the records in equivalent classes using bottum up generalizatio algorithm.
4) Store the k-diverse data in .data file.
