from Domain.validator import CeaiValidator
from Repository.file_repository import FileRepository
from Service.tea_service import TeaService
from UI.consola import Consola

if __name__ == '__main__':
    validator = CeaiValidator()
    file_name = 'data_ceai'
    repository = FileRepository(file_name)
    service = TeaService(repository, validator)
    consola = Consola(service)
    consola.run_program()
