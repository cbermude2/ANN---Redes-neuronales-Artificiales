'''
################################
Estructura del Código
################################
Fase 1: Creación del Dataset: 100 filas con 5 variables de entrada.
Fase 2: Persistencia de Datos: respaldo del Dataset en "datos.csv"
Fase 3: Partición y Normalización: División del Dataset en TRAIN/VAL/TEST para evitar la "Fuga de Información" (Data Leakage).
Fase 4: Construcción y Entrenamiento: Definición de la arquitectura (capas, neuronas y funciones de activación).
Fase 5: Diagnóstico: Visualización de métricas y validación de resultados finales.
'''

# --- (Fase 1: Creación del Dataset) ---

import pandas as pd
import numpy as np

# 1. Configuración de aleatoriedad para que siempre salgan los mismos datos
np.random.seed(42)

# 2. Generación de 100 filas de datos (supera el mínimo de 80 del caso) 
data_size = 100

# Creamos las 5 variables de entrada (X) con rangos realistas 
data = {
    'horas_estudio': np.random.uniform(1, 10, data_size),   # De 1 a 10 horas
    'asistencia': np.random.uniform(0, 10, data_size),      # De 0 a 10 puntos
    'tareas_entregadas': np.random.randint(0, 6, data_size),# De 0 a 5 tareas
    'participacion': np.random.uniform(0, 5, data_size),    # De 0 a 5 puntos
    'examen_parcial': np.random.uniform(0, 10, data_size)   # De 0 a 10 puntos
}

# 3. Creamos el DataFrame (df) de Pandas
df = pd.DataFrame(data)

# 4. Definimos la lógica de la Variable Objetivo (y)
# Esto da coherencia a los datos para que la red pueda aprender un patrón 
# Simulamos que aprueba (1) si la suma ponderada es mayor a 7
#Las entradas: X1=horas_estudio, X2=asistencia, X3=examen_parcial
#Los pesos: W1=0.3, W2=0.2, W3=0.5. Entre todos deben sumar 1
suma_ponderada = (df['horas_estudio'] * 0.3 + 
                  df['asistencia'] * 0.2 + 
                  df['examen_parcial'] * 0.5)
df['aprobado'] = (suma_ponderada > 7).astype(int)


# --- (Fase 2: Persistencia de Datos) ---

# 1. Guardar el DataFrame en un archivo físico .csv
# index=False evita que se guarde una columna extra con los números de fila
df.to_csv('datos.csv', index=False)
print("¡Archivo 'datos.csv' generado con éxito!")

#2. Carga Dataset guardado, usando el archivo físico
#En etapa TRAIN es mejor usar los mismos datos para comparar modelos, o realizar auditorías
df_para_entrenar = pd.read_csv('datos.csv')


# --- (Fase 3: Partición y Normalización) ---
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Separar el  Dataframe (df) en variables de Entrada (X) y Objetivo (y)
# axis=1 -> busca en las COLUMNAS la palabra 'aprobado'. Si fuese axis=0 buscaría en filas
# df.drop() -> suelta la columna 'aprobado' y el resto de columnas se quedan en variable X
# variable y selecciona solo la columna 'aprobado'

X = df.drop('aprobado', axis=1)
y = df['aprobado']

# 2. División 70/15/15
# Separamos train = 70% y el resto en temporal, temp = 30% (test_size=0.3)
# random_state=42 asegura Consistencia: siempre empieza en el mismo punto y genere exactamente la misma división de datos
# si se lo deja libre se usará un número se usará el reloj, entonces cada vez que se ejecute el codigo los datos se dividirán de forma distinta.
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)

# Del ese 30%, dividimos la mitad para Validación y la otra mitad para Prueba (15% cada uno)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 3. Normalización (Escalamiento) 
# "scaler" solo aprende de los datos de entrenamiento para no "hacer trampa" 
scaler = StandardScaler()
X_train_esc = scaler.fit_transform(X_train) # Aprende y transforma
X_val_esc = scaler.transform(X_val)         # Solo transforma con lo aprendido
X_test_esc = scaler.transform(X_test)       # Solo transforma con lo aprendido



# --- (Fase 4: Entrenamiento) ---
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

# 1. DEFINIR LA RED
# Usamos una capa oculta de 16 neuronas, activación ReLU y optimizador adam
#batch_size = auto cuando no se lo especifica. En esta práctica consideramos los  100 registros 
#es decir Entrenamiento por Lote COmpleto (Batch Training) así no se genera "ruido" que provocan los lotes pequeños. 
red_neuronal = MLPClassifier(hidden_layer_sizes=(16,), 
                            activation='relu', 
                            solver='adam', 
                            max_iter=100,      # Equivalente a épocas
                            random_state=42, 
                            verbose=True)     # Muestra el progreso

# 2. ENTRENAR
print("\nIniciando el entrenamiento de la red...")
red_neuronal.fit(X_train_esc, y_train)

# 3. EVIDENCIA VISUAL (Gráfica de Pérdida)
plt.figure(figsize=(8, 5))
plt.plot(red_neuronal.loss_curve_)
plt.title('Curva de Pérdida (Aprendizaje)')
plt.xlabel('Iteraciones (Épocas)')
plt.ylabel('Error (Loss)')
plt.grid(True)
plt.show()

# 4. EVALUAR EN PRUEBA
precision = red_neuronal.score(X_test_esc, y_test)
print(f"\n--- RESULTADOS FINALES ---")
print(f"Precisión en el conjunto de prueba: {precision * 100:.2f}%")

# 5. MOSTRAR 5 PREDICCIONES VS REALES
predicciones = red_neuronal.predict(X_test_esc[:5])
print("\nComparativa de Predicciones:")
print("Predicho | Real")
for p, r in zip(predicciones, y_test[:5]):
    print(f"   {p}     |  {r}")