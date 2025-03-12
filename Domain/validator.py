class ValidatorError(Exception):
    pass


class CeaiValidator:
    def validare_ceai(self, ceai):
        erori = ''
        if ceai.pret < 0:
            erori = erori + ' pretul trebuie sa fie un numar pozitiv' # erori = 'pretul trebuie sa fie un numar pozitiv'
        if erori != '':
            raise ValidatorError(erori)
