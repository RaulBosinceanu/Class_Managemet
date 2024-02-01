from bussiness.ServiceNota import ServiceNote
from domain.note import Note
from domain.probleme import Probleme
from domain.studenti import Studenti
from erori.exceptii import ValidationError, RepoError
from infrastructura.RepositoryProbleme import RepoProbleme
from infrastructura.RepositoryStudenti import RepoStudenti
from infrastructura.RepositoryNote import RepoNote
from validari.ValidariNote import ValidatorNote


class TesteNote:
    def __init__(self):
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

    def ruleaza_toate_testele_note(self):

        print('-----------------------------TESTE NOTE-----------------------------')
        print('ruleaza teste domain note')
        self.__ruleaza_teste_domain_note()
        print('teste domain note trecute cu succes')
        print('ruleaza teste validator nota')
        self.__ruleaza_teste_validator_note()
        print('teste validator nota trecte cu succes')
        print('ruleaza teste repository note')
        self.__ruleaza_teste_repo_note()
        print('teste repository note trecute cu succes')
        print('ruleaza teste service note')
        self.__ruleaza_teste_service_note()
        print('teste service note trecute cu succes')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------TESTE Note-------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def __ruleaza_teste_domain_note(self):
        self.ruleaza_teste_get_note()
        self.ruleaza_teste_eq_note()
        self.ruleaza_teste_str_note()

    def ruleaza_teste_get_note(self):
        assert (self.__nota.get_id_nota() == self.__id_nota)
        assert (self.__nota.get_student() == self.__student)
        assert (self.__nota.get_problema() == self.__problema)

    def ruleaza_teste_eq_note(self):
        assert(self.__nota == self.__nota_acelasi_id)

    def ruleaza_teste_str_note(self):
        assert(self.__nota.__str__() == "2200, 2022, Moldovan Diana, 214, 07_08, adauga, 28/09/2022, 7")

# ----------------------------------------------TESTE VALIDATOR---------------------------------------------------------
    def __ruleaza_teste_validator_note(self):
        self.__validator_note = ValidatorNote()
        self.__validator_note.valideaza(self.__nota)
        try:
            self.__validator_note.valideaza(self.__nota_invalida)
            assert False
        except ValidationError as ve:
            assert(str(ve) == 'Id nota invalid')

# ----------------------------------------------TESTE REPOSITORY--------------------------------------------------------
    def __ruleaza_teste_repo_note(self):
        self.__repo_nota = RepoNote()
        self.ruleaza_teste_adaugare_nota()
        self.ruleaza_teste_modifica_nota()
        self.ruleaza_teste_cauta_nota()
        self.ruleaza_teste_sterge_nota()

    def ruleaza_teste_adaugare_nota(self):
        assert(self.__repo_nota.__len__() == 0)
        self.__repo_nota.adauga_nota_repo(self.__nota)
        assert (self.__repo_nota.__len__() == 1)
        try:
            self.__repo_nota.adauga_nota_repo(self.__nota_acelasi_id)
            assert False
        except RepoError as re:
            assert(str(re) == 'nota existenta!')

    def ruleaza_teste_modifica_nota(self):
        self.__repo_nota.modifica_nota_repo(self.__nota_acelasi_id)
        nota_cautata = self.__repo_nota.cauta_nota_dupa_id_repo(self.__id_nota)
        assert(nota_cautata.get_student() == self.__student_nou)
        assert (nota_cautata.get_problema() == self.__problema_noua)

    def ruleaza_teste_cauta_nota(self):
        nota_cautata = self.__repo_nota.cauta_nota_dupa_id_repo(self.__id_nota)
        assert (nota_cautata.get_student().get_id_student() == self.__student_nou.get_id_student())
        try:
            self.__repo_nota.cauta_nota_dupa_id_repo(2333)
            assert False
        except RepoError as re:
            assert (str(re) == "nota inexistenta!")

    def ruleaza_teste_sterge_nota(self):
        assert(self.__repo_nota.__len__() == 1)
        self.__repo_nota.sterge_nota_dupa_id_repo(self.__id_nota)
        assert(self.__repo_nota.__len__() == 0)
        try:
            self.__repo_nota.sterge_nota_dupa_id_repo(self.__id_nota)
            assert False
        except RepoError as re:
            assert(str(re) == 'nota inexistenta!')

# ----------------------------------------------TESTE SERVICE-----------------------------------------------------------
    def __ruleaza_teste_service_note(self):
        self.__repo_studenti = RepoStudenti()
        self.__repo_probleme = RepoProbleme()
        self.__service_note = ServiceNote(self.__repo_nota, self.__repo_studenti,
                                          self.__repo_probleme, self.__validator_note)
        self.ruleaza_teste_stergere_student_service()
        self.ruleaza_teste_stergere_problema_service()
        self.ruleaza_teste_adaugare_nota_service()
        self.ruleaza_teste_modifica_nota()
        self.ruleaza_teste_cauta_nota_dupa_id_service()
        self.ruleaza_teste_sterge_nota_dupa_id_service()
# ------------------------------------RAPOARTE---------------------------------------------------------------------
        self.__student1 = Studenti(1111, 'Mol Dia', 214)
        self.__student2 = Studenti(2222, 'Mol Dia', 215)
        self.__student3 = Studenti(3333, 'Bos Raul', 217)
        self.__problema1 = Probleme('10_10', 'dfd', '12/12/2020')
        self.__problema2 = Probleme('20_20', 'dfd', '12/02/2020')
        self.__problema3 = Probleme('30_30', 'dfd', '12/12/2020')
        self.__nota1 = Note(1000, self.__student1, self.__problema1, 2)
        self.__nota2 = Note(2000, self.__student1, self.__problema2, 6)
        self.__nota3 = Note(3000, self.__student2, self.__problema3, 4)
        self.__nota4 = Note(4000, self.__student2, self.__problema2, 2)
        self.__nota5 = Note(5000, self.__student3, self.__problema2, 8)
        self.__repo_studenti.adauga_student_repo(self.__student1)
        self.__repo_studenti.adauga_student_repo(self.__student2)
        self.__repo_studenti.adauga_student_repo(self.__student3)
        self.__repo_probleme.adauga_problema_repo(self.__problema1)
        self.__repo_probleme.adauga_problema_repo(self.__problema2)
        self.__repo_probleme.adauga_problema_repo(self.__problema3)
        self.__repo_nota.adauga_nota_repo(self.__nota1)
        self.__repo_nota.adauga_nota_repo(self.__nota2)
        self.__repo_nota.adauga_nota_repo(self.__nota3)
        self.__repo_nota.adauga_nota_repo(self.__nota4)
        self.__repo_nota.adauga_nota_repo(self.__nota5)
        self.ruleaza_teste_lista_de_studenti_pt_o_problema()
        self.ruleaza_teste_studenti_sub_5()


    def ruleaza_teste_stergere_student_service(self):
        try:
            self.__service_note.sterge_student_dupa_id_service(1222)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")

    def ruleaza_teste_stergere_problema_service(self):
        try:
            self.__service_note.sterge_problema_dupa_nrLab_nrProblema_service(9000)
            assert False
        except RepoError as re:
            assert (str(re) == "problema inexistenta!")

    def ruleaza_teste_adaugare_nota_service(self):
        self.__repo_studenti.adauga_student_repo(self.__student)
        self.__repo_probleme.adauga_problema_repo(self.__problema)
        assert(self.__service_note.size() == 0)
        self.__service_note.adauga_nota_service(self.__id_nota, self.__student.get_id_student(),
                                                self.__problema.get_nrLab_nrProblema(), self.__notare)
        assert (self.__service_note.size() == 1)
        try:
            self.__service_note.adauga_nota_service(self.__id_nota_invalid,
                                                    self.__student.get_id_student(),
                                                    self.__problema.get_nrLab_nrProblema(), self.__notare_invalida)
            assert False
        except ValidationError as ve:
            assert (str(ve) == 'Id nota invalid')

    def ruleaza_teste_modifica_nota_service(self):
        self.__repo_studenti.adauga_student_repo(self.__student_nou)
        self.__repo_probleme.adauga_problema_repo(self.__problema_noua)
        self.__service_note.modifica_nota_service(self.__id_nota, self.__student_nou.get_id_student(),
                                                  self.__problema_noua.get_nrLab_nrProblema(), self.__notare)
        nota_cautata = self.__service_note.cauta_nota_dupa_id_service(
            self.__nota.get_id_nota())
        assert(nota_cautata == self.__nota)
        try:
            self.__service_note.modifica_nota_service(self.__id_nota_invalid,
                                                      self.__student_nou.get_id_student(),
                                                      self.__problema_noua.get_nrLab_nrProblema(), self.__notare)
            assert False
        except ValidationError as ve:
            assert(str(ve) == "Id nota invalid!\n")
        try:
            self.__service_note.modifica_nota_service(self.__id_nota_nou,
                                                      self.__student_nou.get_id_student(),
                                                      self.__problema_noua.get_nrLab_nrProblema(), self.__notare_noua)
            assert False
        except RepoError as re:
            assert(str(re) == "Nota inexistenta!\n")

    def ruleaza_teste_cauta_nota_dupa_id_service(self):
        nota_cautata = self.__service_note.cauta_nota_dupa_id_service(
                            self.__nota.get_id_nota())
        assert (nota_cautata == self.__nota)
        try:
            self.__service_note.cauta_nota_dupa_id_service(4566)
            assert False
        except RepoError as re:
            assert(str(re) == "nota inexistenta!")

    def ruleaza_teste_sterge_nota_dupa_id_service(self):
        self.__service_note.sterge_nota_dupa_id_service(self.__id_nota)
        assert(self.__service_note.size() == 0)
        try:
            self.__service_note.sterge_nota_dupa_id_service(4556)
            assert False
        except RepoError as re:
            assert(str(re) == "nota inexistenta!")

    def ruleaza_teste_lista_de_studenti_pt_o_problema(self):
        lista = self.__service_note.lista_de_studenti_pt_o_problema('20_20')
        assert (lista[1] == ['Mol Dia', 6])
        assert (lista[2] == ['Mol Dia', 2])
        assert (lista[0] == ['Bos Raul', 8])


    def ruleaza_teste_studenti_sub_5(self):
        lista = self.__service_note.studenti_sub_5()
        assert (lista[0] == ['Mol Dia', 4])
        assert (lista[1] == ['Mol Dia', 3])
