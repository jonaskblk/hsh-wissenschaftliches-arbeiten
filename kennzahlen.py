import pandas as pd
import numpy as np

# Ausgabe der Kennzahlen
def print_stats(merkmal_of_interest, stats_to_print):
    print('\n' + merkmal_of_interest)
    print('Modalwert:\t' + str(stats_to_print[0]))
    print('Median:\t\t' + str(stats_to_print[1]))
    print('Mittelwert:\t' + str(stats_to_print[2]))
    print('0.25-Quartil\t' + str(stats_to_print[3]))
    print('0.75-Quartil\t' + str(stats_to_print[4]))
    print('Varianz\t\t' + str(stats_to_print[5]))
    print('Standardabw.\t' + str(stats_to_print[6]))

# Methode zur Berechnung des Modalwertes
def mod(a):
    values, counts = np.unique(a, return_counts=True)
    ind = np.argmax(counts)
    return values[ind]

# Excel-Datei mit Beisspieldatensatz in ein Dataframe einlesen
df_raw = pd.read_excel('beispieldatensatz.xlsx')

# Kennzahlen ausgeben
stats = []

## Geschlecht
merkmal = 'Geschlecht'
stats.insert(0, mod(df_raw[merkmal]))
stats.insert(1, '-')
stats.insert(2, '-')
stats.insert(3, '-')
stats.insert(4, '-')
stats.insert(5, '-')
stats.insert(6, '-')
print_stats(merkmal, stats)

## Körpergröße
merkmal = 'Körpergröße'
stats.insert(0, '-')
stats.insert(1, np.median(df_raw[merkmal]))
stats.insert(2, np.round(np.mean(df_raw[merkmal]),decimals=1))
stats.insert(3, np.quantile(df_raw[merkmal], 0.25))
stats.insert(4, np.quantile(df_raw[merkmal], 0.75))
stats.insert(5, np.round(np.var(df_raw[merkmal]),decimals=2))
stats.insert(6, np.round(np.std(df_raw[merkmal]),decimals=2))
print_stats(merkmal, stats)

## Körpergewicht
merkmal = 'Körpergewicht'
stats.insert(0, '-')
stats.insert(1, np.median(df_raw[merkmal]))
stats.insert(2, np.round(np.mean(df_raw[merkmal]),decimals=1))
stats.insert(3, np.quantile(df_raw[merkmal], 0.25))
stats.insert(4, np.quantile(df_raw[merkmal], 0.75))
stats.insert(5, np.round(np.var(df_raw[merkmal]),decimals=2))
stats.insert(6, np.round(np.std(df_raw[merkmal]),decimals=2))
print_stats(merkmal, stats)

## Note
merkmal = 'Note'
stats.insert(0, mod(df_raw[merkmal]))
stats.insert(1, np.median(df_raw[merkmal]))
stats.insert(2, np.round(np.mean(df_raw[merkmal]),decimals=1))
stats.insert(3, np.quantile(df_raw[merkmal], 0.25))
stats.insert(4, np.quantile(df_raw[merkmal], 0.75))
stats.insert(5, np.round(np.var(df_raw[merkmal]),decimals=2))
stats.insert(6, np.round(np.std(df_raw[merkmal]),decimals=2))
print_stats(merkmal, stats)
