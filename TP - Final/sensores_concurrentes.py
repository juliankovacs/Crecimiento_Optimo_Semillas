import threading
import time
import random

# Variables globales para almacenar los datos recolectados
temperature_data = []
humidity_data = []

# Lock para sincronizar el acceso a los datos y la consola
data_lock = threading.Lock()

start_time = time.time()

# Función que simula la recolección de datos de un sensor de temperatura
def collect_temperature():
    for _ in range(5):  # Recolectar datos durante 5 segundos
        temp = round(random.uniform(20.0, 30.0), 2)  # Generar un valor de temperatura aleatorio
        with data_lock:  # Bloquear el acceso mientras se escribe y se imprime
            temperature_data.append(temp)
            print(f"Sensor de temperatura: {temp}°C")
        time.sleep(1)

# Función que simula la recolección de datos de un sensor de humedad
def collect_humidity():
    for _ in range(5):  # Recolectar datos durante 5 segundos
        humidity = round(random.uniform(30.0, 60.0), 2)  # Generar un valor de humedad aleatorio
        with data_lock:  # Bloquear el acceso mientras se escribe y se imprime
            humidity_data.append(humidity)
            print(f"Sensor de humedad: {humidity}%")
        time.sleep(1)

# Crear los threads para cada sensor
temperature_thread = threading.Thread(target=collect_temperature)
humidity_thread = threading.Thread(target=collect_humidity)

# Iniciar los threads
temperature_thread.start()
humidity_thread.start()

# Esperar a que ambos threads terminen
temperature_thread.join()
humidity_thread.join()

end_time = time.time()

# Mostrar los datos recolectados
print("\nDatos recolectados:")
print(f"Temperaturas: {temperature_data}")
print(f"Humedad: {humidity_data} ")
print(f"Tiempo total de ejecución: {end_time - start_time} segundos")
