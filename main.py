from Generare.GenerareProbleme import GenerareProbleme
from Generare.GenerareStudenti import GenerareStudenti
from bussiness.ServiceNota import ServiceNote
from bussiness.ServiceProbleme import ServiceProbleme
from bussiness.ServiceStudenti import ServiceStudenti
from infrastructura.RepositoryProbleme import RepoProbleme
from infrastructura.RepositoryStudenti import RepoStudenti
from infrastructura.RepositoryNote import RepoNote
from infrastructura.file_repo_note import FileRepoNote
from infrastructura.file_repo_probleme import FileRepoProbleme
from infrastructura.file_repo_studenti import FileRepoStudenti
from interfata.ui import UI
from teste.TesteFileNote import TesteFileNote
from teste.TesteFileProbleme import TesteFileProbleme
from teste.TesteFileStudenti import TesteFileStudenti
from teste.TesteNote import TesteNote
from teste.TesteStudenti import Teste
from validari.ValidariNote import ValidatorNote
from validari.ValidariProbleme import ValidatorProblema
from validari.ValidariStudenti import ValidatorStudent


class ValidotorStudent:
    pass


class Main:
    def __init__(self):
        pass

    teste_studenti = Teste()
    teste_studenti.ruleaza_toate_testele()
    repo_studenti = RepoStudenti()
    calea_catre_fisier_studenti = 'studenti.txt'
    file_repo_studenti = FileRepoStudenti(calea_catre_fisier_studenti)
    validator_studenti = ValidatorStudent()
    service_studenti = ServiceStudenti(file_repo_studenti, validator_studenti)
    repo_probleme = RepoProbleme()
    calea_catre_fisier_probleme = "probleme.txt"
    file_repo_probleme = FileRepoProbleme(calea_catre_fisier_probleme)
    validator_problema = ValidatorProblema()
    service_probleme = ServiceProbleme(file_repo_probleme, validator_problema)
    generator_studenti = GenerareStudenti(service_studenti)
    generator_probleme = GenerareProbleme(service_probleme)
    teste_note = TesteNote()
    teste_note.ruleaza_toate_testele_note()
    validator_note = ValidatorNote()
    repo_note = RepoNote()
    cale_catre_fisier_note = "note.txt"
    file_repo_note = FileRepoNote(cale_catre_fisier_note)
    service_note = ServiceNote(file_repo_note, file_repo_studenti, file_repo_probleme, validator_note)
    teste_file_studenti = TesteFileStudenti()
    teste_file_studenti.run_all_tests()
    teste_file_probleme = TesteFileProbleme()
    teste_file_probleme.run_all_tests()
    teste_file_note = TesteFileNote()
    #teste_file_note.run_all_tests()
    ui = UI(service_studenti, service_probleme, service_note, generator_studenti, generator_probleme)
    ui.run_ui()


