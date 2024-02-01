from domain.studenti import Studenti


class ServiceStudenti:

    def __init__(self, repo_studenti, validator_student):
        self.__repo_studenti = repo_studenti
        self.__validator_student = validator_student

    def size(self):
        """
        reda lungimea listei de studenti
        :return:
        """
        return len(self.__repo_studenti)

    def adauga_student_service(self, id_student, nume, grup):
        """
        adauga un student cu id, nume si grup dupa ce apeleaza functia de validare pentru a verifica daca este valida
        :param id_student: int
        :param nume: string
        :param grup: int
        :return:
        """
        student = Studenti(id_student, nume, grup)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.adauga_student_repo(student)

    def cauta_student_dupa_id_service(self, id_student):
        """
        cauta un anumit student in functie de id
        :param id_student: int
        :return:
        """
        return self.__repo_studenti.cauta_student_dupa_id_repo(id_student)

    def modifica_student_service(self, id_student, nume, grup):
        """
        actuallizeaza un student cu id-ul, numele si grupa introduse de utilizator daca acestea sun valide pentru
        modificare
        :param id_student:
        :param nume:
        :param grup:
        :return:
        """
        student = Studenti(id_student, nume, grup)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.modifica_student_repo(student)

    def sterge_student_dupa_id_service(self, id_student):
        """
        sterge un student din lista daca id-ul introdus de utilizator este valid
        :param id_student:
        :return:
        """
        self.__repo_studenti.sterge_student_dupa_id_repo(id_student)

    def get_all_studenti_service(self):
        """
        afiseaza intreaga lista de studenti
        :return:
        """
        return self.__repo_studenti.get_all_studenti_repo()
