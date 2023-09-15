import pandas as pd
import matplotlib.pyplot as plt

# Excel-Datei mit Beisspieldatensatz in ein Dataframe einlesen
df_raw = pd.read_excel('beispieldatensatz.xlsx')

# Je ein Dataframe für m und eines für w erzeugen
df_m = df_raw.loc[df_raw['Geschlecht'] == 'm']
df_w = df_raw.loc[df_raw['Geschlecht'] == 'w']

# Merkmal festlegen, für das die Box-Plots erzeugt werden sollen:
# Körpergewicht oder Körpergröße oder Note
# merkmal = 'Körpergewicht'
# merkmal = 'Körpergröße'
merkmal = 'Note'

# Für m und w nur die Daten in ein Dataframe laden, die Merkmalsausprägungen sind
data_m_merkmal = df_m[merkmal]
data_w_merkmal = df_w[merkmal]
df_summe_merkmal = df_raw[merkmal]
data_m_w_merkmal = [data_m_merkmal, data_w_merkmal, df_summe_merkmal]

# Benötigte Plots erzeugen: 1) Box-Plot und 2) die Achsen
bp, ax = plt.subplots(figsize=(5, 4))

# Box-Plots erstellen
bp = ax.boxplot(data_m_w_merkmal, labels=['Männlich', 'Weiblich', 'Gesamt'], patch_artist=True)

# Box-Plots einfärben
colors = ['lightblue', 'pink', 'lightgreen']
for b in bp:
    for patch, color in zip(bp['boxes'], colors):
        patch.set_color(color)

# Achsen beschriften
ax.set_xlabel('Geschlecht')
ax.set_ylabel(merkmal)

# Gitternetz anzeigen
ax.yaxis.grid(True)

# Vollständigen Plot anzeigen
plt.show()
