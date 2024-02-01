from domain.studenti import Studenti
from infrastructura.RepositoryStudenti import RepoStudenti


class FileRepoStudenti(RepoStudenti):

    def __read_all_from_file(self):
        """
            Deschide fisierul pentru citire cu tot ce era in el inainte de apelare
        :return:
        """
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(", ")
                    id_student = int(parts[0])
                    nume = parts[1]
                    grup = int(parts[2])
                    student = Studenti(id_student, nume, grup)
                    self._studenti[id_student] = student

    def __write_all_to_file(self):
        """
            Deschide fisierul pentru scriere
        :return:
        """
        with open(self.__calea_catre_fisier, "w") as f:
            for student in self._studenti.values():
                f.write(str(student)+"\n")

    def __init__(self, calea_catre_fisier):
        RepoStudenti.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def adauga_student_repo(self, student):
        """
            Deschide fisierul pentru a avea toti studentii anteriori, adauga studentul in fisier, si o scrie in fisier
        :param student:
        :return:
        """
        self.__read_all_from_file()
        RepoStudenti.adauga_student_repo(self, student)
        self.__write_all_to_file()

    def modifica_student_repo(self, student):
        """
           Deschide fisierul pentru a avea toti studentii anteriori, modifica un student din fisier, si o scrie in fisier
        :param student:
        :return:
        """
        self.__read_all_from_file()
        RepoStudenti.modifica_student_repo(self, student)
        self.__write_all_to_file()

    def sterge_student_dupa_id_repo(self, id_student):
        """
            Deschide fisierul pentru a avea toti studentii anteriori, sterge studentul din fisier, si o scrie in fisier
        :param id_student:
        :return:
        """
        self.__read_all_from_file()
        RepoStudenti.sterge_student_dupa_id_repo(self, id_student)
        self.__write_all_to_file()

    def get_all_studenti_repo(self):
        """
            Deschide fisierul pentru a avea toti studentii anteriori si le returneaza
        :return:
        """
        self.__read_all_from_file()
        return RepoStudenti.get_all_studenti_repo(self)

    def cauta_student_dupa_id_repo(self, id_student):
        """
            Deschide fisierul pentru a avea toti studentii anteriori, si cauta un student dupa id
        :param id_student:
        :return:
        """
        self.__read_all_from_file()
        return RepoStudenti.cauta_student_dupa_id_repo(self, id_student)

    def size(self):
        """
            Deschide fisierul pentru a avea toti studentii anteriori, si reda lungimea dictionarului cu studenti
        :return:
        """
        self.__read_all_from_file()
        return RepoStudenti.size(self)
