class RepositoryException(Exception):
    pass
class InMemoryRepository:
    def __init__(self):
        self.repository = {}

    def find_all(self):
        return list(self.repository.values()) #[Tea("Expresso", "Black", 12.34), Tea("Latte", "Alb", 12.34)]

    def save(self, ceai): #dictionary.save(Tea)
        if self.find_by_name(ceai) is not None:
            self.repository[ceai.nume] = ceai
        else:
            raise RepositoryException("Numele deja exista") #i wrote this because

    def find_by_name(self, ceai):
        if ceai.nume in self.repository:
            return None
        return ceai


