# Lab5

## Asignatura

Procesamiento Digital de Señales

## Programa

Ingeniería Biomédica – Universidad Militar Nueva Granada

## Práctica de laboratorio

**Lab5**

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

## 2. Efecto de la respiración sobre la actividad cardíaca
La respiración influye directamente en la frecuencia cardíaca mediante un fenómeno llamado:

## 2.1 Arritmia sinusal respiratoria
- Durante la **inspiración**: Disminuye la actividad parasimpática, aumenta la frecuencia cardíaca.
- Durante la **espiración**: Aumenta la actividad parasimpática, disminuye la frecuencia cardíaca

Esto genera variaciones en los intervalos R-R del ECG.

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
Alta HRV → buena adaptación fisiológica
Baja HRV → estrés, fatiga o posibles patologías
