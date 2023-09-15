import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the standard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the standard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

# Excel-Datei mit Beisspieldatensatz in ein Dataframe einlesen
df_raw = pd.read_excel('beispieldatensatz.xlsx')

# Je ein Dataframe für m und eines für w erzeugen
df_m = df_raw.loc[df_raw['Geschlecht'] == 'm']
df_w = df_raw.loc[df_raw['Geschlecht'] == 'w']

# Für m und w nur die Daten in ein Dataframe laden, die Merkmalsausprägungen sind
data_m_groesse = df_m['Körpergröße']
data_m_gewicht = df_m['Körpergewicht']
data_w_groesse = df_w['Körpergröße']
data_w_gewicht = df_w['Körpergewicht']
df_summe_groesse = df_raw['Körpergröße']
df_summe_gewicht = df_raw['Körpergewicht']

# Plot erstellen
bp, ax = plt.subplots(figsize=(5, 4))
scatter = ax.scatter(df_summe_groesse, df_summe_gewicht, c='blue', s=20, zorder=5)

# Ellipse für Standardabweichung erzeugen
confidence_ellipse(df_summe_groesse, df_summe_gewicht, ax, \
                   alpha=0.5, facecolor='pink', edgecolor='purple', zorder=2)

# Achsen und Gitternetz konfigurieren
ax.set(xlabel='Körpergröße [in cm]', ylabel='Körpergewicht [in kg]')
ax.yaxis.grid(True, zorder=1)
ax.xaxis.grid(True, zorder=1)

# Vollständigen Plot anzeigen
plt.show()
