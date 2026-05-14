# Variabilidad de la Frecuencia Cardíaca (HRV) y balance autonómico 

## Asignatura

Procesamiento Digital de Señales

## Programa

Ingeniería Biomédica – Universidad Militar Nueva Granada

## Práctica de laboratorio

**Variabilidad de la Frecuencia Cardíaca (HRV) y balance autonómico**

## Integrantes

Danna Jimena Medina Ríos – Código 5600923
María José Polo Tovar – Código 5600894

---
## Descripción
---
##  Metodología 
---
## Diagrama de Flujo
---
### Parte A — Fundamento teórico

## 1. Sistema nervioso autónomo (simpático y parasimpático)
El sistema nervioso autónomo (SNA) regula funciones involuntarias del cuerpo, incluyendo la actividad cardíaca. Se divide en:

## 1.1 Sistema simpático 
- Se activa en situaciones de estrés o actividad (“lucha o huida”).
- Efectos en el corazón:
Aumenta la frecuencia cardíaca (taquicardia), incrementa la fuerza de contracción, reduce la variabilidad de la frecuencia cardíaca (HRV).
## 1.2 Sistema parasimpático
- Predomina en estados de reposo (“reposo y digestión”).
- Actúa principalmente a través del nervio vago.
- Efectos en el corazón: Disminuye la frecuencia cardíaca, aumenta la variabilidad cardíaca (HRV).

El equilibrio entre ambos sistemas regula el ritmo cardíaco.

---

## 2. Efecto de la respiración sobre la actividad cardíaca
La respiración influye directamente en la frecuencia cardíaca mediante un fenómeno llamado:

## 2.1 Arritmia sinusal respiratoria
- Durante la **inspiración**:
  
  → Disminuye la actividad parasimpática.
  
  → Aumenta la frecuencia cardíaca.
- Durante la **espiración**:
  
  → Aumenta la actividad parasimpática.
  
  → Disminuye la frecuencia cardíaca.

Esto genera variaciones en los intervalos R-R del ECG.

---

## 3. Variabilidad de la Frecuencia Cardíaca (HRV)
La HRV (Heart Rate Variability) es la variación en el tiempo entre latidos consecutivos del corazón.

- Cómo se obtiene
1. Se registra la señal de ECG.
2. Se identifican los picos R.
3. Se calcula el tiempo entre picos consecutivos:
   
   $$
RR_i = t_{i+1} - t_i
$$

- Importancia
  
Indicador del estado del sistema nervioso autónomo.

Alta HRV → buena adaptación fisiológica.

Baja HRV → estrés, fatiga o posibles patologías

---
## 4. Diagrama de Poincaré

Es una herramienta gráfica para analizar la serie de intervalos R-R.

- Cómo se construye
  
Se grafica:

$$
RR_{n+1} \text{ vs } RR_n
$$

- Interpretación
  
Forma de nube elíptica:

Ancha → alta variabilidad (parasimpático dominante)

Estrecha → baja variabilidad (simpático dominante)

- Parámetros importantes
  
   → SD1: eje corto de la elipse: variabilidad a corto plazo (latido a latido), refleja actividad parasimpática.
  
   → SD2: eje largo: variabilidad a largo plazo, refleja actividad simpática + parasimpática.
  
  ---
  ## 5. Plan de acción
  
  <p align="center">
  <img src="mapa.jpeg" width="700">
</p>

<p align="center">
  <em> Plan de acción diagrama de flujo </em>
</p>

---
### Parte A - Adquisición de la señal ECG 
  <p align="center">
  <img src="Esquema.jpeg" width="700">
</p>

<p align="center">
  <em> Esquema colocación de electrodos </em>
</p>

Se selecciona una mujer de 20 años como sujeto de prueba para adquirir la señal electrocardiográfica. La señal ECG se graba durante 4 minutos, de los cuales la participante permanece inmóvil y en silencio total durante los 2 primeros minutos; posteriormente, lee en voz alta un pasaje de un texto seleccionado por el equipo durante los 2 últimos minutos.

La toma de la señal electrocardiográfica se realiza mediante un BITalino y la correcta conexión de los cables. El electrodo con cable de color blanco se ubica en la región subclavicular izquierda, el electrodo con cable de color negro en la región subclavicular derecha y, por último, el electrodo con cable de color rojo en las costillas derechas.

  <p align="center">
  <img src="1.png" width="700">
</p>

<p align="center">
  <em> Señal Original </em>
</p>

Para que la frecuencia de muestreo y los niveles de cuantificación fueran apropiados para el tipo de señal se realizo una frecuencia de muestreo de 1000 Hz.

---

### Parte B - Pre-procesamiento de la señal

<p align="center">
  <img src="2.png" width="700">
</p>

<p align="center">
  <em> Señal Original y Filtrada </em>
</p>

<p align="center">
  <img src="3.png" width="700">
</p>

<p align="center">
  <em> Segmento 1 </em>
</p>
<p align="center">
  <img src="4.png" width="700">
</p>

<p align="center">
  <em> Segmento 2 </em>
</p>

<p align="center">
  <img src="5.png" width="700">
</p>

<p align="center">
  <em> Segmento 1 Picos R-R </em>
</p>
<p align="center">
  <img src="6.png" width="700">
</p>

<p align="center">
  <em> Segmento 2 Picos R-R </em>
</p>

<p align="center">
  <img src="7.png" width="700">
</p>

<p align="center">
  <em> Segmento 1 Nueva Señal </em>
</p>
<p align="center">
  <img src="8.png" width="700">
</p>

<p align="center">
  <em> Segmento 2 Nueva Señal </em>
</p>




----
### Parte B - Análisis de la HRV en el dominio del tiempo 

<p align="center">
  <img src="11.png" width="700">
</p>
<p align="center">
  <em> Datos HRV </em>
</p>

----
### Parte C - Construcción del diagrama de Poincaré 

<p align="center">
  <img src="9.png" width="700">
</p>
<p align="center">
  <em> Segmento 1 Diagrama Poincaré  </em>
</p>
<p align="center">
  <img src="10.png" width="700">
</p>
<p align="center">
  <em> Segmento 1 Diagrama Poincaré </em>
</p>
<p align="center">
  <img src="12.png" width="700">
</p>
<p align="center">
  <em> Datos Poincaré </em>
</p>



