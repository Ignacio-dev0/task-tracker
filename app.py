from functions import add,listar,update

print("Hi, Welcome to apllication!!!")


while True:
    
    instruction = input()
    parts = instruction.count(' ') 
    if parts != 0:
        instruction, resto = instruction.split(' ',1)

    if instruction == "add":
        # Limpiamos las comillas 
        resto = resto.strip('"')
        print(f"Comando: {instruction}")
        print(f"Descripción: {resto}")
        add(resto)
    if instruction == "help":
        print('add "description"')
        print('update <id>, "new_description")')
        print('delete "id"')
        print("list")
        print('list "status"')
        print('mark-in-progress "id"')
        print('mark-done "id"')
    if instruction== "list":
        listar()
    if instruction == "update":
     
        id,description = resto.split(' ',1)
        # Limpiamos las comillas 
        description = description.strip('"')

        update(id,description)
    