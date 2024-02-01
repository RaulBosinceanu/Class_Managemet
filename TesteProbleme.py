from bussiness.ServiceProbleme import ServiceProbleme
from domain.probleme import Probleme
from erori.exceptii import RepoError, ValidationError
from infrastructura.RepositoryProbleme import RepoProbleme
from validari.ValidariProbleme import ValidatorProblema


class Teste(object):

    def __init__(self):
        self.__nrLab_nrProblema = "8_2"
        self.__descriere = "fa o clasa"
        self.__deadline = "27/11/2022"
        self.__problema = Probleme(self.__nrLab_nrProblema, self.__descriere, self.__deadline)

    def __ruleaza_teste_domeniu(self):
        assert (self.__problema.get_nrLab_nrProblema() == self.__nrLab_nrProblema)
        assert (self.__problema.get_descriere() == self.__descriere)
        assert (self.__problema.get_deadline() == self.__deadline)
        clona_problema = Probleme(self.__nrLab_nrProblema, None, None)
        assert (self.__problema == clona_problema)
        assert (self.__problema.__eq__(clona_problema))
        assert (self.__problema.__str__() == '8_2 fa o clasa 27/11/2022')

    def __ruleaza_teste_validare_problema(self):
        self.__validator_problema = ValidatorProblema()
        self.__validator_problema.valideaza(self.__problema)
        self.__nrLab_nrProblema_invalid = ""
        self.__descriere_invalida = ""
        self.__deadline_invalid = 90
        self.__problema_invalida = Probleme(self.__nrLab_nrProblema_invalid, self.__descriere_invalida,
                                            self.__deadline_invalid)
        try:
            self.__validator_problema.valideaza(self.__problema_invalida)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "problema invalida!\ndescriere invalida!\ndeadline invalid!\n")

    def __ruleaza_teste_repo_probleme(self):
        self.__repo_probleme = RepoProbleme()
        assert (len(self.__repo_probleme) == 0)
        self.__repo_probleme.adauga_problema_repo(self.__problema)
        assert (len(self.__repo_probleme) == 1)
        problema_gasita = self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
        assert (problema_gasita.get_descriere() == self.__problema.get_descriere())
        try:
            self.__repo_probleme.adauga_problema_repo(self.__problema)
            assert False
        except RepoError as re:
            assert (str(re) == "problema existenta!")
        self.__nrLab_nrProblema_inexistent = 12

        try:
            self.__repo_probleme.adauga_problema_repo(self.__nrLab_nrProblema_inexistenta)
            assert False
        except RepoError as re:
            assert(str(re) == "problema inexistenta!")
        self.__descriere_noua = "Mihai"
        self.__deadline_nou = '28/05/2022'
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
            assert(str(re) == "problema inexistenta!")
        self.__alta_problema = Probleme(self.__nrLab_nrProblema_inexistent, self.__descriere_noua, self.__deadline_nou)
        self.__repo_probleme.adauga_problema_repo(self.__alta_problema)
        assert (len(self.__repo_probleme) == 2)
        probleme = self.__repo_probleme.get_all_probleme_repo()
        assert(len(probleme) == 2)
        self.__repo_probleme.sterge_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
        assert (len(self.__repo_probleme) == 1)
        try:
            self.__repo_probleme.sterge_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
            assert False
        except RepoError as re:
            assert (str(re) == "problema inexistenta!")

    def __ruleaza_teste_service_proleme(self):
        self.__repo_probleme = RepoProbleme()
        self.__service_probleme = ServiceProbleme(self.__repo_probleme, self.__validator_problema)
        assert (self.__service_probleme.size() == 0)
        self.__service_probleme.adauga_problema_service(self.__nrLab_nrProblema, self.__descriere, self.__deadline)
        assert (self.__service_probleme.size() == 1)
        problema_gasita = self.__service_probleme.cauta_problema_dupa_nrLab_nrProblema_service(self.__problema)
        assert (problema_gasita.get_descriere() == self.__descriere)
        try:
            self.__service_probleme.adauga_problema_service(self.__nrLab_nrProblema, 'adauga', 28/11/2022)
            assert False
        except RepoError as re:
            assert (str(re) == "problema existenta!")
        self.__nrLab_nrProblema_inexistenta = ""
        try:
            self.__service_probleme.cauta_problema_dupa_nrLab_nrProblema_service(self.__nrLab_nrProblema_inexistenta)
            assert False
        except RepoError as re:
            assert (str(re) == "problema inexistenta!")
        try:
            self.__service_probleme.adauga_problema_service(self.__nrLab_nrProblema_invalid, self.__descriere_invalida,
                                                            self.__deadline_invalid)
            assert False
        except ValidationError as ve:
            assert (str(ve) == "nrLab_nrProblema invalid!\ndescriere invalida!\ndeadline invalid!\n")
        try:
            self.__service_probleme.modifica_problema_service(self.__nrLab_nrProblema_inexistenta, None, '23/05/2022')
            assert False
        except RepoError as re:
            assert (str(re) == "problema inexistenta!")
        self.__deadline_nou = '15/08/2023'
        self.__descriere_noua = 'hfj'
        self.__service_probleme.modifica_problema_service(self.__nrLab_nrProblema, self.__descriere_noua,
                                                          self.__deadline_nou)
        problema_gasita = self.__service_probleme.cauta_problema_dupa_nrLab_nrProblema_service(self.__nrLab_nrProblema)
        assert (problema_gasita.get_descriere() == self.__descriere_noua)
        try:
            self.__service_probleme.sterge_problema_dupa_nrLab_nrProblema_service(self.__nrLab_nrProblema_inexistenta)
            assert False
        except RepoError as re:
            assert (str(re) == "problema inexistenta!")
        self.__service_probleme.sterge_problema_dupa_nrLab_nrProblema_service(self.__nrLab_nrProblema)
        assert (self.__service_probleme.size() == 0)

    def ruleaza_toate_testele(self):
        print("ruleaza teste domeniu")
        self.__ruleaza_teste_domeniu()
        print("teste domeniu rulate cu succes")
        print("ruleaza teste validare problema")
        self.__ruleaza_teste_validare_problema()
        print("teste validare problema rulate cu succes")
        print("ruleaza teste repo probleme.txt")
        self.__ruleaza_teste_repo_probleme()
        print("teste repo probleme.txt rulate cu succes")
        print("ruleaza teste service probleme.txt")
        self.__ruleaza_teste_service_proleme()
        print("teste service probleme.txt rulate cu succes")
