import unittest

from bussiness.ServiceProbleme import ServiceProbleme
from domain.probleme import Probleme
from erori.exceptii import RepoError, ValidationError
from infrastructura.file_repo_probleme import FileRepoProbleme
from validari.ValidariProbleme import ValidatorProblema


class TestProblemeDomain(unittest.TestCase):

    def setUp(self):
        self.__nrLab_nrProblema = "12_08"
        self.__descriere = "adauga"
        self.__deadline = "02/11/2012"
        self.__problema = Probleme(self.__nrLab_nrProblema, self.__descriere, self.__deadline)

    def tearDown(self):
        pass

    def test_init_problema(self):
        self.assertEqual(self.__problema.get_nrLab_nrProblema(), "12_08")
        self.assertEqual(self.__problema.get_descriere(), "adauga")
        self.assertEqual(self.__problema.get_deadline(), "02/11/2012")

    def test_set_problema(self):
        self.__problema.set_descriere("sterge")
        self.__problema.set_deadline("12/12/2012")
        self.assertEqual(self.__problema.get_descriere(), "sterge")
        self.assertEqual(self.__problema.get_deadline(), "12/12/2012")

    def test_equ_problema(self):
        problema_acelasi_id = Probleme("12_08", "adauga", "02/11/2022")
        self.assertEqual(self.__problema, problema_acelasi_id)

    def test_str_problema(self):
        self.assertEqual(self.__problema.__str__(), "12_08, adauga, 02/11/2012")


class TestProblemaValidator(unittest.TestCase):

    def setUp(self):
        self.__nrLab_nrProblema = "8_2"
        self.__descriere = "fa o clasa"
        self.__deadline = "27/11/2022"
        self.__problema = Probleme(self.__nrLab_nrProblema, self.__descriere, self.__deadline)
        self.__nrLab_nrProblema_invalid = ""
        self.__descriere_invalida = ""
        self.__deadline_invalid = "22"
        self.__problema_invalida = Probleme(self.__nrLab_nrProblema_invalid, self.__descriere_invalida,
                                            self.__deadline_invalid)
        self.__validator = ValidatorProblema()

    def tearDown(self):
        pass

    def test_validator_problema_white_box(self):
        self.__validator.valideaza(self.__problema)
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('', 'aaaa', '12/12/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "nrLab_nrProblema invalid!\n")
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('12_12', '', '12/12/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "descriere invalida!\n")
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('12_12', 'aaaa', '32/12/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "deadline invalid!\n")
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('12_12', 'aaaa', '0/12/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "deadline invalid!\n")
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('12_12', 'aaaa', '12/16/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "deadline invalid!\n")
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('12_12', 'aaaa', '12/0/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "deadline invalid!\n")
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('12_12', 'aaaa', '32/12/20120')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "deadline invalid!\n")

    def test_validator_problema_black_box(self):
        self.__validator.valideaza(self.__problema)
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('', 'aaaa', '12/12/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "nrLab_nrProblema invalid!\n")
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('12_12', '', '12/12/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "descriere invalida!\n")
        try:
            self.assertFalse(self.__validator.valideaza(Probleme('12_12', 'aaaa', '32/12/2020')))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "deadline invalid!\n")


class TesteProblemaFileRepo(unittest.TestCase):

    def setUp(self):
        self.__cale_test_file = 'C:\\Users\\user\\PycharmProjects\\tema_laborator_7-9\\teste\\Teste_probleme'
        self.__repo_probleme = FileRepoProbleme(self.__cale_test_file)
        self.__goleste_fisier(self.__cale_test_file)
        self.__nrLab_nrProblema = "12_08"
        self.__descriere = "adauga"
        self.__deadline = "12/12/2012"
        self.__problema = Probleme(self.__nrLab_nrProblema, self.__descriere, self.__deadline)
        self.__nrLab_nrProblema_inexistent = ""
        self.__descriere_noua = ""
        self.__deadline_nou = "12"
        self.__problema_modificata = Probleme(self.__nrLab_nrProblema, self.__descriere_noua, self.__deadline_nou)
        self.__problema_inexistenta = Probleme(self.__nrLab_nrProblema_inexistent, None, None)
        self.__repo_probleme.adauga_problema_repo(self.__problema)

    def tearDown(self):
        pass

    def __goleste_fisier(self, calea):
        with open(calea, "w") as f:
            pass

    def test_adauga(self):
        self.assertTrue(self.__repo_probleme.size() == 1)
        try:
            self.assertFalse(self.__repo_probleme.adauga_problema_repo(self.__problema))
        except RepoError as re:
            self.assertTrue(str(re) == "problema existenta!")

    def test_cauta(self):
        problema_gasita = self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
        self.assertTrue(problema_gasita.get_descriere() == self.__problema.get_descriere())
        try:
            self.assertFalse(self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(
                self.__nrLab_nrProblema_inexistent))
        except RepoError as re:
            self.assertTrue(str(re) == "problema inexistenta!")

    def test_modifica(self):
        self.__repo_probleme.modifica_problema_repo(self.__problema_modificata)
        self.assertTrue(len(self.__repo_probleme) == 1)
        problema_gasita = self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
        self.assertTrue(problema_gasita.get_descriere() == self.__descriere_noua)
        try:
            self.assertFalse(self.__repo_probleme.modifica_problema_repo(self.__problema_inexistenta))
        except RepoError as re:
            self.assertTrue(str(re) == "problema inexistenta!")

    def test_sterge(self):
        self.__repo_probleme.sterge_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema)
        self.assertTrue(len(self.__repo_probleme) == 0)
        try:
            self.assertFalse(self.__repo_probleme.sterge_problema_dupa_nrLab_nrProblema_repo(self.__nrLab_nrProblema))
        except RepoError as re:
            self.assertTrue(str(re) == "problema inexistenta!")


class TesteProblemeService(unittest.TestCase):
    def setUp(self):
        self.__cale_test_file = 'C:\\Users\\user\\PycharmProjects\\tema_laborator_7-9\\teste\\Teste_studenti'
        self.__repo_probleme = FileRepoProbleme(self.__cale_test_file)
        self.__goleste_fisier(self.__cale_test_file)
        self.__validator_problema = ValidatorProblema()
        self.__service_probleme = ServiceProbleme(self.__repo_probleme, self.__validator_problema)
        self.__nrLab_nrProblema = "12_08"
        self.__descriere = "adauga"
        self.__deadline = "12/12/2012"
        self.__problema = Probleme(self.__nrLab_nrProblema, self.__descriere, self.__deadline)
        self.__nrLab_nrProblema_invalid = ""
        self.__descriere_invalida = ""
        self.__deadline_invalid = "14/22/2003"
        self.__service_probleme.adauga_problema_service(self.__nrLab_nrProblema, self.__descriere, self.__deadline)

    def tearDown(self):
        pass

    def __goleste_fisier(self, calea):
        with open(calea, "w") as f:
            pass

    def test_adauga(self):
        self.assertTrue(self.__service_probleme.size() == 1)
        try:
            self.assertFalse(self.__service_probleme.adauga_problema_service(self.__nrLab_nrProblema, '343',
                                                                             "22/12/2022"))
        except RepoError as re:
            self.assertTrue(str(re) == "problema existenta!")
        try:
            self.assertFalse(self.__service_probleme.adauga_problema_service(self.__nrLab_nrProblema_invalid,
                                                                             self.__descriere_invalida,
                                                                             self.__deadline_invalid))
        except ValidationError as ve:
            self.assertFalse(str(ve) == "nrLab_nrProblema invalid!\ndescriere invalida!\ndeadline invalid!\n")

    def test_cauta(self):
        problema_gasita = self.__service_probleme.cauta_problema_dupa_nrLab_nrProblema_service(self.__nrLab_nrProblema)
        self.assertTrue(problema_gasita.get_descriere() == self.__descriere)
        try:
            self.assertFalse(self.__service_probleme.cauta_problema_dupa_nrLab_nrProblema_service(1234))
        except RepoError as re:
            self.assertTrue(str(re) == "problema inexistenta!")

    def test_modifica(self):
        try:
            self.assertFalse(self.__service_probleme.modifica_problema_service("", None, "22/12/2011"))
        except RepoError as re:
            self.assertTrue(str(re) == "problema inexistenta!")
        self.__service_probleme.modifica_problema_service(self.__nrLab_nrProblema, 'aa', "22/12/2022")
        problema_gasita = self.__service_probleme.cauta_problema_dupa_nrLab_nrProblema_service(self.__nrLab_nrProblema)
        self.assertTrue(problema_gasita.get_descriere() == 'aa')
