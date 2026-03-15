# ============================================================
# TP1 : Simulation de signaux numériques
# Matière : Technologies Multimédia Avancées
# Auteur : (Votre nom)
# Description :
# Ce TP permet de :
#  - Générer un signal sinusoïdal
#  - Ajouter un bruit blanc gaussien
#  - Manipuler un signal porte
#  - Calculer une convolution
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1.1 Génération d’un signal sinusoïdal
# ============================================================

# Paramètres du signal
f0 = 10          # Fréquence du signal en Hz
A = 1            # Amplitude
phi = 0          # Phase en radians

# Paramètres d'échantillonnage
fs = 100         # Fréquence d’échantillonnage (Hz)
T = 1            # Durée du signal (secondes)

# Création du vecteur temps
# np.arange(start, stop, step)
t = np.arange(0, T, 1/fs)

# Génération du signal sinusoïdal
# x(t) = A sin(2πf0t + φ)
x = A * np.sin(2 * np.pi * f0 * t + phi)

# # Affichage du signal
plt.figure()
plt.plot(t, x)
plt.title("Signal sinusoïdal x(t)")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


# ============================================================
# 1.2 Ajout de bruit blanc gaussien
# ============================================================

# Génération d’un bruit blanc gaussien
# moyenne = 0, écart-type = 0.3
bruit = np.random.normal(0, 0.3, len(x))

# Création du signal bruité
y = x + bruit

# Affichage comparatif
plt.figure()
plt.plot(t, x, label="Signal pur")
plt.plot(t, y, label="Signal bruité", alpha=0.7)
plt.title("Signal pur vs Signal bruité")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()


# ============================================================
# 1.3 Signal porte et convolution
# ============================================================

# Création d’un signal porte numérique
# Longueur totale = 100 points
rect = np.zeros(100)

# Valeur 1 entre les indices 20 et 40
rect[20:41] = 1

# Affichage du signal porte
plt.figure()
plt.stem(rect)
plt.title("Signal porte (Rect)")
plt.xlabel("Indice n")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# Convolution du signal porte avec lui-même
conv = np.convolve(rect, rect)

# Affichage de la convolution
plt.figure()
plt.plot(conv)
plt.title("Convolution du signal porte avec lui-même")
plt.xlabel("Indice n")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# ============================================================
# Fin du TP1
# ============================================================
