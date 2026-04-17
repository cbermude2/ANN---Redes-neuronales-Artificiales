# 🧠 Aplicación de Redes Neuronales – Pipeline + MLP (Iris)

---

## 📌 Descripción

Este proyecto implementa un flujo completo de trabajo en redes neuronales utilizando el dataset **Iris**.

Se desarrolla un proceso en dos fases:

1. **Preparación de datos (pipeline mínimo)**
2. **Construcción, entrenamiento y mejora de un modelo MLP**

El objetivo es que el estudiante comprenda el ciclo completo:

```text
Datos → Preparación → Modelo → Evaluación → Mejora
```

---

## 🎯 Objetivos de aprendizaje

* Cargar y explorar un dataset
* Preparar datos para redes neuronales
* Aplicar **one-hot encoding**
* Construir un modelo MLP básico
* Entrenar y evaluar el modelo
* Interpretar resultados (matriz de confusión)
* Mejorar el modelo ajustando su arquitectura

---

## 📊 Dataset

Se utiliza el dataset **Iris**, incluido en `scikit-learn`:

* 150 muestras
* 3 clases (tipos de flores)
* 4 características por muestra

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

O usar Google Colab (recomendado para evitar problemas de instalación).

---

# 🧪 Estructura del código

---

## 🔹 1. Cargar datos

```python
from sklearn.datasets import load_iris
```

* Se carga el dataset
* Se separa en:

  * `X`: características
  * `y`: etiquetas

---

## 🔹 2. Preparar datos

### ✔ División Train/Test

```python
train_test_split(X, y, test_size=0.2)
```

* 80% entrenamiento
* 20% prueba

---

### ✔ One-Hot Encoding

```python
to_categorical(y)
```

Convierte etiquetas:

```text
0 → [1,0,0]
1 → [0,1,0]
2 → [0,0,1]
```

📌 Necesario para clasificación multiclase

---

## 🔹 3. Modelo + Entrenamiento

### ✔ Modelo base (MLP mínimo)

```python
Dense(8, activation='relu')
Dense(3, activation='softmax')
```

* 1 capa oculta
* 3 neuronas de salida (3 clases)

---

### ✔ Compilación

```python
optimizer='adam'
loss='categorical_crossentropy'
metrics=['accuracy']
```

---

### ✔ Entrenamiento

```python
model.fit(..., epochs=20)
```

---

## 🔹 4. Evaluación

### ✔ Accuracy

```python
model.evaluate()
```

---

### ✔ Predicciones

```python
model.predict()
```

---

### ✔ Matriz de confusión

```python
confusion_matrix(y_true, y_pred)
```

Permite analizar:

* Aciertos
* Errores por clase

---

## 🔹 5. Mejora del modelo

Se crea un segundo modelo con mayor capacidad:

```python
Dense(16)
Dense(8)
Dense(3)
```

✔ Más capas → mayor capacidad de aprendizaje

---

### ✔ Comparación final

```text
Accuracy | loss - modelo original
Accuracy | loss - modelo mejorado
```

---

# 📈 Resultados esperados

* Accuracy alto (≈ 90% o más)
* Mejora en el segundo modelo
* Matriz de confusión con pocos errores

---

# ⚠️ Buenas prácticas (muy importante)

* No usar datos de test en entrenamiento
* Aplicar correctamente one-hot encoding
* Verificar dimensiones de los datos
* Ejecutar el código en orden

---

# ❌ Errores comunes

* No convertir etiquetas a categóricas
* Usar función de pérdida incorrecta
* No interpretar la matriz de confusión
* No comparar modelos

---

# 🎓 Actividad sugerida

Modificar el modelo:

```python
Dense(8 → 32)
epochs=20 → 50
```

👉 Analizar cómo cambia el accuracy

---

# 👨‍🏫 Uso académico

Este código está diseñado para:

* Clases prácticas de IA
* Introducción a redes neuronales
* Laboratorios guiados



