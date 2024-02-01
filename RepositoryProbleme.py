from erori.exceptii import RepoError


class RepoProbleme(object):

    def __init__(self):
        self._probleme = {}

    def __len__(self):
        return len(self._probleme)

    def adauga_problema_repo(self, problema):
        """
        adauga problema problema in lista de probleme.txt
        :param problema:entitate
        :return:
        """
        if problema.get_nrLab_nrProblema() in self._probleme:
            raise RepoError("problema existenta!")
        self._probleme[problema.get_nrLab_nrProblema()] = problema

    def cauta_problema_dupa_nrLab_nrProblema_repo(self, nrLab_nrProblema):
        """
        identifica un o problema in functie de numarul laboratorului
        :param nrLab_nrProblema:string
        :return:
        """
        if nrLab_nrProblema not in self._probleme:
            raise RepoError("problema inexistenta!")
        return self._probleme[nrLab_nrProblema]

    def modifica_problema_repo(self, nrLab_nrProblema):
        """
        modifica toate atributele unui student: id, nume si grup
        :param nrLab_nrProblema: string
        :return:
        """
        if nrLab_nrProblema.get_nrLab_nrProblema() not in self._probleme:
            raise RepoError("problema inexistenta!")
        self._probleme[nrLab_nrProblema.get_nrLab_nrProblema()] = nrLab_nrProblema

    def get_all_probleme_repo(self):
        """
        afiseaza toate problemele din lista probleme.txt
        :return:
        """
        r = []
        for nrLab_nrProblema in self._probleme:
            problema = self._probleme[nrLab_nrProblema]
            r.append(problema)
        return r

    def sterge_problema_dupa_nrLab_nrProblema_repo(self, nrLab_nrProblema):
        """
        sterge problema dapa numarul ei
        :param nrLab_nrProblema:
        :return:
        """
        if nrLab_nrProblema not in self._probleme:
            raise RepoError("problema inexistenta!")
        del self._probleme[nrLab_nrProblema]

    def size(self):
        return len(self._probleme)
