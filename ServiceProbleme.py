from domain.probleme import Probleme


class ServiceProbleme:

    def __init__(self, __repo_problema, __validator_problema):
        self.__repo_problema = __repo_problema
        self.__validator_problema = __validator_problema

    def size(self):
        """
        reda lungimea listei de probleme.txt
        :return:
        """
        return len(self.__repo_problema)

    def adauga_problema_service(self, nrLab_nrProblema, descriere, deadline):
        """
        adauga un student cu id, nume si grup dupa ce apeleaza functia de validare pentru a verifica daca este valida
        :param nrLab_nrProblema: string
        :param descriere: string
        :param deadline: data
        :return:
        """
        problema = Probleme(nrLab_nrProblema, descriere, deadline)
        self.__validator_problema.valideaza(problema)
        self.__repo_problema.adauga_problema_repo(problema)

    def cauta_problema_dupa_nrLab_nrProblema_service(self, nrLab_nrProblema):
        """
        cauta o anumita problema in functie de nr labuluisi al problemei
        :param nrLab_nrProblema: string
        :return:
        """
        return self.__repo_problema.cauta_problema_dupa_nrLab_nrProblema_repo(nrLab_nrProblema)

    def modifica_problema_service(self, nrLab_nrProblema, descriere, deadline):
        """
        actuallizeaza o problema cu nrLab_nrProblema, dcriere si deadline-ul introduse de utilizator daca acestea sunt
        valide pentru modificare
        :param nrLab_nrProblema: string
        :param descriere: string
        :param deadline: data
        :return:
        """
        problema = Probleme(nrLab_nrProblema, descriere, deadline)
        self.__validator_problema.valideaza(problema)
        self.__repo_problema.modifica_problema_repo(problema)

    def sterge_problema_dupa_nrLab_nrProblema_service(self, nrLab_nrProblema):
        """
        sterge o problema din lista daca nrLab_nrProblema introdus de utilizator este valid
        :param nrLab_nrProblema: string
        :return:
        """
        self.__repo_problema.sterge_problema_dupa_nrLab_nrProblema_repo(nrLab_nrProblema)

    def get_all_probleme_service(self):
        """
        afiseaza intreaga lista de probleme.txt
        :return:
        """
        return self.__repo_problema.get_all_probleme_repo()
