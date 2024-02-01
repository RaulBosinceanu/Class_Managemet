from erori.exceptii import ValidationError


class ValidatorStudent(object):

    def valideaza(self, student):
        """
         verifica ca datele introduse ptr id, nume si grup sa fie valide
        :param student: entitatea student
        :return:
        """
        erori = ""
        if student.get_id_student() < 0:
            erori += "id invalid!\n"
        if student.get_nume() == "":
            erori += "nume invalid!\n"
        if (student.get_grup() < 100) or (student.get_grup() > 999):
            erori += "grup invalid!\n"
        if len(erori) > 0:
            raise ValidationError(erori)
