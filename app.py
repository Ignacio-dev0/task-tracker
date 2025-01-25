from functions import *

print("Hi, Welcome to apllication!!!")


while True:
    
    instruction = input()
    parts = instruction.count(' ') 
    if parts != 0:
        instruction, resto = instruction.split(' ',1)

    if instruction == "add":
        try:
            # Limpiamos las comillas 
            resto = resto.strip('"')
            if resto == "":
                print("You must enter a description")
            else:
                add(resto)
        except NameError:
            print("You must enter a description")
    if instruction == "help":
        print('\nadd "description"')
        print('update <id>, "new_description")')
        print('delete <id>')
        print("list")
        print('list "status"')
        print('mark-in-progress <id>')
        print('mark-done <id>')
    if instruction== "list":
        if parts == 0:
            listar()
        else:
            resto = resto.strip('"')
            listarStatus(resto)
    if instruction == "update":
        try:
            if resto == "":
                print("You must enter a ID and description")
            else:
                id,description = resto.split(' ',1)
                # Limpiamos las comillas 
                description = description.strip('"')

                update(id,description)
        except NameError:
            print("You must enter a valid ID and description")
    if instruction == "delete":
        try:
            if resto == "":
                print("You must enter a ID")
            else:
                delete(resto)
        except NameError:
            print("You must enter a valid ID")
    if instruction == "mark-in-progress":
        try:
            mark_in_progress(resto)
        except NameError:
            print("You must enter a valid ID")
    if instruction == "mark-done":
        try:
            mark_done(resto)
        except NameError:
            print("You must enter a valid ID")