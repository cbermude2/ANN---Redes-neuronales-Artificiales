*******************************************************
🧠 ANN - Redes Neuronales Artificiales
Tema 4: Herramientas y entornos para redes neuronales
## Pipeline mínimo y modelo MLP (Prácticas 1 y 2)
*******************************************************


---

## 📌 Descripción

Este repositorio contiene dos prácticas fundamentales para la construcción de modelos de **redes neuronales artificiales**, enfocadas en:

* Preparación de datos (pipeline mínimo)
* Implementación de un modelo MLP
* Entrenamiento y evaluación

Las prácticas están diseñadas para estudiantes con conocimientos básicos de programación en Python.

---

## 🎯 Objetivos de aprendizaje

Al finalizar estas prácticas, el estudiante será capaz de:

* Preparar datos para modelos de Machine Learning
* Aplicar buenas prácticas (train/test split, normalización)
* Construir un modelo de red neuronal simple (MLP)
* Entrenar y evaluar un modelo de clasificación

---

## 🧪 Práctica 1: Pipeline mínimo de datos

### 📋 Descripción

En esta práctica se construye un pipeline básico de procesamiento de datos utilizando el dataset **Iris**.

### 🔧 Actividades

* Cargar el dataset Iris
* Identificar variables de entrada (X) y salida (y)
* Analizar dimensiones con `.shape`
* Dividir datos en entrenamiento y prueba (80/20)
* Normalizar los datos correctamente

### ✅ Resultado esperado

* Datos listos para entrenamiento
* Sin fuga de información (data leakage)

---

## 🧪 Práctica 2: Modelo MLP y entrenamiento

### 📋 Descripción

En esta práctica se implementa un modelo de red neuronal tipo **Perceptrón Multicapa (MLP)**.

### 🔧 Actividades

* Aplicar one-hot encoding a las etiquetas
* Definir modelo con Keras (TensorFlow)
* Configurar:

  * Función de pérdida
  * Optimizador
  * Métrica
* Entrenar el modelo
* Evaluar el desempeño
* Realizar predicciones

### ✅ Resultado esperado

* Modelo entrenado correctamente
* Métrica de accuracy funcional
* Predicciones coherentes



## ⚠️ Consideraciones importantes

* Ejecutar primero la **Práctica 1** antes de la Práctica 2
* No aplicar normalización antes del train/test split
* No usar datos de test durante el entrenamiento
* Verificar dimensiones de los datos

---

## 📊 Dataset utilizado

* Iris Dataset (incluido en `scikit-learn`)
* 150 muestras
* 3 clases
* 4 características

---

