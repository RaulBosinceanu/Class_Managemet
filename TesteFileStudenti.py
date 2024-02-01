from domain.studenti import Studenti
from erori.exceptii import RepoError
from infrastructura.file_repo_studenti import FileRepoStudenti


class TesteFileStudenti:
    def __init__(self):
        self.__cale_test_file = 'teste/Teste_studenti'
        self.__repo_studenti = FileRepoStudenti(self.__cale_test_file)
        self.__id_student = 2345
        self.__nume = "Raul"
        self.__grup = 211
        self.__student = Studenti(self.__id_student, self.__nume, self.__grup)

    def run_all_tests(self):
        self.__goleste_fisier(self.__cale_test_file)
        self.__run_file_repo_tests()

    def __goleste_fisier(self, calea):
        with open(calea, "w") as f:
            pass

    def __run_file_repo_tests(self):
        assert self.__repo_studenti.size() == 0
        self.__repo_studenti.adauga_student_repo(self.__student)
        assert self.__repo_studenti.size() == 1
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
            assert (str(re) == "student inexistent!")
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
            assert (str(re) == "student inexistent!")
        self.__alt_student = Studenti(self.__id_student_inexistent, self.__nume_nou, self.__grup_nou)
        self.__repo_studenti.adauga_student_repo(self.__alt_student)
        assert (len(self.__repo_studenti) == 2)
        studenti = self.__repo_studenti.get_all_studenti_repo()
        assert (len(studenti) == 2)
        self.__repo_studenti.sterge_student_dupa_id_repo(self.__id_student)
        assert (len(self.__repo_studenti) == 1)
        try:
            self.__repo_studenti.sterge_student_dupa_id_repo(self.__id_student)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
