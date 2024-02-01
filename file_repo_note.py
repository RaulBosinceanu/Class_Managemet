from domain.note import Note
from infrastructura.RepositoryNote import RepoNote


class FileRepoNote(RepoNote):

    def __read_all_from_file(self):
        """
            Deschide fisierul pentru citire cu tot ce era in el inainte de apelare
        :return:
        """
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._note.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(", ")
                    id_nota = int(parts[0])
                    id_student = int(parts[1])
                    nrLab_nrProblema = parts[2]
                    notare = float(parts[3])
                    nota = Note(id_nota, id_student, nrLab_nrProblema, notare)
                    self._note[id_nota] = nota

    def __write_all_to_file(self):
        """
            Deschide fisierul pentru scriere
        :return:
        """
        with open(self.__calea_catre_fisier, "w") as f:
            for nota in self._note.values():
                f.write(str(nota)+"\n")

    def __init__(self, calea_catre_fisier):
        RepoNote.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def adauga_nota_repo(self, nota):
        """
            Deschide fisierul pentru a avea toate notele anterioare, adauga nota in fisier, si o scrie in fisier
        :param nota: entitate
        :return:
        """
        self.__read_all_from_file()
        RepoNote.adauga_nota_repo(self, nota)
        self.__write_all_to_file()

    def modifica_nota_repo(self, nota):
        """
             Deschide fisierul pentru a avea toate notele anterioare, modifica o nota din fisier, si o scrie in fisier
        :param nota:
        :return:
        """
        self.__read_all_from_file()
        RepoNote.modifica_nota_repo(self, nota)
        self.__write_all_to_file()

    def sterge_nota_dupa_id_repo(self, id_nota):
        """
             Deschide fisierul pentru a avea toate notele anterioare, stere nota din fisier, si o scrie in fisier
        :param id_nota:
        :return:
        """
        self.__read_all_from_file()
        RepoNote.sterge_nota_dupa_id_repo(self, id_nota)
        self.__write_all_to_file()

    def get_all_note_repo(self):
        """
            Deschide fisierul pentru a avea toate notele anterioare si le returneaza
        :return:
        """
        self.__read_all_from_file()
        return RepoNote.get_all_note_repo(self)

    def cauta_nota_dupa_id_repo(self, id_nota):
        """
            Deschide fisierul pentru a avea toate notele anterioare, si cauta o nota dupa id_ul ei
        :param id_nota:
        :return:
        """
        self.__read_all_from_file()
        return RepoNote.cauta_nota_dupa_id_repo(self, id_nota)

    def size(self):
        """
            Deschide fisierul pentru a avea toate notele anterioare, si reda lungimea dictionarului cu note
        :return:
        """
        self.__read_all_from_file()
        return RepoNote.size(self)
