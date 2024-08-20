import functions as fn
import pandas as pd
import random as rd

nmbr_days = 5
nmbr_prds = 8

faculty_availability = pd.read_csv('aiml_b_fac_availability.csv')
subjects = pd.read_csv('subjects.csv')

tbl = fn.create_table(nmbr_days, nmbr_prds)

subject_freqs = fn.subject_frequency(subjects)

for row in range(nmbr_days):
    for column in range(nmbr_prds):
        k = rd.choice(subject_freqs)

        #algorithm to be placed

        tbl[row][column].__init__(subject=k[0], fac=k[1])
        subject_freqs.remove(k)

fn.print_table(tbl)
