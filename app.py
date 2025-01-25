from functions import *

print("Hi, Welcome to apllication!!!")


while True:
    
    instruction = input()
    parts = instruction.count(' ') 
    if parts != 0:
        instruction, resto = instruction.split(' ',1)

    if instruction == "add":
        # Limpiamos las comillas 
        resto = resto.strip('"')
        
        add(resto)
    if instruction == "help":
        print('\nadd "description"')
        print('update <id>, "new_description")')
        print('delete <id>')
        print("list")
        print('list "status"')
        print('mark-in-progress <id>')
        print('mark-done <id>')
    if instruction== "list":
        listar()
    if instruction == "update":
     
        id,description = resto.split(' ',1)
        # Limpiamos las comillas 
        description = description.strip('"')

        update(id,description)
    if instruction == "delete":
        delete(resto)
    if instruction == "mark-in-progress":
        mark_in_progress(resto)
    if instruction == "mark-done":
        mark_done(resto)

    