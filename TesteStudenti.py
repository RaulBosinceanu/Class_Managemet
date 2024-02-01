from bussiness.ServiceStudenti import ServiceStudenti
from domain.studenti import Studenti
from erori.exceptii import RepoError, ValidationError
from infrastructura.RepositoryStudenti import RepoStudenti
from validari.ValidariStudenti import ValidatorStudent


class Teste(object):

    def __init__(self):
        self.__id_student = 2345
        self.__nume = "Raul"
        self.__grup = 211
        self.__student = Studenti(self.__id_student, self.__nume, self.__grup)

    def __ruleaza_teste_domeniu(self):
        assert (self.__student.get_id_student() == self.__id_student)
        assert (self.__student.get_nume() == self.__nume)
        assert (self.__student.get_grup() == self.__grup)
        clona_student = Studenti(self.__id_student, None, None)
        assert (self.__student == clona_student)
        assert (self.__student.__eq__(clona_student))
        assert (self.__student.__str__() == '2345, Raul, 211')

    def __ruleaza_teste_validare_student(self):
        self.__validator_student = ValidatorStudent()
        self.__validator_student.valideaza(self.__student)
        self.__id_student_invalid = -23
        self.__nume_invalid = ""
        self.__grup_invalid = 90
        self.__student_invalid = Studenti(self.__id_student_invalid, self.__nume_invalid, self.__grup_invalid)
        try:
            self.__validator_student.valideaza(self.__student_invalid)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\ngrup invalid!\n")

    def __ruleaza_teste_repo_studenti(self):
        self.__repo_studenti = RepoStudenti()
        assert (len(self.__repo_studenti) == 0)
        self.__repo_studenti.adauga_student_repo(self.__student)
        assert (len(self.__repo_studenti) == 1)
        student_gasit = self.__repo_studenti.cauta_student_dupa_id_repo(self.__id_student)
        assert (student_gasit.get_nume() == self.__student.get_nume())
        try:
            self.__repo_studenti.adauga_student_repo(self.__student)
            assert False
        except RepoError as re:
            assert (str(re) == "student existent!")
        self.__id_student_inexistent = 12

        try:
            self.__repo_studenti.cauta_student_dupa_id_repo(self.__id_student_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "student inexistent!")
        self.__nume_nou = "Mihai"
        self.__grup_nou = 214
        self.__student_modificat = Studenti(self.__id_student, self.__nume_nou, self.__grup_nou)
        self.__repo_studenti.modifica_student_repo(self.__student_modificat)
        assert (len(self.__repo_studenti) == 1)
        student_gasit = self.__repo_studenti.cauta_student_dupa_id_repo(self.__id_student)
        assert (student_gasit.get_nume() == self.__nume_nou)
        self.__student_inexistent = Studenti(self.__id_student_inexistent, None, None)
        try:
            self.__repo_studenti.modifica_student_repo(self.__student_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "student inexistent!")
        self.__alt_student = Studenti(self.__id_student_inexistent, self.__nume_nou, self.__grup_nou)
        self.__repo_studenti.adauga_student_repo(self.__alt_student)
        assert (len(self.__repo_studenti) == 2)
        studenti = self.__repo_studenti.get_all_studenti_repo()
        assert(len(studenti) == 2)
        self.__repo_studenti.sterge_student_dupa_id_repo(self.__id_student)
        assert (len(self.__repo_studenti) == 1)
        try:
            self.__repo_studenti.sterge_student_dupa_id_repo(self.__id_student)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")

    def __ruleaza_teste_service_studenti(self):
        self.__repo_studenti = RepoStudenti()
        self.__service_studenti = ServiceStudenti(self.__repo_studenti, self.__validator_student)
        assert (self.__service_studenti.size() == 0)
        self.__service_studenti.adauga_student_service(self.__id_student, self.__nume, self.__grup)
        assert (self.__service_studenti.size() == 1)
        student_gasit = self.__service_studenti.cauta_student_dupa_id_service(self.__id_student)
        assert (student_gasit.get_nume() == self.__nume)
        try:
            self.__service_studenti.adauga_student_service(self.__id_student, '343', 123)
            assert False
        except RepoError as re:
            assert (str(re) == "student existent!")
        self.__id_student_inexistent = 12
        try:
            self.__service_studenti.cauta_student_dupa_id_service(self.__id_student_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        try:
            self.__service_studenti.adauga_student_service(self.__id_student_invalid, self.__nume_invalid,
                                                           self.__grup_invalid)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\ngrup invalid!\n")
        try:
            self.__service_studenti.modifica_student_service(self.__id_student_inexistent, None, 234)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        self.__grup_nou = 214
        self.__nume_nou = 'hfj'
        self.__service_studenti.modifica_student_service(self.__id_student, self.__nume_nou, self.__grup_nou)
        student_gasit = self.__service_studenti.cauta_student_dupa_id_service(self.__id_student)
        assert (student_gasit.get_nume() == self.__nume_nou)
        try:
            self.__service_studenti.sterge_student_dupa_id_service(self.__id_student_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        self.__service_studenti.sterge_student_dupa_id_service(self.__id_student)
        assert (self.__service_studenti.size() == 0)

    def ruleaza_toate_testele(self):
        print("ruleaza teste domeniu")
        self.__ruleaza_teste_domeniu()
        print("teste domeniu rulate cu succes")
        print("ruleaza teste validare student")
        self.__ruleaza_teste_validare_student()
        print("teste validare studenti rulate cu succes")
        print("ruleaza teste repo studenti")
        self.__ruleaza_teste_repo_studenti()
        print("teste repo studenti rulate cu succes")
        print("ruleaza teste service studenti")
        self.__ruleaza_teste_service_studenti()
        print("teste service studenti rulate cu succes")
