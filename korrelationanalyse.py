import math
import pandas as pd
import numpy as np
import scipy.stats

'''
Zur Nullhypothese (H0)
Inhaltliche Nullhypothese:
Es gibt keinen oder einen negativen Zusammenhang zwischen Körpergröße und Körpergewicht.

Statistische Nullhypothese
r <= 0

Zur Alternativhypothese (H1)
# Inhaltliche Alternativhypothese:
Es gibt einen positiven Zusammenhang zwischen Körpergröße und Körpergewicht.

# Statistische Alternativhypothese:
r > 0

Die H1 ist eine gerichtete Hypothese. Daher wird ein einseitiger Signifikanztest durchgeführt.
'''

# Excel-Datei mit Beisspieldatensatz in ein Dataframe einlesen
df_raw = pd.read_excel('beispieldatensatz.xlsx')

# Korrelation nach Bravis-Pearson für Körpergröße und Körpergewicht bestimmen
r = np.corrcoef(df_raw['Körpergröße'], df_raw['Körpergewicht'])[0, 1]
r_rounded = np.round(r, decimals=3)

# Stichprobengröße
n = df_raw['Körpergröße'].count()

# Siginifikanzniveau festlegen
alpha = 0.05

# Emprischen t-Wert berechnen
t_emp = r/math.sqrt((1-r**2)/(n-2))
t_emp_rounded = np.round(t_emp, decimals=3)

# Kritischen T-Wert für Signifikanzniveau 0,05 berechnen
t_krit = scipy.stats.t.ppf(1-alpha, 19)
t_krit_rounded = np.round(t_krit, decimals=3)

print()
print(f"Korrelationskoeffizient (Pearson) ca. {r_rounded}.")
print(f"Empirische t-Wert ca. {t_emp_rounded}.")
print(f"Kritischer t-Wert ca. {t_krit_rounded}.")
print()

if(abs(t_krit) > abs(t_emp)):
    print("Der empirische Wert ist weniger extrem als der kritische t-Wert.")
    print(f"-> Die H0 kann auf diesem Signifikanzniveau (alpha={alpha}) nicht verworfen werden.")
    print("-> Die H1 konnte durch diesen Signifikanztest nicht erhärtet werden.")

if(abs(t_krit) < abs(t_emp)):
    print("Der empirische Wert ist extremer als der kritische t-Wert.")
    print(f"-> Die H0 kann auf diesem Signifikanzniveau (alpha={alpha}) verworfen werden")
    print("-> Die H1 konnte durch diesen Signifikanztest erhärtet werden.")

print()
