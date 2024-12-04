import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder

# Cargar el archivo CSV
data = pd.read_csv('plant_growth_data.csv', delimiter= ',')

# Análisis exploratorio de los datos (EDA)
print(data.describe())  # Estadísticas básicas

# Ver la distribución de la variable objetivo 'Growth_Milestone'
sns.countplot(x='Growth_Milestone', data=data)
plt.title('Distribución de los hitos de crecimiento')
plt.show()

# Analizar las relaciones entre las variables numéricas y el hito de crecimiento
sns.pairplot(data[['Sunlight_Hours', 'Temperature', 'Humidity', 'Growth_Milestone']], hue='Growth_Milestone')
plt.show()

# Correlación entre variables numéricas
correlation_matrix = data[['Sunlight_Hours', 'Temperature', 'Humidity']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.show()

# Codificar las variables categóricas
encoder = OneHotEncoder()
categorical_columns = ['Soil_Type', 'Water_Frequency', 'Fertilizer_Type']
encoded_categorical = encoder.fit_transform(data[categorical_columns]).toarray()  # Convertir a matriz densa

# Preparar los datos
X = pd.concat([data[['Sunlight_Hours', 'Temperature', 'Humidity']], pd.DataFrame(encoded_categorical)], axis=1)
y = data['Growth_Milestone']

# Asegúrate de que las columnas sean cadenas
X.columns = X.columns.astype(str)

# Identificar condiciones óptimas
optimal_conditions = data[data['Growth_Milestone'] == 1]
print(optimal_conditions.describe())
