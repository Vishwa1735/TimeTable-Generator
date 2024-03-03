import functions as fn
import pandas as pd
import random as rd

nmbr_days = 8
nmbr_prds = 5

faculty_availability = pd.read_csv('aiml_b_fac_availability.csv')
subjects = pd.read_csv('subjects.csv')

tbl = fn.create_table(nmbr_days, nmbr_prds)




fn.print_table(tbl)
