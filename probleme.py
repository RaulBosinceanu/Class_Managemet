class Probleme:
    """
        este un tip de data abstract
    """

    def __init__(self, nrLab_nrProblema, descriere, deadline):
        """
        creeaza o noua problema cu nrLab_nrProblema, descriere,deadline
        :param nrLab_nrProblema: string
        :param descriere: string
        :param deadline: data
        """
        self.__nrLab_nrProblema = nrLab_nrProblema
        self.__descriere = descriere
        self.__deadline = deadline

    def get_nrLab_nrProblema(self):
        """
        reda numarul laboratolui si numarul problemei
        :return:
        """
        return self.__nrLab_nrProblema

    def get_descriere(self):
        """
        returneaza descrierea unei problemei
        :return:
        """
        return self.__descriere

    def get_deadline(self):
        """
        returneaza data limita la care trebuie predata problema
        :return:
        """
        return self.__deadline

    def set_descriere(self, value):
        """
        modifica descrierea cu stringul value
        :param value:
        :return:
        """
        self.__descriere = value

    def set_deadline(self, value):
        """
        modifica data de predare cu stringul value
        :param value:
        :return:
        """
        self.__deadline = value


    def __str__(self):
        """
        returneaza obiectul sub forma unui string
        :return:
        """
        return f"{self.__nrLab_nrProblema}, {self.__descriere}, {self.__deadline}"

    def __eq__(self, other):
        """
        verifica daca doua obiecte au aceiasi problema
        :param other:
        :return:
        """
        return self.__nrLab_nrProblema == other.__nrLab_nrProblema

