class GenerareProbleme:
    def __init__(self, service_probleme):
        self.__service_probleme = service_probleme

    def generare_problema(self):
        """
        genereaza o problema random
        :return:
        """
        import random
        self.__nrLab = random.randint(1, 14)
        self.__nrProblema = random.randint(1, 28)
        self.__nrLab_nrProblema = str(self.__nrLab) + '_' + str(self.__nrProblema)
        self.__descriere = random.choice(["adauga", "sterge", "muta", "aplica", "calculeaza", "dubleaza",  "taie"])
        self.__deadline = random.choice(["27/04/2022", "26/08/2022", "14/01/2022", "30/04/2023", "25/10/2022",
                                         "23/08/2024", "27/08/2022", "01/02/2022", "31/09/2023", "19/04/2022",
                                         "17/11/2022", "27/12/2022"])
        return self.__nrLab_nrProblema, self.__descriere, self.__deadline

    def generare_probleme(self, nr):
        """
        genereaza numarul nr de probleme.txt random
        :param nr:
        :return:
        """
        i = 0
        while i < nr:
            nrLab_nrProblema, descriere, deadline = self.generare_problema()
            try:
                self.__service_probleme.adauga_problema_service(nrLab_nrProblema, descriere, deadline)
            except:
                continue
            i += 1
