"""
Ejercicio: Gestión de Usuarios en Hilos con args y kwargs
Objetivo: Crear una aplicación en Python que gestione la información de varios usuarios mediante hilos. Cada hilo recibirá parámetros específicos sobre un usuario y mostrará información personalizada usando args y kwargs.

Instrucciones:

Define una función procesar_usuario que reciba los siguientes parámetros:

Un ID de usuario (usando args).
Información del usuario como nombre y edad (usando kwargs).
La función debe imprimir el ID del usuario junto con su nombre y edad.
Crea una lista de usuarios con al menos 5 usuarios, donde cada usuario tenga:

Un ID de usuario único.
Un nombre y una edad.
Para cada usuario en la lista, crea un hilo que ejecute la función procesar_usuario y pasa los datos de cada usuario a través de args y kwargs.

Inicia todos los hilos y espera a que terminen antes de imprimir un mensaje final indicando que todos los hilos han finalizado.

Agrega una pausa aleatoria dentro de la función procesar_usuario para simular el tiempo de procesamiento de cada usuario y observar cómo los hilos funcionan de manera concurrente.

Ejemplo de salida esperada:

Usuario ID: 1, Nombre: Ana, Edad: 30
Usuario ID: 2, Nombre: Carlos, Edad: 22
Usuario ID: 3, Nombre: Beatriz, Edad: 27
Usuario ID: 4, Nombre: David, Edad: 35
Usuario ID: 5, Nombre: Elena, Edad: 29
Todos los usuarios han sido procesados.
"""

import threading
import time

def procesar_usuario(id, nombre, edad):
    print(f"Usuario ID: {id}, Nombre: {nombre}, Edad: {edad}")


usuarios = [
    {"id": 1, "nombre": "Ana", "edad": 30},
    {"id": 2, "nombre": "Carlos", "edad": 22},
    {"id": 3, "nombre": "María", "edad": 18},
    {"id": 4, "nombre": "David", "edad": 35},
    {"id": 5, "nombre": "Elena", "edad": 29},
]

hilos = []
contador = 0
for usuario in usuarios:
    hilo = threading.Thread(target=procesar_usuario, args=(usuario["id"],), kwargs={'nombre':usuario["nombre"], 'edad':usuario["edad"]})
    hilos.append(hilo)
    time.sleep(2)
    hilo.start()
    contador = contador + 1

for hilo in hilos:
    hilo.join()

if contador == 5:
    print("Todos los usuarios han sido procesados.")
