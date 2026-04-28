# 🧠 Evaluación de Modelos en Datos Desbalanceados

## 📊 Caso: Detección de Fraude con Redes Neuronales (MLP)

---

## 📌 Descripción

Este proyecto implementa un caso práctico de **clasificación binaria** para la detección de fraude en transacciones, utilizando un modelo de red neuronal (**MLPClassifier**).

El objetivo principal NO es solo entrenar el modelo, sino **evaluarlo correctamente**, entendiendo por qué métricas como el **accuracy pueden ser engañosas** en datasets desbalanceados.

---

## 🎯 Objetivos de aprendizaje

* Comprender el problema del **desbalanceo de clases**
* Implementar un modelo de clasificación con redes neuronales
* Evaluar modelos con métricas adecuadas:

  * Accuracy
  * Precision
  * Recall (Sensibilidad)
  * F1 Score
* Interpretar una **matriz de confusión**
* Identificar cuándo un modelo es **inútil a pesar de tener alta accuracy**

---

## ⚠️ Problema clave

En este caso:

```text
1000 transacciones
20 fraudes (2%)
```

👉 Dataset **extremadamente desbalanceado**

---

## 🚨 Resultado importante

El modelo obtiene:

```text
Accuracy: 98%
Precision: 0.0
Recall: 0.0
F1: 0.0
```

---

## ❌ Interpretación

Aunque el accuracy es alto:

👉 El modelo **NO detecta ningún fraude**

```text
Predice todo como "no fraude"
```

---

## 📊 Matriz de confusión

```text
[[196   0]
 [  4   0]]
```

|                 | Predicción: No fraude | Predicción: Fraude |
| --------------- | --------------------- | ------------------ |
| Real: No fraude | 196 ✅                 | 0                  |
| Real: Fraude    | 4 ❌                   | 0 ❌                |

---

## 🧠 Conclusión clave

> Un modelo puede tener alta accuracy y ser completamente inútil si no detecta la clase importante.

---

## 🧪 Estructura del código

El ejercicio está organizado por fases:

### 🔹 FASE 1: Generación de datos

* Dataset simulado
* Desbalanceo intencional (2% fraude)

### 🔹 FASE 2: División de datos

* Train/Test split
* Uso de `stratify` para mantener proporciones

### 🔹 FASE 3: Modelo base

* Red neuronal simple (MLPClassifier)

### 🔹 FASE 4: Evaluación

* Accuracy, Precision, Recall, F1
* Matriz de confusión

### 🔹 FASE 5: Comparación de modelos

* Modelo base vs modelo mejorado

---

## ⚙️ Requisitos

Instalar dependencias:

```bash
pip install numpy scikit-learn
```

---

## ▶️ Ejecución

```bash
python main.py
```

O ejecutar en Google Colab.

---

## 📊 Métricas clave

| Métrica   | Qué mide                             |
| --------- | ------------------------------------ |
| Accuracy  | Aciertos totales                     |
| Precision | Qué tan confiables son los positivos |
| Recall    | Qué tantos positivos detecta         |
| F1        | Balance entre precision y recall     |

---

## 🧠 Lecciones aprendidas

* Accuracy **no es suficiente** en datos desbalanceados
* Recall es crítico en problemas como fraude
* F1 Score ayuda a evaluar el equilibrio
* La matriz de confusión es esencial

---

## 🚀 Posibles mejoras

Para resolver el problema:

* Ajustar pesos de clase (`class_weight`)
* Balancear el dataset (oversampling / undersampling)
* Ajustar el umbral de decisión
* Probar otros modelos

---
