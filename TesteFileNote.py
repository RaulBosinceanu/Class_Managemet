from domain.note import Note
from domain.probleme import Probleme
from domain.studenti import Studenti
from erori.exceptii import RepoError
from infrastructura.file_repo_note import FileRepoNote


class TesteFileNote:
    def __init__(self):
        self.__cale_test_file = 'teste/Teste_note'
        self.__repo_nota = FileRepoNote(self.__cale_test_file)
        self.__id_nota = 2200
        self.__student = Studenti(2022, "Moldovan Diana", 214)
        self.__problema = Probleme("07_08", "adauga", "28/09/2022")
        self.__notare = 7
        self.__nota = Note(self.__id_nota, self.__student, self.__problema, self.__notare)

        self.__id_nota_invalid = 22
        self.__student_invalid = Studenti(-24, 'nfnf', 11)
        self.__problema_invalida = Probleme(-45, 'mdnjf', 12)
        self.__notare_invalida = 15
        self.__nota_invalida = Note(self.__id_nota_invalid, self.__student, self.__problema, self.__notare_invalida)
        self.__id_nota_nou = 1234
        self.__student_nou = Studenti(3033, "Bosinceanu Raul", 211)
        self.__problema_noua = Probleme("05_12", "sterge", "19/10/2022")
        self.__notare_noua = 8
        self.__nota_acelasi_id = Note(self.__id_nota, self.__student_nou, self.__problema_noua, self.__notare_noua)
        self.__nota_noua = Note(self.__id_nota_nou, self.__student_nou, self.__problema_noua, self.__notare_noua)

    def run_all_tests(self):
        self.__goleste_fisier(self.__cale_test_file)
        self.__ruleaza_teste_adaugare_nota()
        self.__ruleaza_teste_modifica_nota()
        self.__ruleaza_teste_cauta_nota()
        self.__ruleaza_teste_sterge_nota()

    def __goleste_fisier(self, calea):
        with open(calea, "w") as f:
            pass

    def __ruleaza_teste_adaugare_nota(self):
        assert self.__repo_nota.__len__() == 0
        self.__repo_nota.adauga_nota_repo(self.__nota)
        assert (self.__repo_nota.__len__() == 1)
        try:
            self.__repo_nota.adauga_nota_repo(self.__nota_acelasi_id)
            assert False
        except RepoError as re:
            assert(str(re) == 'nota existenta!')

    def __ruleaza_teste_modifica_nota(self):
        self.__repo_nota.modifica_nota_repo(self.__nota_acelasi_id)
        nota_cautata = self.__repo_nota.cauta_nota_dupa_id_repo(self.__id_nota)
        assert(nota_cautata.get_student() == self.__student_nou)
        assert (nota_cautata.get_problema() == self.__problema_noua)

    def __ruleaza_teste_cauta_nota(self):
        nota_cautata = self.__repo_nota.cauta_nota_dupa_id_repo(self.__id_nota)
        assert (nota_cautata.get_student().get_id_student() == self.__student_nou.get_id_student())
        try:
            self.__repo_nota.cauta_nota_dupa_id_repo(2333)
            assert False
        except RepoError as re:
            assert (str(re) == "nota inexistenta!")

    def __ruleaza_teste_sterge_nota(self):
        assert(self.__repo_nota.__len__() == 1)
        self.__repo_nota.sterge_nota_dupa_id_repo(self.__id_nota)
        assert(self.__repo_nota.__len__() == 0)
        try:
            self.__repo_nota.sterge_nota_dupa_id_repo(self.__id_nota)
            assert False
        except RepoError as re:
            assert(str(re) == 'nota inexistenta!')
