from domain.probleme import Probleme
from erori.exceptii import RepoError
from infrastructura.file_repo_probleme import FileRepoProbleme


class TesteFileProbleme:
    def __init__(self):
        self.__cale_test_file = 'teste/Teste_probleme'
        self.__repo_probleme = FileRepoProbleme(self.__cale_test_file)
        self.__nrLab_nrProblema = "8_2"
        self.__descriere = "fa o clasa"
        self.__deadline = "27/11/2022"
        self.__problema = Probleme(self.__nrLab_nrProblema, self.__descriere, self.__deadline)

    def run_all_tests(self):
        self.__goleste_fisier(self.__cale_test_file)
        self.__run_file_repo_tests()

    def __goleste_fisier(self, calea):
        with open(calea, "w") as f:
            pass

    def __run_file_repo_tests(self):
        assert self.__repo_probleme.size() == 0
        self.__repo_probleme.adauga_problema_repo(self.__problema)
        assert self.__repo_probleme.size() == 1
        problema_gasita = self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
        assert (problema_gasita.get_descriere() == self.__problema.get_descriere())
        try:
            self.__repo_probleme.adauga_problema_repo(self.__problema)
            assert False
        except RepoError as re:
            assert (str(re) == "problema existenta!")
        self.__nrLab_nrProblema_inexistent = 12

        try:
            self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema_inexistent)
            assert False
        except RepoError as re:
            assert (str(re) == "problema inexistenta!")
        self.__descriere_noua = "Mihai"
        self.__deadline_nou = "28/05/2022"
        self.__problema_modificata = Probleme(self.__nrLab_nrProblema, self.__descriere_noua, self.__deadline_nou)
        self.__repo_probleme.modifica_problema_repo(self.__problema_modificata)
        assert (len(self.__repo_probleme) == 1)
        problema_gasita = self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
        assert (problema_gasita.get_descriere() == self.__descriere_noua)
        self.__problema_inexistenta = Probleme(self.__nrLab_nrProblema_inexistent, None, None)
        try:
            self.__repo_probleme.modifica_problema_repo(self.__problema_inexistenta)
            assert False
        except RepoError as re:
            print(str(re))
            assert (str(re) == "problema inexistenta!")
        self.__alta_problema = Probleme(self.__nrLab_nrProblema_inexistent, self.__descriere_noua, self.__deadline_nou)
        self.__repo_probleme.adauga_problema_repo(self.__alta_problema)
        assert (len(self.__repo_probleme) == 2)
        probleme = self.__repo_probleme.get_all_probleme_repo()
        assert (len(probleme) == 2)
        self.__repo_probleme.sterge_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
        assert (len(self.__repo_probleme) == 1)
        try:
            self.__repo_probleme.sterge_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
            assert False
        except RepoError as re:
            assert (str(re) == "problema inexistenta!")