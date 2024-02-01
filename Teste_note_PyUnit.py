import unittest

from bussiness.ServiceNota import ServiceNote
from domain.note import Note
from domain.probleme import Probleme
from domain.studenti import Studenti
from erori.exceptii import ValidationError, RepoError
from infrastructura.RepositoryNote import RepoNote
from infrastructura.RepositoryProbleme import RepoProbleme
from infrastructura.RepositoryStudenti import RepoStudenti
from validari.ValidariNote import ValidatorNote


class TesteNotedomain(unittest.TestCase):
    def setUp(self):
        self.__id_nota = 2200
        self.__student = Studenti(2022, "Moldovan Diana", 214)
        self.__problema = Probleme("07_08", "adauga", "28/09/2022")
        self.__notare = 7
        self.__nota = Note(self.__id_nota, self.__student, self.__problema, self.__notare)
        self.__student_nou = Studenti(3033, "Bosinceanu Raul", 211)
        self.__problema_noua = Probleme("05_12", "sterge", "19/10/2022")
        self.__notare_noua = 8
        self.__nota_acelasi_id = Note(self.__id_nota, self.__student_nou, self.__problema_noua, self.__notare_noua)

    def tearDown(self):
        pass

    def test_get_note(self):
        self.assertTrue(self.__nota.get_id_nota() == self.__id_nota)
        self.assertTrue(self.__nota.get_student() == self.__student)
        self.assertTrue(self.__nota.get_problema() == self.__problema)

    def test_eq_note(self):
        self.assertTrue(self.__nota == self.__nota_acelasi_id)

    def test_str_note(self):
        self.assertTrue(self.__nota.__str__() == "2200, 2022, Moldovan Diana, 214, 07_08, adauga, 28/09/2022, 7")


class TesteValidatorNote(unittest.TestCase):
    def setUp(self):
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

    def tearDown(self):
        pass

    def test_validator_note(self):
        self.__validator_note = ValidatorNote()
        self.__validator_note.valideaza(self.__nota)
        try:
            self.assertFalse(self.__validator_note.valideaza(self.__nota_invalida))
        except ValidationError as ve:
            self.assertTrue(str(ve) == 'Id nota invalid')


class TesteRepoNote(unittest.TestCase):
    def setUp(self):
        self.__repo_nota = RepoNote()
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
        self.__repo_nota.adauga_nota_repo(self.__nota)

    def tearDown(self):
        pass

    def test_adaugare_nota(self):
        self.assertTrue(self.__repo_nota.__len__() == 1)
        try:
            self.assertFalse(self.__repo_nota.adauga_nota_repo(self.__nota_acelasi_id))
        except RepoError as re:
            self.assertTrue(str(re) == 'nota existenta!')

    def test_modifica_nota(self):
        self.__repo_nota.modifica_nota_repo(self.__nota_acelasi_id)
        nota_cautata = self.__repo_nota.cauta_nota_dupa_id_repo(self.__id_nota)
        self.assertTrue(nota_cautata.get_student() == self.__student_nou)
        self.assertTrue(nota_cautata.get_problema() == self.__problema_noua)

    def test_ruleaza_teste_cauta_nota(self):
        nota_cautata = self.__repo_nota.cauta_nota_dupa_id_repo(self.__id_nota)
        self.assertTrue(nota_cautata.get_student().get_id_student() == self.__student.get_id_student())
        try:
            self.assertFalse(self.__repo_nota.cauta_nota_dupa_id_repo(2333))
        except RepoError as re:
            self.assertTrue(str(re) == "nota inexistenta!")

    def test_sterge_nota(self):
        assert (self.__repo_nota.__len__() == 1)
        self.__repo_nota.sterge_nota_dupa_id_repo(self.__id_nota)
        self.assertTrue(self.__repo_nota.__len__() == 0)
        try:
            self.assertFalse(self.__repo_nota.sterge_nota_dupa_id_repo(self.__id_nota))
        except RepoError as re:
            self.assertTrue(str(re) == 'nota inexistenta!')


class TesteServiceNote(unittest.TestCase):
    def setUp(self):
        self.__repo_studenti = RepoStudenti()
        self.__repo_probleme = RepoProbleme()
        self.__repo_nota = RepoNote()
        self.__validator_note = ValidatorNote()
        self.__service_note = ServiceNote(self.__repo_nota, self.__repo_studenti,
                                          self.__repo_probleme, self.__validator_note)
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
        self.__repo_studenti.adauga_problema_repo(self.__student)
        self.__repo_probleme.adauga_problema_repo(self.__problema)
        self.__service_note.adauga_nota_service(self.__id_nota, self.__student.get_id_student(),
                                                self.__problema.get_nrLab_nrProblema(), self.__notare)

    def tearDown(self):
        pass

    def test_stergere_student_service(self):
        try:
            self.assertFalse(self.__service_note.sterge_student_dupa_id_service(1222))
        except RepoError as re:
            self.assertTrue(str(re) == "student inexistent!")

    def test_stergere_problema_service(self):
        try:
            self.assertFalse(self.__service_note.sterge_problema_dupa_nrLab_nrProblema_service(9000))
        except RepoError as re:
            self.assertTrue(str(re) == "problema inexistenta!")

    def test_adaugare_nota_service(self):
        self.assertTrue(self.__service_note.size() == 1)
        try:
            self.assertFalse(self.__service_note.adauga_nota_service(self.__id_nota_invalid,
                                                                     self.__student.get_id_student(),
                                                                     self.__problema.get_nrLab_nrProblema(),
                                                                     self.__notare_invalida))
        except ValidationError as ve:
            self.assertTrue(str(ve) == 'Id nota invalid')

    def test_modifica_nota_service(self):
        self.__repo_studenti.adauga_problema_repo(self.__student_nou)
        self.__repo_probleme.adauga_problema_repo(self.__problema_noua)
        self.__service_note.modifica_nota_service(self.__id_nota, self.__student_nou.get_id_student(),
                                                  self.__problema_noua.get_nrLab_nrProblema(), self.__notare)
        nota_cautata = self.__service_note.cauta_nota_dupa_id_service(
            self.__nota.get_id_nota())
        self.assertTrue(nota_cautata == self.__nota)

    def test_cauta_nota_dupa_id_service(self):
        nota_cautata = self.__service_note.cauta_nota_dupa_id_service(self.__id_nota)
        self.assertTrue(nota_cautata == self.__nota)
        try:
            self.assertFalse(self.__service_note.cauta_nota_dupa_id_service(4566))
        except RepoError as re:
            self.assertTrue(str(re) == "nota inexistenta!")

    def test_sterge_nota_dupa_id_service(self):
        self.__service_note.sterge_nota_dupa_id_service(self.__id_nota)
        self.assertTrue(self.__service_note.size() == 0)
        try:
            self.assertFalse(self.__service_note.sterge_nota_dupa_id_service(4556))
        except RepoError as re:
            self.assertTrue(str(re) == "nota inexistenta!")
