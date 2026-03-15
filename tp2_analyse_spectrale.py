# ============================================================
# TP2 : Analyse Spectrale et Filtrage
# Matière : Technologies Multimédia Avancées
# Auteur : (Votre nom)
# Description :
# - Analyse spectrale d’un son pur
# - Ajout d’un bruit haute fréquence
# - Filtrage fréquentiel
# - Reconstruction du signal
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 2.1 Analyse spectrale d’un son pur
# ============================================================

# Paramètres
fs = 44100          # Fréquence d'échantillonnage (Hz)
T = 1               # Durée du signal (1 seconde)
t = np.arange(0, T, 1/fs)

# Fréquences du signal
f1 = 440            # La3
f2 = 880            # La4

# Génération du signal
signal = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

# ================= FFT =================
N = len(signal)

fft_signal = np.fft.fft(signal)
freq = np.fft.fftfreq(N, 1/fs)

# On prend seulement la partie positive
fft_magnitude = np.abs(fft_signal[:N//2])
freq_positive = freq[:N//2]

# Affichage du spectre
plt.figure()
plt.plot(freq_positive, fft_magnitude)
plt.title("Spectre du signal pur (FFT)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


# ============================================================
# 2.2 Identification et Filtrage d’un bruit
# ============================================================

# 1) Ajout d’un bruit haute fréquence
fbruit = 5000
bruit = 0.3 * np.sin(2*np.pi*fbruit*t)

signal_bruite = signal + bruit

# FFT du signal bruité
fft_bruite = np.fft.fft(signal_bruite)
fft_bruite_magnitude = np.abs(fft_bruite[:N//2])

#Visualisation du spectre bruité
plt.figure()
plt.plot(freq_positive, fft_bruite_magnitude)
plt.title("Spectre du signal bruité")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


# ============================================================
# Filtrage fréquentiel (suppression du pic à 5000 Hz)
# ============================================================

# Copie du spectre
fft_filtre = fft_bruite.copy()

# Définition d'une bande autour de 5000 Hz à supprimer
bande = 100  # largeur de bande supprimée

# Mise à zéro des coefficients autour de 5000 Hz
for i in range(len(freq)):
    if abs(freq[i] - fbruit) < bande:
        fft_filtre[i] = 0
    if abs(freq[i] + fbruit) < bande:
        fft_filtre[i] = 0

# Reconstruction du signal
signal_filtre = np.fft.ifft(fft_filtre)

# On garde uniquement la partie réelle
signal_filtre = np.real(signal_filtre)

# ============================================================
# Comparaison temporelle
# ============================================================

plt.figure()
plt.plot(t[:2000], signal[:2000], label="Signal original")
plt.plot(t[:2000], signal_filtre[:2000], label="Signal filtré", alpha=0.7)
plt.title("Comparaison temporelle (zoom)")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

# ============================================================
# Fin TP2
# ============================================================