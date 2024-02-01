from domain.note import Note


class ServiceNote:

    def __init__(self, repo_note, repo_studenti, repo_probleme, validator_nota):
        self.__repo_note = repo_note
        self.__validator_nota = validator_nota
        self.__repo_studenti = repo_studenti
        self.__repo_probleme = repo_probleme

    def size(self):
        """
        reda lungimea listei de note
        :return:
        """
        return len(self.__repo_note)

    def adauga_nota_service(self, id_nota, id_student, id_problema, nota):
        """
        adauga o nota cu id dupa ce apeleaza functia de validare pentru a verifica daca este valida
        :return:
        """
        student = self.__repo_studenti.cauta_student_dupa_id_repo(id_student)
        problema = self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(id_problema)
        nota = Note(id_nota, student, problema, nota)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.adauga_nota_repo(nota)

    def cauta_nota_dupa_id_service(self, id_nota):
        """
        cauta o anumita nota in functie de id
        :param id_nota: int
        :return:
        """
        return self.__repo_note.cauta_nota_dupa_id_repo(id_nota)

    def modifica_nota_service(self, id_nota, id_student, id_problema, nota):
        """
        actuallizeaza o nota dupa id daca id-ul introdus de utilizator este valid
        modificare
        :return:
        """
        student = self.__repo_studenti.cauta_student_dupa_id_repo(id_student)
        problema = self.__repo_probleme.cauta_problema_dupa_nrLab_nrProblema_repo(id_problema)
        nota = Note(id_nota, student, problema, nota)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.modifica_nota_repo(nota)

    def sterge_nota_dupa_id_service(self, id_nota):
        """
        sterge o nota din lista daca id-ul introdus de utilizator este valid
        :param id_nota: int
        :return:
        """
        self.__repo_note.sterge_nota_dupa_id_repo(id_nota)

    def sterge_student_dupa_id_service(self, id_student):
        self.__validator_nota.valideaza_id(id_student)
        self.__repo_studenti.sterge_student_dupa_id_repo(id_student)
        lista = self.__repo_note.get_all_note_repo()
        for nota in lista:
            if nota.get_student().get_id_student() == id_student:
                self.__repo_note.sterge_nota_dupa_id_repo(nota.get_id_nota)

    def sterge_problema_dupa_nrLab_nrProblema_service(self, nrLab_nrProblema):
        self.__validator_nota.valideaza_id(nrLab_nrProblema)
        self.__repo_probleme.sterge_problema_dupa_nrLab_nrProblema_repo(nrLab_nrProblema)
        lista = self.__repo_note.get_all_note_repo()
        for nota in lista:
            if nota.get_problema().get_nrLab_nrProblema() == nrLab_nrProblema:
                self.__repo_note.sterge_tema_dupa_nrLab_nrProblema_repo(nota.get_nrLab_nrProblema)

    def get_all_note_service(self):
        """
        afiseaza intreaga lista de note
        :return:
        """
        return self.__repo_note.get_all_note_repo()

    def lista_de_studenti_pt_o_problema(self, id_problema):
        """
        creeaza o lista cu toate noatele de la problema introdusa si o ordoneaza alfabetic si dupa nota
        :return:
        """
        rez = []
        # self.__validator_nota.valideaza_id(id_problema)
        note = self.__repo_note.get_all_note_repo()
        for nota in note:
            problema = nota.get_problema()
            student = nota.get_student()
            if problema.get_nrLab_nrProblema() == id_problema:
                rez.append([student.get_nume(), nota.get_nota()])
        rez.sort(key=lambda x: x[0])
        rez.sort(key=lambda x: x[1], reverse=True)
        return rez

    def lista_medii_studenti(self):
        rez = []
        studenti = self.__repo_studenti.get_all_studenti_repo()
        note = self.__repo_note.get_all_note_repo()
        for student in studenti:
            suma_note = 0
            numar_note = 0
            for nota in note:
                if nota.get_student() == student:
                    suma_note += nota.get_nota()
                    numar_note += 1
            if numar_note > 0:
                media = suma_note/numar_note
                rez.append([student.get_nume(), media])
        return rez

    def studenti_sub_5(self):
        """
        afiseaza toti studenti care au media laboratoarelo mai mici decat 5
        :return:
        """
        rez = []
        lista_medii = self.lista_medii_studenti()
        for medie in lista_medii:
            if medie[1] < 5:
                rez.append(medie)
        return rez

    def media_frecventa(self):
        """
        afiseaza cea mai frecventa medie
        :return:
        """
        frecventa = {}
        nume_medie = self.lista_medii_studenti()
        for medie in nume_medie:
            med = medie[1]
            if med in frecventa:
                frecventa[med] += 1
            else:
                frecventa[med] = 1
        frecventa_max = 0
        medie_max = 0
        for medie in frecventa:
            if frecventa[medie] > frecventa_max:
                frecventa_max = frecventa[medie]
                medie_max = medie
        return medie_max