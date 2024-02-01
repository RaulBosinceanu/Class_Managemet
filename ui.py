from erori.exceptii import ValidationError, RepoError


class UI(object):

    def __init__(self, service_student, service_probleme, service_note, generator_studenti, generator_probleme):
        self.__generator_studenti = generator_studenti
        self.__generator_probleme = generator_probleme
        self.__service_studenti = service_student
        self.__service_probleme = service_probleme
        self.__service_note = service_note
        self.__comenzi = {
            "add_student": self.__ui_adauga_student,
            "delete_student_by_id": self.__ui_sterge_student_dupa_id,
            "modify_student": self.__ui_modifica_student,
            "find_student_by_id": self.__ui_cauta_student_dupa_id,
            "add_assignment": self.__ui_adauga_problema,
            "delete_assignment_by_lab_number_problem_number": self.__ui_sterge_problema_dupa_nrLab_nrProblema,
            "modify_assignment": self.__ui_modifica_problema,
            "find_assignment_by_lab_number_problem_number": self.__ui_cauta_problema_dupa_nrLab_nrProblema,
            "generate_students": self.__ui_generare_studenti,
            "generate_assignments": self.__ui_generare_probleme,
            "grade_student": self.__ui_adauga_nota,
            "print_students": self.__ui_print_studenti,
            "print_assignments": self.__ui_print_problema,
            "print_grades": self.__ui_print_note,
            "student_list_for_assignment": self.__ui_lista_de_studenti_pt_o_problema,
            "students_below_5": self.__ui_studenti_sub_5,
            "average_with_highest_frequency": self.__ui_frecventa_max
        }

    def __print_menu(self):
        print('\n\n\n\n\n\n\n\n\n\n\n')
        print('------------------------------------------------------------STUDENT ORGANIZATION APPLICATION-----'
              '-------------------------------------------------------\n\n')
        print('The application manages students and assignments.txt\n')
        print('Each student has a unique ID consisting of four digits, a name, a surname, and a group')
        print('Student: XXXX, Full Name, Group\n')
        print('Each assignment has a lab number and problem number, a description, and a deadline')
        print('Assignment: XX_XX, Description, dd/mm/yyyy\n\n')
        print('CONSOLE MENU:')
        print('         >>>add_student: student_id, name, group')
        print('         >>>modify_student: student_id, new_name, new_group')
        print('         >>>delete_student_by_id: student_id')
        print('         >>>find_student_by_id: student_id')
        print('         >>>print_students\n')
        print('         >>>add_assignment: lab_number_problem_number, description, deadline')
        print('         >>>modify_assignment: lab_number_problem_number, new_description, new_deadline')
        print('         >>>delete_assignment_by_lab_number_problem_number: lab_number_problem_number')
        print('         >>>find_assignment_by_lab_number_problem_number: lab_number_problem_number')
        print('         >>>grade_student: grade_id, student_id, lab_number_problem_number, grade')
        print('         >>>generate_students: number')
        print('         >>>generate_assignments: number')
        print('         >>>print_assignments\n')
        print('         >>>print_grades\n')
        print('         >>>student_list_for_assignment: lab_number_problem_number')
        print('         >>>students_below_5')
        print('         >>>average_with_highest_frequency')
        print('         >>>exit')

    def __ui_adauga_student(self):
        if len(self.__params) != 3:
            print("Invalid parameters number")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grup = int(self.__params[2])
        self.__service_studenti.adauga_student_service(id_student, nume, grup)
        print("The student has been succesfully added")

    def __ui_sterge_student_dupa_id(self):
        if len(self.__params) != 1:
            print("Invalid parameters number!")
            return
        self.__service_studenti.sterge_student_dupa_id_service(int(self.__params[0]))
        print("The student has been succesfully deleted")

    def __ui_modifica_student(self):
        if len(self.__params) != 3:
            print("Invalid parameters number!")
            return
        self.__service_studenti.modifica_student_service(int(self.__params[0]), self.__params[1], int(self.__params[2]))
        print("The student has been succesfully modified")

    def __ui_cauta_student_dupa_id(self):
        if len(self.__params) != 1:
            print("Invalid parameters number")
            return
        print(self.__service_studenti.cauta_student_dupa_id_service(int(self.__params[0])))

    def __ui_print_studenti(self):
        if len(self.__params) != 0:
            print("Invalid parameters number")
            return
        studenti = self.__service_studenti.get_all_studenti_service()
        if len(studenti) == 0:
            print("There are no registered students")
            return
        for student in studenti:
            print(student)

    def __ui_adauga_problema(self):
        if len(self.__params) != 3:
            print("Invalid parameters number!")
            return
        nrLab_nrProblema = self.__params[0]
        desacriere = self.__params[1]
        deadline = self.__params[2]
        self.__service_probleme.adauga_problema_service(nrLab_nrProblema, desacriere, deadline)
        print("The assignment has been succesfully added")

    def __ui_sterge_problema_dupa_nrLab_nrProblema(self):
        if len(self.__params) != 1:
            print("Invalid parameters number")
            return
        self.__service_probleme.sterge_problema_dupa_nrLab_nrProblema_service(self.__params[0])
        print("The assignment has been succesfully deleted")

    def __ui_modifica_problema(self):
        if len(self.__params) != 3:
            print("Invalid parameters number!")
            return
        self.__service_probleme.modifica_problema_service(self.__params[0], self.__params[1], self.__params[2])
        print("The assignment has been succesfully modified")

    def __ui_cauta_problema_dupa_nrLab_nrProblema(self):
        if len(self.__params) != 1:
            print("Invalid parameters number")
            return

        print(self.__service_probleme.cauta_problema_dupa_nrLab_nrProblema_service(self.__params[0]))

    def __ui_print_problema(self):
        if len(self.__params) != 0:
            print("Invalid parameters number")
            return
        probleme = self.__service_probleme.get_all_probleme_service()
        if len(probleme) == 0:
            print("There are no registered assignements")
            return
        for problema in probleme:
            print(problema)

    def __ui_generare_studenti(self):
        if len(self.__params) != 1:
            print("Invalid parameters number")
            return
        self.__generator_studenti.generare_studenti(int(self.__params[0]))
        print("The", self.__params[0], "students was succesfully generated")

    def __ui_generare_probleme(self):
        if len(self.__params) != 1:
            print("Invalid parameters number")
            return
        self.__generator_probleme.generare_probleme(int(self.__params[0]))
        print("The", self.__params[0], "problems was succesfuly generated")

    def __ui_adauga_nota(self):
        if len(self.__params) != 4:
            print("Invalid parameters number!")
            return
        id_nota = int(self.__params[0])
        id_student = int(self.__params[1])
        id_problema = self.__params[2]
        nota = float(self.__params[3])
        self.__service_note.adauga_nota_service(id_nota, id_student, id_problema, nota)
        print("Grade succesfully given")

    def __ui_print_note(self):
        if len(self.__params) != 0:
            print("Invalid parameters number!")
            return
        note = self.__service_note.get_all_note_service()
        if len(note) == 0:
            print("There are no registered grades")
            return
        for nota in note:
            print(nota)

    def __ui_lista_de_studenti_pt_o_problema(self):
        if len(self.__params) != 1:
            print("Invalid parameters number!")
            return
        lista = self.__service_note.lista_de_studenti_pt_o_problema(self.__params[0])
        if lista == []:
            print('Are not students with this grade at this lab!')
        else:
            for student in lista:
                print(student)

    def __ui_studenti_sub_5(self):
        if len(self.__params) != 0:
            print("Invalid parameters number!")
            return
        lista = self.__service_note.studenti_sub_5()
        if lista == []:
            print('There are not students with average below 5!')
        else:
            for student in lista:
                print(student)

    def __ui_frecventa_max(self):
        if len(self.__params) != 0:
            print("Invalid parameters number!")
            return
        medie_max = self.__service_note.media_frecventa()
        if medie_max == 0:
            print('There are no grades')
        else:
            print(self.__service_note.media_frecventa())

    def run_ui(self):
        while True:
            self.__print_menu()
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split(": ")
            nume_comanda = parti[0]
            if len(parti) > 1:
                parametrii = parti[1].split(", ")
                self.__params = parametrii
            else:
                self.__params = []
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError as ve:
                    print(ve)
                except ValidationError as ve:
                    print(ve)
                except RepoError as re:
                    print(re)
            else:
                print("comanda invalida!")
