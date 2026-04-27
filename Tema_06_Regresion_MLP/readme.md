# 🧠 Predicción de Precio de Bienes Raíces con Redes Neuronales (MLP)

---

## 📌 Descripción

Este proyecto implementa un flujo completo de aprendizaje automático utilizando redes neuronales artificiales para predecir el **precio de viviendas** a partir de variables simples.

El desarrollo está organizado por **fases**, lo que permite comprender paso a paso el proceso:

```text
Datos → Modelo → Evaluación → Análisis → Mejora
```

---

## 🎯 Objetivos de aprendizaje

* Generar y trabajar con datos simulados
* Preparar datos para redes neuronales
* Implementar un modelo MLP para regresión
* Evaluar el desempeño del modelo
* Analizar errores por rangos
* Mejorar el modelo y comparar resultados

---

## 📊 Variables del modelo

El precio se predice en función de:

* 📐 **m2** → tamaño de la vivienda
* 🛏 **habitaciones** → número de habitaciones
* 🏚 **antigüedad** → años de construcción

---

## ⚙️ Requisitos

Instalar dependencias:

```bash
pip install numpy scikit-learn tensorflow
```

> ✅ Recomendado: Python 3.10 o 3.11

---

## 🚀 Ejecución

```bash
python main.py
```

O ejecutar en Google Colab.

---

# 🧪 Estructura del proyecto

---

## 🔹 FASE 1: Generación de datos

Se simulan datos de viviendas mediante una función:

```text
precio = (m2 * 300) + (habitaciones * 10000) - (antigüedad * 500) + ruido
```

✔ Incluye ruido para simular escenarios reales
✔ Se construye el dataset (X, y)

---

## 🔹 FASE 2: Modelo y entrenamiento

Se implementa un modelo MLP:

* Capa oculta: 16 neuronas (ReLU)
* Capa de salida: 1 neurona (regresión)

Configuración:

* Optimizador: Adam
* Función de pérdida: MSE
* Métrica: MAE

---

## 🔹 FASE 3: Evaluación

Se calculan las métricas:

* **MAE** → error promedio
* **MSE** → error cuadrático
* **RMSE** → error en escala real

---

## 🔹 FASE 4: Análisis de errores

Se analizan errores por rangos de precio:

* Bajo (< 80,000)
* Medio (80,000 – 150,000)
* Alto (> 150,000)

✔ Permite identificar dónde falla el modelo

---

## 🔹 FASE 5: Mejora del modelo

Se crea un modelo más complejo:

* Más neuronas
* Más capas
* Más épocas

Se compara el desempeño:

```text
MAE original vs MAE mejorado
```

---

# 📈 Resultados esperados

* Modelo funcional de regresión
* Cálculo correcto de métricas
* Identificación de errores por rango
* Comparación entre modelos

---

# 🧠 Interpretación de resultados

* Un **MAE menor** indica mejor desempeño
* Si la mejora es muy pequeña → no es significativa
* RMSE alto indica presencia de errores grandes

---

# ⚠️ Buenas prácticas

* No mezclar datos de entrenamiento y prueba
* Escalar los datos correctamente
* Analizar errores, no solo métricas
* Comparar modelos con criterio

---

# ❌ Errores comunes

* No normalizar datos
* Interpretar mal las métricas
* Creer que un modelo más complejo siempre es mejor
* Ignorar el análisis de errores

---

# 🎓 Actividad sugerida

1. Ejecutar el código
2. Registrar métricas (MAE, MSE, RMSE)
3. Analizar errores por rangos
4. Comparar modelos
5. Proponer mejoras

---

# 👨‍🏫 Uso académico

Este proyecto está diseñado para:

* Clases de Redes Neuronales
* Introducción a regresión con MLP
* Laboratorios prácticos guiados

---

# 📌 Autor

Docente: *[Tu nombre]*
Asignatura: Aplicación de Redes Neuronales
Institución: UCSG TEC

---

# 📄 Licencia

Uso académico.

---
