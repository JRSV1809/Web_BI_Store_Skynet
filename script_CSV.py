import csv
from datetime import datetime
import random

# Nombres de productos y sucursales de ejemplo
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
sucursales = ['Sucursal 1', 'Sucursal 2', 'Sucursal 3']

# Genera un rango de fechas de ventas, por ejemplo del 1 al 30 de septiembre de 2024
def generar_fecha():
    return datetime(2024, 9, random.randint(1, 30))

# Genera el CSV de ventas
def generar_csv_ventas(nombre_archivo='ventas_productos.csv', num_registros=100):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Escribir la cabecera del CSV
        writer.writerow(['Fecha', 'Nombre del Producto', 'Cantidad', 'Sucursal'])
        
        # Generar datos de ventas
        for _ in range(num_registros):
            fecha_venta = generar_fecha().strftime('%Y-%m-%d')  # Formatear fecha
            producto = random.choice(productos)
            cantidad = random.randint(1, 100)  # Cantidad aleatoria entre 1 y 100
            sucursal = random.choice(sucursales)
            
            # Escribir fila en el CSV
            writer.writerow([fecha_venta, producto, cantidad, sucursal])

    print(f'Archivo CSV "{nombre_archivo}" generado con éxito.')

# Ejecutar el script para generar el archivo CSV
if __name__ == "__main__":
    generar_csv_ventas(num_registros=200)  # Puedes ajustar el número de registros
