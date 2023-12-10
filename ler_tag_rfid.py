#!/usr/bin/env python3
import subprocess

def is_authorized(id, file_path):
    with open(file_path, 'r') as file:
    for line in file:
            if id.strip() == line.strip():
                return True
    return False

def unlock_door():
  command = """
    curl -iX POST \
      --url 'http://localhost:3001/iot/door001' \
      --data urn:ngsi-ld:Door:001@unlock
    """
  subprocess.run(command, shell=True)

def main():
    id_to_check = input("Por favor, insira o ID do colaborador: ")
    file_path = "autorizados.txt"  

    if is_authorized(id_to_check, file_path):
        unlock_door()
        print("Porta destrancada.")
    else:
        print("Acesso negado.")

if __name__ == "__main__":
    main()