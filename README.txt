*******************************************************
🧠 ANN - Redes Neuronales Artificiales
Tema 3: Entrenamiento básico de redes neuronales (MLP)
*******************************************************

Este repositorio contiene el código base y los insumos para resolver la Práctica 1. 
Objetivo: construir una red neuronal multicapa (MLP) para clasificar el rendimiento estudiantil ("Aprobar/No Aprobar").

🛠️ Requisitos de Instalación
Para ejecutar este proyecto, necesitas tener instalado Python (versión 3.10 a 3.12 recomendada). Abre tu terminal y ejecuta los siguientes comandos en orden:

Pandas: Para la creación del dataset y manipulación de tablas.
   pip install pandas

Scikit-Learn: Para la partición de datos (70/15/15) y la normalización de variables.
   pip install scikit-learn

Matplotlib: Para generar las gráficas de las curvas de pérdida (evidencia de aprendizaje).
   pip install matplotlib

TensorFlow: Para construir y entrenar la red neuronal con Keras.
   pip install tensorflow

⚠️ Nota: Si usas Python 3.14 o superior y TensorFlow presenta errores de compatibilidad, el código activará automáticamente un modo de respaldo con Scikit-Learn.

📈 ¿Cómo interpretar los resultados?
Se mostrará una gráfica de la Curva de Pérdida (Loss Curve):
- Aprendizaje Correcto: La curva de error disminuye constantemente.
- Sobreajuste (Overfitting): El error de entrenamiento baja pero el de validación sube.
- Subajuste (Underfitting): El error se mantiene alto y no mejora con las épocas.