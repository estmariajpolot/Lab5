import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from scipy.signal import find_peaks

#ARCHIVO

archivo = "ANDREA.txt"

with open(archivo, 'r') as f:
    lineas = f.readlines()

for linea in lineas:
    if "sampling rate" in linea:
        encabezado = linea
        break

fs = int(re.search(r'"sampling rate":\s*(\d+)', encabezado).group(1))

print("FRECUENCIA DE MUESTREO")
print(f"fs = {fs} Hz")

# Cargar datos
data = pd.read_csv(
    archivo,
    comment='#',
    sep='\t',
    header=None
)

ecg = data.iloc[:, 5].values

t = np.arange(len(ecg)) / fs

# GRAFICA SEÑAL ORIGINAL

plt.figure(figsize=(15,5))
plt.plot(t, ecg)
plt.title("Señal ECG Original")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()


# KALMAN

# Primeros 50 ms
muestras_50ms = int(0.05 * fs)
inicio = ecg[:muestras_50ms]
# Media y desviación estándar inicial
media_ini = np.mean(inicio)
desv_ini = np.std(inicio)

# Parámetros
R = desv_ini**2
Q = 0.01 * R

# Inicialización
x_est = np.zeros(len(ecg))
P = 0
x_est[0] = media_ini

# FILTRO KALMAN
for k in range(1, len(ecg)):

    # Predicción
    x_pred = x_est[k-1]
    P_pred = P + Q

    # Ganancia Kalman
    K = P_pred / (P_pred + R)

    # Corrección
    x_est[k] = x_pred + K * (ecg[k] - x_pred)

    # Actualizar error
    P = (1 - K) * P_pred


# COMPARACIÓN
plt.figure(figsize=(15,5))
plt.plot(t, ecg, label='ECG Original', alpha=0.6)
plt.plot(t, x_est, label='ECG FiltradO', linewidth=2)
plt.title("Comparación ECG Original vs Filtrado")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()
plt.show()

# DIVIDIR SEÑAL FILTRADA
# Tiempo límite = 2 minutos
tiempo_limite = 2 * 60   # 120 segundos
# Índice correspondiente
indice_2min = int(tiempo_limite * fs)


# SEÑAL 1 0 a 2 min
ecg_2min = x_est[:indice_2min]
t_2min = t[:indice_2min]

# SEÑAL 2 -> desde 2 min hasta el final
ecg_restante = x_est[indice_2min:]
t_restante = t[indice_2min:]

# GRAFICAR PRIMERA PARTE
plt.figure(figsize=(15,5))
plt.plot(t_2min, ecg_2min)
plt.title("ECG - 0 a 2 minutos")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# GRAFICAR SEGUNDA PARTE

plt.figure(figsize=(15,5))
plt.plot(t_restante, ecg_restante)
plt.title("ECG - 2 minutos hasta el final")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# DETECCIÓN DE PICOS R
distancia = int(0.4 * fs)
altura1 = np.mean(ecg_2min) + 0.3*np.std(ecg_2min)
altura2 = np.mean(ecg_restante) + 0.3*np.std(ecg_restante)

# Prominencia
prom1 = 0.2*np.std(ecg_2min)
prom2 = 0.2*np.std(ecg_restante)

# PICOS SEGMENTO 1
picos_1, _ = find_peaks(
    ecg_2min,
    distance=distancia,
    prominence=prom1,
    height=altura1
)

# PICOS SEGMENTO 2
picos_2, _ = find_peaks(
    ecg_restante,
    distance=distancia,
    prominence=prom2,
    height=altura2
)
# GRÁFICA SEGMENTO 1
plt.figure(figsize=(18,5))
plt.plot(t_2min, ecg_2min)
plt.plot(t_2min[picos_1],ecg_2min[picos_1],'ro',markersize=10)
plt.title("Picos R Segmento 1")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# GRÁFICA SEGMENTO 2
plt.figure(figsize=(18,5))
plt.plot(t_restante, ecg_restante)
plt.plot(t_restante[picos_2],ecg_restante[picos_2],'ro',markersize=10)
plt.title("Picos R Segmento 2")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# INTERVALOS R-R
rr_1 = np.diff(picos_1) / fs
rr_2 = np.diff(picos_2) / fs
# TIEMPO PARA LA SEÑAL HRV
t_rr1 = t_2min[picos_1[1:]]
t_rr2 = t_restante[picos_2[1:]]

# GRAFICAR SEÑAL HRV
plt.figure(figsize=(15,5))
plt.plot( t_rr1, rr_1, marker='o')
plt.title("HRV Segmento 1 (0-2 min)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Intervalo R-R [s]")
plt.grid()
plt.show()
plt.figure(figsize=(15,5))

plt.plot(t_rr2,rr_2,marker='o')
plt.title("HRV Segmento 2 (2 min-final)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Intervalo R-R [s]")
plt.grid()
plt.show()

# PARÁMETROS HRV
# Media RR
media_rr1 = np.mean(rr_1)
media_rr2 = np.mean(rr_2)
# Desviación estándar RR
std_rr1 = np.std(rr_1)
std_rr2 = np.std(rr_2)
# FRECUENCIA CARDÍACA PROMEDIO
fc1 = 60 / media_rr1
fc2 = 60 / media_rr2

# RESULTADOS
print("\n=========== HRV DOMINIO DEL TIEMPO ===========")
print("\nSEGMENTO 1 (0-2 min)")
print(f"Media RR = {media_rr1:.4f} s")
print(f"STD RR   = {std_rr1:.4f} s")
print(f"FC media = {fc1:.2f} bpm")

print("\nSEGMENTO 2 (2 min-final)")
print(f"Media RR = {media_rr2:.4f} s")
print(f"STD RR   = {std_rr2:.4f} s")
print(f"FC media = {fc2:.2f} bpm")

# DIAGRAMA DE POINCARÉ
# SEGMENTO 1
rr1_x = rr_1[:-1]
rr1_y = rr_1[1:]

# SEGMENTO 2
rr2_x = rr_2[:-1]
rr2_y = rr_2[1:]

# GRAFICAR POINCARÉ SEGMENTO 1
plt.figure(figsize=(6,6))
plt.scatter(rr1_x, rr1_y)
plt.title("Diagrama de Poincaré - Segmento 1")
plt.xlabel("RR(n) [s]")
plt.ylabel("RR(n+1) [s]")
plt.grid()
plt.axis('equal')
plt.show()

# GRAFICAR POINCARÉ SEGMENTO 2
plt.figure(figsize=(6,6))
plt.scatter(rr2_x, rr2_y)
plt.title("Diagrama de Poincaré - Segmento 2")
plt.xlabel("RR(n) [s]")
plt.ylabel("RR(n+1) [s]")
plt.grid()
plt.axis('equal')
plt.show()

# CÁLCULO SD1 Y SD2

# SEGMENTO 1
sd1_1 = np.std((rr1_y - rr1_x)/np.sqrt(2))
sd2_1 = np.std((rr1_y + rr1_x)/np.sqrt(2))

# SEGMENTO 2
sd1_2 = np.std((rr2_y - rr2_x)/np.sqrt(2))
sd2_2 = np.std((rr2_y + rr2_x)/np.sqrt(2))

# ÍNDICES CSI Y CVI
# CSI = actividad simpática
# CVI = actividad vagal

# SEGMENTO 1
CSI_1 = sd2_1 / sd1_1
CVI_1 = np.log10(sd1_1 * sd2_1)

# SEGMENTO 2
CSI_2 = sd2_2 / sd1_2
CVI_2 = np.log10(sd1_2 * sd2_2)

# RESULTADOS
print("\n=========== DIAGRAMA DE POINCARÉ ===========")
print("\nSEGMENTO 1")
print(f"SD1 = {sd1_1:.4f}")
print(f"SD2 = {sd2_1:.4f}")
print(f"CSI = {CSI_1:.4f}")
print(f"CVI = {CVI_1:.4f}")
print("\nSEGMENTO 2")
print(f"SD1 = {sd1_2:.4f}")
print(f"SD2 = {sd2_2:.4f}")
print(f"CSI = {CSI_2:.4f}")
print(f"CVI = {CVI_2:.4f}")