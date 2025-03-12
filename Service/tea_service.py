from Domain.entities import Ceai


class TeaService:
    def __init__(self, repository, validator):
        self.repository = repository
        self.validator = validator

    def afisare_ceai(self):
        return self.repository.find_all()

    def save_ceai(self, nume, tip, pret):
        ceai = Ceai(nume, tip, pret)
        self.validator.validare_ceai(ceai)
        self.repository.save(ceai)

    def sortare_tip(self, tip_introdus):
        toate_ceaiuri = self.repository.find_all()
        filtered_list_by_type = [ceai for ceai in toate_ceaiuri if ceai.tip == tip_introdus]
        lista_finala = sorted(filtered_list_by_type, key=self.__sort, reverse=True)
        return lista_finala

    def __sort(self, ceai):
        return ceai.pret