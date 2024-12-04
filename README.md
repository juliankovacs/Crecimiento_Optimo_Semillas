# Plant Growth Prediction Using Machine Learning

Este proyecto aplica técnicas de aprendizaje automático para analizar y predecir hitos de crecimiento de plantas basados en diversos factores ambientales y agrícolas. El script utiliza Random Forest para clasificación y generación de datos sintéticos.

---

## Características

- **Codificación Categórica**: Convierte variables categóricas como tipo de suelo, frecuencia de riego y tipo de fertilizante en representaciones numéricas.
- **Balanceo de Datos**: Usa la técnica SMOTE para balancear el conjunto de datos y resolver problemas de desbalance de clases.
- **Entrenamiento del Modelo**: Utiliza un clasificador Random Forest para predecir los hitos de crecimiento de las plantas.
- **Generación de Datos Sintéticos**: Crea muestras de datos sintéticos para pruebas y análisis adicionales.
- **Decodificación Categórica**: Traduce las salidas numéricas a sus etiquetas categóricas originales para una mejor interpretación.
- **Filtrado de Datos**: Segrega las predicciones en diferentes clases para un análisis detallado.

---

## Requisitos Previos

El script requiere las siguientes bibliotecas de Python:
- `pandas`
- `numpy`
- `scikit-learn`
- `imbalanced-learn`

Instálalas usando pip:
```bash
pip install pandas numpy scikit-learn imbalanced-learn
