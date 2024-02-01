class Note:
    """
        este un tip de data abstract responsabil cu legatura dintre studenti si probleme.txt
    """

    def __init__(self, id_nota, student, problema, nota):
        """
        creeaza o nota cu parametrii:
        :param id_nota: int, id unic
        :param student: Student, studentul asignat problemei
        :param problema: Problema, problema asignata studentului
        """
        self.__id_nota = id_nota
        self.__student = student
        self.__problema = problema
        self.__nota = nota

    def __eq__(self, other):
        """
        verifica daca doua nota au acelasi id
        :param other:
        :return:
        """
        return self.get_id_nota() == other.get_id_nota()

    def __str__(self):
        """
        returneaza obiectul sub forma unui string
        :return:
        """
        return f"{self.get_id_nota()}, {self.get_student()}, {self.get_problema()}, {self.get_nota()}"

    def get_id_nota(self):
        """
        reda id-ul notei
        :return:
        """
        return self.__id_nota

    def get_student(self):
        """
        returneaza id-ul unui student
        :return:
        """
        return self.__student

    def get_problema(self):
        """
        returneaza nrLab_nrProblema al problemei
        :return:
        """
        return self.__problema

    def get_nota(self):
        """
        returneaza nota
        :return:
        """
        return self.__nota
