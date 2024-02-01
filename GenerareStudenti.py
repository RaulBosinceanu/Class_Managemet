class GenerareStudenti:
    def __init__(self,service_studenti):
        self.__service_studenti = service_studenti

    def generare_student(self):
        """
        genereaza un student random
        :return:
        """
        import random
        self.__id_student = random.randint(1000,9999)
        self.__nume = random.choice(["Bosinceanu", "Moldovan", "Muntean", "Paraschiv", "Cezar", "Odobasian", "Latcu" 
                                     "Fizi", "Avram", "Baciu", "Bozga"])
        self.__prenume = random.choice(["Raul", "Diana", "Mircea", "Darius", "Eduard", "Paul", "Alex", "Csabi", ""
                                     "Bianca", "Costel", "Alin", "Dragos"])
        self.__nume_student = self.__nume + ' ' + self.__prenume
        self.__grup = random.randint(100,999)
        return self.__id_student, self.__nume_student, self.__grup

    def generare_studenti(self, nr):
        """
        genereaza numarul nr de studenti random
        :param nr:
        :return:
        """
        for i in range(nr):
            id_student, nume, grup = self.generare_student()
            self.__service_studenti.adauga_student_service(id_student, nume, grup)