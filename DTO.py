class situatie_probleme:
    """
        Clasa de data transfer
    """
    def __init__(self, problema, lista_studenti):
        """
        Data transfer object
        :param problema:
        :param lista_studenti:
        :param nr_studenti:
        """
        self.__problema = problema
        self.__lista_studenti = lista_studenti
        self.__nr_studenti = len(self.__lista_studenti)


    def get_problema(self):
        """
        returneaza problema
        :return:
        """
        return self.__problema

    def get_lista_studenti(self):
        """
        returneaza lista de studenti care au nota la problema
        :return:
        """
        return self.__lista_studenti

    def get_nr_studenti(self):
        """
        returneaza numarul de studenti care au nota la problema respectiva
        :return:
        """
        return self.__nr_studenti

