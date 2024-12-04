import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

# Cargar el archivo CSV
print("Cargando el archivo CSV...")
data = pd.read_csv('plant_growth_data.csv', delimiter=',')

# Codificación de variables categóricas y guardar mapeos
print("Codificando variables categóricas...")
soil_mapping = {cat: code for code, cat in enumerate(data['Soil_Type'].astype('category').cat.categories)}
water_mapping = {cat: code for code, cat in enumerate(data['Water_Frequency'].astype('category').cat.categories)}
fertilizer_mapping = {cat: code for code, cat in enumerate(data['Fertilizer_Type'].astype('category').cat.categories)}

data['Soil_Type'] = data['Soil_Type'].astype('category').cat.codes
data['Water_Frequency'] = data['Water_Frequency'].astype('category').cat.codes
data['Fertilizer_Type'] = data['Fertilizer_Type'].astype('category').cat.codes

# Dividir los datos
print("Dividiendo los datos en conjuntos de entrenamiento y prueba...")
X = data.drop('Growth_Milestone', axis=1)
y = data['Growth_Milestone']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Aplicar SMOTE para balancear las clases en el conjunto de entrenamiento
print("Aplicando SMOTE para balancear las clases en el conjunto de entrenamiento...")
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Entrenar el modelo
print("Entrenando el modelo Random Forest...")
rf_model = RandomForestClassifier(n_estimators=140, random_state=42, class_weight='balanced')
rf_model.fit(X_train_resampled, y_train_resampled)
print("Entrenamiento completado.")

# Generar datos sintéticos
print("Generando datos sintéticos...")
num_new_samples = 20
synthetic_data = pd.DataFrame({
    'Soil_Type': np.random.choice(list(soil_mapping.values()), size=num_new_samples),
    'Sunlight_Hours': np.random.uniform(data['Sunlight_Hours'].min(), data['Sunlight_Hours'].max(), size=num_new_samples),
    'Water_Frequency': np.random.choice(list(water_mapping.values()), size=num_new_samples),
    'Fertilizer_Type': np.random.choice(list(fertilizer_mapping.values()), size=num_new_samples),
    'Temperature': np.random.uniform(data['Temperature'].min(), data['Temperature'].max(), size=num_new_samples),
    'Humidity': np.random.uniform(data['Humidity'].min(), data['Humidity'].max(), size=num_new_samples),
})

# Realizar predicciones con los datos sintéticos
print("Realizando predicciones en los datos sintéticos...")
synthetic_data['Predicted_Growth_Milestone'] = rf_model.predict(synthetic_data)

# Decodificar las variables categóricas
print("Decodificando las variables categóricas...")
reverse_soil_mapping = {v: k for k, v in soil_mapping.items()}
reverse_water_mapping = {v: k for k, v in water_mapping.items()}
reverse_fertilizer_mapping = {v: k for k, v in fertilizer_mapping.items()}

synthetic_data['Soil_Type'] = synthetic_data['Soil_Type'].map(reverse_soil_mapping)
synthetic_data['Water_Frequency'] = synthetic_data['Water_Frequency'].map(reverse_water_mapping)
synthetic_data['Fertilizer_Type'] = synthetic_data['Fertilizer_Type'].map(reverse_fertilizer_mapping)

# Mostrar los resultados
print("Datos sintéticos generados y procesados:")
print(synthetic_data)

# Ajustar la configuración de Pandas para mostrar todas las columnas y filas
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
pd.set_option('display.max_rows', None)     # Mostrar todas las filas
pd.set_option('display.width', None)        # Ajustar el ancho de la consola para la salida
pd.set_option('display.colheader_justify', 'center')  # Centrar los encabezados de las columnas

# Filtrar por clase 0 y clase 1
print("Filtrando datos por clase...")
class_0 = synthetic_data[synthetic_data['Predicted_Growth_Milestone'] == 0]
class_1 = synthetic_data[synthetic_data['Predicted_Growth_Milestone'] == 1]

# Mostrar los datos de ambas clases
print("Clase 0:")
print(class_0)
print("\nClase 1:")
print(class_1)
