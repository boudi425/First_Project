import os
from random import randint
def fasl():
    print("-"*45)
    
def clear_screen():
    os.system("cls")

def Start_of_project(name, project_name, *More_Names):
    print(f"{project_name}")
    if More_Names != None:
        print(f"Made by {name}")
        for i in More_Names:
            print(f"Made by {i}")
    else:
        return None
def Get_random_number(start_number: int, end_number: int):
    return randint(start_number, end_number)