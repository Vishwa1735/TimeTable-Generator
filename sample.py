import pandas as pd
import functions as fn
import random as rd

subjects = pd.read_csv('subjects.csv')


subject_freqs = fn.subject_frequency(subjects)


