from erori.exceptii import ValidationError


class ValidatorProblema(object):

    def valideaza(self, problema):
        """
        verifica ca datele introduse pentru numarul labului si al problemei, descrierea si deadline-ul sa fie valide
        :param problema: entitatea problema
        :return:
        """
        erori = ""
        if problema.get_nrLab_nrProblema == "":
            erori += "nrLab_nrProblema invalid!\n"
        if problema.get_descriere == "":
            erori += "descriere invalida!\n"
        parts_deadline = problema.get_deadline().split('/')
        if (len(parts_deadline) != 3) or (len(parts_deadline[0]) != 2) or (len(parts_deadline[1]) != 2) or \
                (len(parts_deadline[2]) != 4) or (int(parts_deadline[0]) < 1) or (int(parts_deadline[0]) > 31) or \
                (int(parts_deadline[1]) < 1) or (int(parts_deadline[1]) > 12):
            erori += "deadline invalid!\n"
        if len(erori) > 0:
            raise ValidationError(erori)
