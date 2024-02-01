from domain.probleme import Probleme
from infrastructura.RepositoryProbleme import RepoProbleme


class FileRepoProbleme(RepoProbleme):

    def __read_all_from_file(self):
        """
            Deschide fisierul pentru citire cu tot ce era in el inainte de apelare
        :return:
        """
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._probleme.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(", ")
                    nrLab_nrProblema = parts[0]
                    descriere = parts[1]
                    deadline = parts[2]
                    problema = Probleme(nrLab_nrProblema, descriere, deadline)
                    self._probleme[nrLab_nrProblema] = problema

    def __write_all_to_file(self):
        """
            Deschide fisierul pentru scriere
        :return:
        """
        with open(self.__calea_catre_fisier, "w") as f:
            for problema in self._probleme.values():
                f.write(str(problema)+"\n")

    def __init__(self, calea_catre_fisier):
        RepoProbleme.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def adauga_problema_repo(self, problema):
        """
            Deschide fisierul pentru a avea toate problemele anterioare, adauga problema in fisier, si o scrie in fisier
        :param problema:
        :return:
        """
        self.__read_all_from_file()
        RepoProbleme.adauga_problema_repo(self, problema)
        self.__write_all_to_file()

    def modifica_problema_repo(self, problema):
        """
            Deschide fisierul pentru a avea toate problemele anterioare, modifica o problema din fisier, si o scrie in fisier
        :param problema:
        :return:
        """
        self.__read_all_from_file()
        RepoProbleme.modifica_problema_repo(self, problema)
        self.__write_all_to_file()

    def sterge_problema_dupa_nrLab_nrProblema_repo(self, nrLab_nrProblema):
        """
            Deschide fisierul pentru a avea toate problemele anterioare, stere problema din fisier, si o scrie in fisier
        :param nrLab_nrProblema:
        :return:
        """
        self.__read_all_from_file()
        RepoProbleme.sterge_problema_dupa_nrLab_nrProblema_repo(self, nrLab_nrProblema)
        self.__write_all_to_file()

    def get_all_probleme_repo(self):
        """
            Deschide fisierul pentru a avea toate problemele anterioare si le returneaza
        :return:
        """
        self.__read_all_from_file()
        return RepoProbleme.get_all_probleme_repo(self)

    def cauta_problema_dupa_nrLab_nrProblema_repo(self, nrLabnrProblema):
        """
            Deschide fisierul pentru a avea toate problemele anterioare, si cauta o problema dupa id_ul ei
        :param nrLabnrProblema:
        :return:
        """
        self.__read_all_from_file()
        return RepoProbleme.cauta_problema_dupa_nrLab_nrProblema_repo(self, nrLabnrProblema)

    def size(self):
        """
            Deschide fisierul pentru a avea toate problemele anterioare, si reda lungimea dictionarului cu probleme
        :return:
        """
        self.__read_all_from_file()
        return RepoProbleme.size(self)
