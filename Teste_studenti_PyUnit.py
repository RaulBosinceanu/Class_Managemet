import unittest

from bussiness.ServiceStudenti import ServiceStudenti
from domain.studenti import Studenti
from erori.exceptii import ValidationError, RepoError
from infrastructura.file_repo_studenti import FileRepoStudenti
from validari.ValidariStudenti import ValidatorStudent


class TestStudentDomain(unittest.TestCase):

    def setUp(self):
        self.__id_student = 2345
        self.__nume = "Raul"
        self.__grup = 211
        self.__student = Studenti(self.__id_student, self.__nume, self.__grup)

    def tearDown(self):
        pass

    def test_init_student(self):
        self.assertEqual(self.__student.get_id_student(), 2345)
        self.assertEqual(self.__student.get_nume(), "Raul")
        self.assertEqual(self.__student.get_grup(), 211)

    def test_set_student(self):
        self.__student.set_nume("Diana Moldovan")
        self.__student.set_grup(211)
        self.assertEqual(self.__student.get_nume(), "Diana Moldovan")
        self.assertEqual(self.__student.get_grup(), 211)

    def test_equ_studenti(self):
        student_acelasi_id = Studenti(2345, "Raul", 211)
        self.assertEqual(self.__student, student_acelasi_id)

    def test_str_student(self):
        self.assertEqual(self.__student.__str__(), "2345, Raul, 211")


class TestStudentValidator(unittest.TestCase):

    def setUp(self):
        self.__id_student = 2345
        self.__nume = "Raul"
        self.__grup = 211
        self.__student = Studenti(self.__id_student, self.__nume, self.__grup)
        self.__id_student_invalid = -23
        self.__nume_invalid = ""
        self.__grup_invalid = 90
        self.__student_invalid = Studenti(self.__id_student_invalid, self.__nume_invalid, self.__grup_invalid)

    def tearDown(self):
        pass

    def test_validator_student_black_box(self):
        validator_student = ValidatorStudent()
        self.assertIsNone(validator_student.valideaza(self.__student))
        try:
            self.assertFalse(validator_student.valideaza(self.__student_invalid))
        except ValidationError as ve:
            self.assertEqual(str(ve), "id invalid!\nnume invalid!\ngrup invalid!\n")

    def test_validator_student_white_box(self):
        validator_student = ValidatorStudent()
        self.assertIsNone(validator_student.valideaza(self.__student))
        try:
            self.assertFalse(validator_student.valideaza(Studenti(-124, 'Moldovan Diana', 213)))
        except ValidationError as ve:
            self.assertTrue(str(ve), "id invalid!\n")
        try:
            self.assertFalse(validator_student.valideaza(Studenti(1124, '', 213)))
        except ValidationError as ve:
            self.assertEqual(str(ve), "nume invalid!\n")
        try:
            self.assertFalse(validator_student.valideaza(Studenti(1124, 'Moldovan Diana', 13)))
        except ValidationError as ve:
            self.assertEqual(str(ve), "grup invalid!\n")
        try:
            self.assertFalse(validator_student.valideaza(Studenti(1124, 'Moldovan Diana', 1000)))
        except ValidationError as ve:
            self.assertEqual(str(ve), "grup invalid!\n")
        try:
            self.assertFalse(validator_student.valideaza(Studenti(1124, '', 1000)))
        except ValidationError as ve:
            self.assertEqual(str(ve), "nume invalid!\ngrup invalid!\n")
        try:
            self.assertFalse(validator_student.valideaza(self.__student_invalid))
        except ValidationError as ve:
            self.assertEqual(str(ve), "id invalid!\nnume invalid!\ngrup invalid!\n")


class TesteStudentFileRepo(unittest.TestCase):

    def setUp(self):
        self.__cale_test_file = 'C:\\Users\\user\\PycharmProjects\\tema_laborator_7-9\\teste\\Teste_studenti'
        self.__repo_studenti = FileRepoStudenti(self.__cale_test_file)
        self.__goleste_fisier(self.__cale_test_file)
        self.__id_student = 2345
        self.__nume = "Raul"
        self.__grup = 211
        self.__student = Studenti(self.__id_student, self.__nume, self.__grup)
        self.__id_student_inexistent = 12
        self.__nume_nou = "Mihai"
        self.__grup_nou = 214
        self.__student_modificat = Studenti(self.__id_student, self.__nume_nou, self.__grup_nou)
        self.__student_inexistent = Studenti(self.__id_student_inexistent, None, None)
        self.__repo_studenti.adauga_problema_repo(self.__student)

    def tearDown(self):
        pass

    def __goleste_fisier(self, calea):
        with open(calea, "w") as f:
            pass

    def test_adauga(self):
        self.assertFalse(self.__repo_studenti.size() == 1)
        try:
            self.assertFalse(self.__repo_studenti.adauga_problema_repo(self.__student))
        except RepoError as re:
            self.assertTrue(str(re) == "student existent!")

    def test_cauta(self):
        student_gasit = self.__repo_studenti.cauta_student_dupa_id_repo(self.__id_student)
        self.assertTrue(student_gasit.get_nume() == self.__student.get_nume())
        try:
            self.assertFalse(self.__repo_studenti.cauta_student_dupa_id_repo(self.__id_student_inexistent))
        except RepoError as re:
            self.assertTrue(str(re) == "student inexistent!")

    def test_modifica(self):
        self.__repo_studenti.modifica_student_repo(self.__student_modificat)
        self.assertTrue(len(self.__repo_studenti) == 1)
        student_gasit = self.__repo_studenti.cauta_student_dupa_id_repo(self.__id_student)
        self.assertTrue(student_gasit.get_nume() == self.__nume_nou)
        try:
            self.assertFalse(self.__repo_studenti.modifica_student_repo(self.__student_inexistent))
        except RepoError as re:
            self.assertTrue(str(re) == "student inexistent!")

    def test_sterge(self):
        self.__repo_studenti.sterge_student_dupa_id_repo(self.__id_student)
        self.assertTrue(len(self.__repo_studenti) == 0)
        try:
            self.assertFalse(self.__repo_studenti.sterge_student_dupa_id_repo(self.__id_student))
        except RepoError as re:
            self.assertTrue(str(re) == "student inexistent!")


class TesteStudentiService(unittest.TestCase):
    def setUp(self):
        self.__cale_test_file = 'C:\\Users\\user\\PycharmProjects\\tema_laborator_7-9\\teste\\Teste_studenti'
        self.__repo_studenti = FileRepoStudenti(self.__cale_test_file)
        self.__goleste_fisier(self.__cale_test_file)
        self.__validator_student = ValidatorStudent()
        self.__service_studenti = ServiceStudenti(self.__repo_studenti, self.__validator_student)
        self.__id_student = 2345
        self.__nume = "Raul"
        self.__grup = 211
        self.__student = Studenti(self.__id_student, self.__nume, self.__grup)
        self.__id_student_invalid = -23
        self.__nume_invalid = ""
        self.__grup_invalid = 90
        self.__service_studenti.adauga_student_service(self.__id_student, self.__nume, self.__grup)

    def tearDown(self):
        pass

    def __goleste_fisier(self, calea):
        with open(calea, "w") as f:
            pass

    def test_adauga(self):
        self.assertTrue(self.__service_studenti.size() == 1)
        try:
            self.assertFalse(self.__service_studenti.adauga_student_service(self.__id_student, '343', 123))
        except RepoError as re:
            self.assertTrue(str(re) == "student existent!")
        try:
            self.assertFalse(self.__service_studenti.adauga_student_service(self.__id_student_invalid,
                                                                            self.__nume_invalid, self.__grup_invalid))
        except ValidationError as ve:
            self.assertTrue(str(ve) == "id invalid!\nnume invalid!\ngrup invalid!\n")

    def test_cauta(self):
        student_gasit = self.__service_studenti.cauta_student_dupa_id_service(self.__id_student)
        self.assertTrue(student_gasit.get_nume() == self.__nume)
        try:
            self.assertFalse(self.__service_studenti.cauta_student_dupa_id_service(1234))
        except RepoError as re:
            self.assertTrue(str(re) == "student inexistent!")

    def test_modifica(self):
        try:
            self.assertFalse(self.__service_studenti.modifica_student_service(1234, None, 234))
        except RepoError as re:
            self.assertTrue(str(re) == "student inexistent!")
        self.__service_studenti.modifica_student_service(self.__id_student, 'aa', 213)
        student_gasit = self.__service_studenti.cauta_student_dupa_id_service(self.__id_student)
        self.assertTrue(student_gasit.get_nume() == 'aa')
