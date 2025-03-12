from Domain.entities import Ceai
from Repository.in_memory_repository import InMemoryRepository


class FileRepository(InMemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.file_name, 'r') as f:
            content = f.readlines()
            for line in content:
                parts = line.split(',') #[first element, second element, third element]
                ceai = Ceai(parts[0], parts[1], float(parts[2]))
                super().save(ceai)

    def save(self, ceai):
        super().save(ceai)
        with open(self.file_name, 'a') as f:
            f.write(f'\n{ceai.nume},{ceai.tip},{ceai.pret}')


