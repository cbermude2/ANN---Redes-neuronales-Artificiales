# 🧠 Tema 8 — Evaluación del Impacto del Ajuste en Redes Neuronales

## 📊 Caso Práctico: Predicción de Abandono Estudiantil

---

# 📌 Descripción

Este proyecto implementa un caso práctico de Machine Learning utilizando redes neuronales artificiales (**MLPClassifier**) para predecir el riesgo de abandono estudiantil universitario.

El objetivo principal es comprender cómo el ajuste de hiperparámetros y las técnicas de regularización afectan el desempeño de un modelo de inteligencia artificial.

---

# 🎯 Objetivos de Aprendizaje

* Implementar redes neuronales básicas
* Comprender hiperparámetros:

  * Learning Rate
  * Batch Size
  * Epochs
  * Hidden Layers
* Aplicar técnicas de regularización:

  * L2 Regularization
  * Early Stopping
* Evaluar modelos con:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
* Detectar:

  * Sobreajuste (Overfitting)
  * Subajuste (Underfitting)
* Comparar configuraciones de modelos

---

# 🧩 Estructura del Proyecto

El ejercicio está dividido en 5 fases:

| Fase      | Descripción                       |
| --------- | --------------------------------- |
| 🔹 FASE 1 | Generación y preparación de datos |
| 🔹 FASE 2 | Modelo base y entrenamiento       |
| 🔹 FASE 3 | Evaluación del modelo             |
| 🔹 FASE 4 | Análisis del aprendizaje          |
| 🔹 FASE 5 | Mejora y comparación de modelos   |

---

# 📚 Caso de Estudio

Se simula un sistema universitario que intenta predecir si un estudiante abandonará la carrera utilizando variables académicas como:

* Promedio
* Asistencia
* Materias reprobadas
* Uso de plataforma virtual

---

# ⚙️ Tecnologías Utilizadas

* Python
* NumPy
* Pandas
* Scikit-learn
* Matplotlib

---
abrir el notebook en Google Colab.

---

# 🧠 Conceptos Implementados

## 🔹 Hiperparámetros

| Hiperparámetro     | Función                  |
| ------------------ | ------------------------ |
| hidden_layer_sizes | Número de capas/neuronas |
| learning_rate_init | Velocidad de aprendizaje |
| batch_size         | Tamaño de lote           |
| max_iter           | Número de epochs         |

---

## 🔹 Regularización

| Técnica        | Objetivo                              |
| -------------- | ------------------------------------- |
| L2 (alpha)     | Evitar pesos excesivos                |
| Early Stopping | Detener entrenamiento automáticamente |

---

# 📊 Métricas Evaluadas

| Métrica   | Qué mide                         |
| --------- | -------------------------------- |
| Accuracy  | Exactitud total                  |
| Precision | Confiabilidad de positivos       |
| Recall    | Sensibilidad                     |
| F1 Score  | Balance entre precision y recall |

---

# 📈 Curva de Entrenamiento

Se analiza la evolución de la función de pérdida (loss) para identificar:

* aprendizaje correcto
* sobreajuste
* subajuste

---

# 🎯 Resultados Esperados

El estudiante podrá:

✔ comparar modelos
✔ ajustar hiperparámetros
✔ interpretar métricas
✔ detectar sobreajuste
✔ seleccionar el mejor modelo

---

# 🌎 Aplicación en el Mundo Real

Este tipo de modelos puede utilizarse en:

* Predicción de abandono estudiantil
* Detección de fraude
* Diagnóstico médico
* Predicción financiera
* Sistemas de recomendación

---

# 🧠 Conclusión Clave

> Un modelo más complejo no siempre es un mejor modelo.
> Es recomendable modificar una métrica a la vez 
> La selección del modelo debe basarse en métricas adecuadas y capacidad de generalización.

---

# 👨‍🏫 Uso Académico

Proyecto desarrollado para la asignatura:

## Aplicación de Redes Neuronales

Orientado a estudiantes con conocimientos básicos de programación y Machine Learning.

---

# 📄 Licencia
Solo de uso académico
Uso académico y educativo.

