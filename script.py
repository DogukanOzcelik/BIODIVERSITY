import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns

observations = pd.read_csv('data/observations.csv')
species = pd.read_csv('data/species_info.csv')

# ------ species_info.csv ------
# category - class of animal
# scientific_name - the scientific name of each species
# common_name - the common names of each species
# conservation_status - each species’ current conservation status

# ------ observations.csv ------
# scientific_name - the scientific name of each species
# park_name - Park where species were found
# observations - the number of times each species was observed at park

print(observations.head())
print(species.head())