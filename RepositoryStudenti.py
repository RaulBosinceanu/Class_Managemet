from erori.exceptii import RepoError


class RepoStudenti(object):

    def __init__(self):
        self._studenti = {}

    def __len__(self):
        return len(self._studenti)

    def adauga_student_repo(self, student):
        """
        adauga studentul student in lista de studenti
        :param student:
        :return:
        """
        if student.get_id_student() in self._studenti:
            raise RepoError("student existent!")
        self._studenti[student.get_id_student()] = student

    def cauta_student_dupa_id_repo(self, id_student):
        """
        identifica un student in functie de id
        :param id_student:
        :return:
        """
        if id_student not in self._studenti:
            raise RepoError("student inexistent!")
        return self._studenti[id_student]

    def modifica_student_repo(self, student):
        """
        modifica toate atributele unui student: id, nume si grup
        :param student:
        :return:
        """
        if student.get_id_student() not in self._studenti:
            raise RepoError("student inexistent!")
        self._studenti[student.get_id_student()] = student

    def get_all_studenti_repo(self):
        """
        afiseaza toti studentii din lista studenti
        :return:
        """
        r = []
        for id_student in self._studenti:
            student = self._studenti[id_student]
            r.append(student)
        return r

    def sterge_student_dupa_id_repo(self, id_student):
        """
        sterge student daca id-ul este gasit
        :param id_student:
        :return:
        """
        if id_student not in self._studenti:
            raise RepoError("student inexistent!")
        del self._studenti[id_student]

    def size(self):
        return len(self._studenti)

