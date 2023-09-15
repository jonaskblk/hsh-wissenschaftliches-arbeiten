import pandas as pd
import numpy as np


# Methode zur Berechnung des Modalwertes
def mod(a):
    values, counts = np.unique(a, return_counts=True)
    ind = np.argmax(counts)
    return values[ind]


def get_stats(datapoints):
    stats_of_interest = []

    stats_of_interest.insert(0, mod(datapoints))
    stats_of_interest.insert(1, np.median(datapoints))
    stats_of_interest.insert(2, np.round(np.mean(datapoints), decimals=1))
    stats_of_interest.insert(3, np.quantile(datapoints, 0.25))
    stats_of_interest.insert(4, np.quantile(datapoints, 0.75))
    stats_of_interest.insert(5, np.min(datapoints))
    stats_of_interest.insert(6, np.max(datapoints))
    stats_of_interest.insert(7, np.round(np.var(datapoints), decimals=2))
    stats_of_interest.insert(8, np.round(np.std(datapoints),decimals=2))

    return stats_of_interest


# Excel-Datei mit Beisspieldatensatz in ein Dataframe einlesen
df_raw = pd.read_excel('beispieldatensatz.xlsx')

# Je ein Dataframe für m und eines für w erzeugen
df_m = df_raw.loc[df_raw['Geschlecht'] == 'm']
df_w = df_raw.loc[df_raw['Geschlecht'] == 'w']

# Kennzahlen ermitteln
kennzahlen = ['mod', 'med', 'x̄', 'q1', 'q3', 'min', 'max', 'var', 'sd']
merkmale = ['Körpergröße', 'Körpergewicht', 'Note']

df_kennzahlen = pd.DataFrame(index=kennzahlen)
get_stats(datapoints=df_raw[merkmale[0]])

# Körpergröße
df_kennzahlen.insert(0, "Körpergröße", get_stats(datapoints=df_raw[merkmale[0]]), True)
df_kennzahlen.insert(1, "Körpergröße (m)", get_stats(datapoints=df_m[merkmale[0]]), True)
df_kennzahlen.insert(2, "Körpergröße (w)", get_stats(datapoints=df_w[merkmale[0]]), True)

# Körpergewicht
df_kennzahlen.insert(3, "Körpergewicht", get_stats(datapoints=df_raw[merkmale[1]]), True)
df_kennzahlen.insert(4, "Körpergewicht (m)", get_stats(datapoints=df_m[merkmale[1]]), True)
df_kennzahlen.insert(5, "Körpergewicht (w)", get_stats(datapoints=df_w[merkmale[1]]), True)

# Note
df_kennzahlen.insert(6, "Note", get_stats(datapoints=df_raw[merkmale[2]]), True)
df_kennzahlen.insert(7, "Note (m)", get_stats(datapoints=df_m[merkmale[2]]), True)
df_kennzahlen.insert(8, "Note (w)", get_stats(datapoints=df_w[merkmale[2]]), True)

df_kennzahlen.to_excel('kennzahlen.xlsx')
