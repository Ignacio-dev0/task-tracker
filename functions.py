from datetime import datetime
import json


def add(description):
    # Obtener la fecha y hora actual en formato ISO 8601
    varDir = 'contador.txt'
    with open(varDir, 'r') as archivo:
        id = archivo.read()
        # var = var.split('\n')
        # var = var[0]

    fecha_hora_actual = datetime.now().isoformat()  
    # Crear una nueva tarea
    task = {
        "id": id,
        "description": description,
        "status": "todo",
        "createdAt": fecha_hora_actual,
        "updateAt": fecha_hora_actual,
    }
    print("Task Id is: ", id)
    # Escribir la lista actualizada de vuelta al archivo JSON
    with open(varDir, 'w') as archivo:
        archivo.write(str(int(id) + 1))


    source = 'task.json'

    # Leer el contenido existente del archivo JSON
    try:
        with open(source, 'r') as archivo:
            tasks = json.load(archivo)
    except FileNotFoundError:
        tasks = []
    
    # Agregar la nueva tarea a la lista
    tasks.append(task)
    
    # Escribir la lista actualizada de vuelta al archivo JSON
    with open(source, 'w') as archivo:
        json.dump(tasks, archivo, indent=4)
    
    print("Task added successfully")

def listar():
    source = 'task.json'
    # Leer el contenido existente del archivo JSON
    try:
        with open(source, 'r') as archivo:
            tasks = json.load(archivo)
    except FileNotFoundError:
        tasks = []
    print(f"{'Id':<2} - {'Description':<15} - {'Status'} - {'Created At':<26} - {'Updated At'}")
    # Mostrar la lista de tareas
    for task in tasks:
        print(f"{task['id']:<2} - {task['description']:<15} - {task['status']:<6} - {task['createdAt']} - {task['updateAt']}")

def update(id,description):
    source = 'task.json'

    # Leer el contenido existente del archivo JSON
    try:
        with open(source, 'r') as archivo:
            tasks = json.load(archivo)
    except FileNotFoundError:
        tasks = []

    # Buscar la tarea con el ID especificado
    for task in tasks:
        if task['id'] == id:
            # Actualizar la descripción de la tarea
            task['description'] = description
            # Actualizar la fecha y hora de la tarea
            task['updateAt'] = datetime.now().isoformat()
            
            # Escribir la lista actualizada de vuelta al archivo JSON
            with open(source, 'w') as archivo:
                json.dump(tasks, archivo, indent=4)

            return print("Task updated successfully")  
    print(f"Task with ID {id} not found")
