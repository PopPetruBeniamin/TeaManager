import traceback

from Domain.validator import ValidatorError
from Repository.in_memory_repository import RepositoryException


class Consola:
    def __init__(self, service):
        self.service = service
        self.menu = "1. Afisare ceaiuri\n2. Adauga ceai\n3. Sortare dupa tip\nx. exit\n"

    def run_program(self):
        option = input(self.menu) #option = input("Choose option: ")
        while True:
            try:
                if option == '1':
                    self.ui_afisare_ceairui()
                if option == '2':
                    self.ui_adaugare_ceai()
                    print("Adaugare cu succes")
                if option == '3':
                    self.ui_sortare_dupa_tip()
                if option == 'x':
                    break
            except ValueError:
                print("Pretul trebuie sa fie un numar pozitiv")
            except RepositoryException as re:
                print(re)
            except ValidatorError as ve:
                print(ve)
            except Exception as e:
                print("An exception: ", e)
            option = input(self.menu)

    def ui_afisare_ceairui(self): #if option == 1
        print(*self.service.afisare_ceai(), sep='\n')

    def ui_adaugare_ceai(self): #if option == 2
        nume = input("Nume: ")
        tip = input("Tip: ")
        pret = float(input("Pret: "))
        self.service.save_ceai(nume, tip, pret)

    def ui_sortare_dupa_tip(self): # if option == 3
        tip_introdus = input('Srieti un tip: ')
        print(self.service.sortare_tip(tip_introdus), sep='\n')
