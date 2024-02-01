from erori.exceptii import ValidationError


class ValidatorNote(object):

    def __init__(self):
        pass
    """
    Clasa responsabila de validarea temei
    """

    def valideaza(self, nota):
        """
        verifica ca datele introduse pentru nota sa fie corecte
        :param nota: entitatea tema
        :return:
        """
        erori = ""
        if len(str(nota.get_id_nota())) != 4:
            erori += "Id nota invalid"
        if nota.get_nota() <= 0 and nota.get_nota > 10:
            erori += "nota invalida!"
        if len(erori) > 0:
            raise ValidationError(erori)

    def valideaza_id(self, id):
        if len(str(id)) != 4:
            raise ValidationError("Id invalid!\n")
