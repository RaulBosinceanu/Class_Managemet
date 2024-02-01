from erori.exceptii import RepoError


class RepoNote(object):
    """
        Clasa creata cu responsabilitatea de a gestiona note
    """
    def __init__(self):
        """
            Nota este un dictionar ce are ca si elemente entitati de tip nota
        """
        self._note = {}

    def __len__(self):
        """
            returneaza lungima dictionarului de note
        :return:
        """
        return len(self._note)

    def adauga_nota_repo(self, nota):
        """
        adauga o nota in dictionar
        :param nota:
        :return:
        """
        if nota.get_id_nota() in self._note:
            raise RepoError("nota existenta!")
        self._note[nota.get_id_nota()] = nota

    def cauta_nota_dupa_id_repo(self, id_nota):
        """
        identifica o nota in functie de id
        :param id_nota:
        :return:
        """
        if id_nota not in self._note:
            raise RepoError("nota inexistenta!")
        return self._note[id_nota]

    def modifica_nota_repo(self, nota):
        """
        modifica o nota
        :param nota:
        :return:
        """
        if nota.get_id_nota() not in self._note:
            raise RepoError("nota inexistenta!")
        self._note[nota.get_id_nota()] = nota

    def get_all_note_repo(self):
        """
        returneaza o lista cu toate notele intrduse
        :return:
        """
        r = []
        for id_nota in self._note:
            nota = self._note[id_nota]
            r.append(nota)
        return r

    def sterge_nota_dupa_id_repo(self, id_nota):
        """
        sterge nota daca id-ul este gasit
        :param id_nota:
        :return:
        """
        if id_nota not in self._note:
            raise RepoError("nota inexistenta!")
        del self._note[id_nota]

    def size(self):
        return len(self._note)
        