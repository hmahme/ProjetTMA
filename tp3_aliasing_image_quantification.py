# ============================================================
# TP3 : Aliasing Audio et Quantification d'Image
# Matière : Technologies Multimédia Avancées
# Auteur : (Votre nom)
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import cv2
from scipy.io import wavfile

# ============================================================
# PARTIE 1 : AUDIO ET ALIASING
# # ============================================================

# # 1) Chargement du fichier audio (wav 44.1 kHz)
audio_path = "C:\Users\HP\Desktop\TMA\TP3\audio.mp4"   # <-- mettre votre fichier ici
signal, fs = librosa.load(audio_path, sr=None)

print("Fréquence d'échantillonnage :", fs)

# # ------------------------------------------------------------
# # 2) Sous-échantillonnage sauvage (1 échantillon sur 10)
# # ------------------------------------------------------------
signal_down = signal[::10]
fs_down = fs // 10

print("Nouvelle fréquence :", fs_down)

# # Sauvegarde du fichier sous-échantillonné
wavfile.write("C:\Users\HP\Desktop\TMA\TP3\mp4",
              fs_down,
              (signal_down * 32767).astype(np.int16))

# ------------------------------------------------------------
# 3) Spectrogramme comparaison
# ------------------------------------------------------------

plt.figure(figsize=(10,4))
D = librosa.amplitude_to_db(np.abs(librosa.stft(signal)), ref=np.max)
librosa.display.specshow(D, sr=fs, x_axis='time', y_axis='hz')
plt.title("Spectrogramme Original")
plt.colorbar()
plt.show()

plt.figure(figsize=(10,4))
D_down = librosa.amplitude_to_db(np.abs(librosa.stft(signal_down)), ref=np.max)
librosa.display.specshow(D_down, sr=fs_down, x_axis='time', y_axis='hz')
plt.title("Spectrogramme Sous-échantillonné")
plt.colorbar()
plt.show()

# ============================================================
# PARTIE 2 : IMAGE ET QUANTIFICATION
# ============================================================

# 1) Charger image en niveaux de gris
image_path = "C:\Users\HP\Desktop\TMA\TP3\photo.jpg"   # <-- mettre votre image ici
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

plt.figure()
plt.imshow(img, cmap='gray')
plt.title("Image originale (8 bits)")
plt.axis('off')
plt.show()

# ------------------------------------------------------------
# 2) Quantification à 2 bits (4 niveaux)
# ------------------------------------------------------------
img_2bits = (img // 64) * 64

plt.figure()
plt.imshow(img_2bits, cmap='gray')
plt.title("Quantification 2 bits (4 niveaux)")
plt.axis('off')
plt.show()

# ------------------------------------------------------------
# Quantification à 1 bit (2 niveaux)
# ------------------------------------------------------------
img_1bit = (img // 128) * 255

plt.figure()
plt.imshow(img_1bit, cmap='gray')
plt.title("Quantification 1 bit (2 niveaux)")
plt.axis('off')
plt.show()

# ------------------------------------------------------------
# 4) Pixelisation (réduction résolution spatiale)
# ------------------------------------------------------------

h, w = img.shape

# Réduction taille /8
img_small = cv2.resize(img, (w//8, h//8), interpolation=cv2.INTER_NEAREST)

# Ré-agrandissement à taille originale
img_pixel = cv2.resize(img_small, (w, h), interpolation=cv2.INTER_NEAREST)

plt.figure()
plt.imshow(img_pixel, cmap='gray')
plt.title("Image pixelisée")
plt.axis('off')
plt.show()

# ============================================================
# FIN TP3
# ============================================================ 