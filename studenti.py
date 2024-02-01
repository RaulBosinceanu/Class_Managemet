class Studenti:
    """
        este un tip de data abstract
    """
    def __init__(self, id_student, nume, grup):
        """
        creeaza un nou student cu id, nume si grup
        :param id_student: int
        :param nume: string
        :param grup: int
        """
        self.__id_student = id_student
        self.__nume = nume
        self.__grup = grup

    def get_id_student(self):
        """
        returneaza id-ul unui student
        :return:
        """
        return self.__id_student

    def get_nume(self):
        """
        returneaza numele unui student
        :return:
        """
        return self.__nume

    def get_grup(self):
        """
        returneaza grupa unui student
        :return:
        """
        return self.__grup

    def set_nume(self, value):
        """
        modifica valoarea numelui cu stringul value
        :param value:
        :return:
        """
        self.__nume = value

    def set_grup(self, value):
        """
        modifica valoarea grupei cu init-ul value
        :param value:
        :return:
        """
        self.__grup = value

    def __str__(self):
        """
        returneaza obiectul sub forma unui string
        :return:
        """
        return f"{self.__id_student}, {self.__nume}, {self.__grup}"

    def __eq__(self, other):
        """
        verifica daca doua obiecte au acelasi id
        :param other:
        :return:
        """
        return self.__id_student == other.__id_student
