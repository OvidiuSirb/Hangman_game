from controller.controller import Controller
from domain.entities import Sentence
from repository.repo import Repository
from repository.filerepo import FileRepo
from ui.console import Ui

repo = FileRepo()
controller = Controller(repo)

ui = Ui(controller)

repo.store(Sentence("Baloane cu apa"))
repo.store(Sentence("De ce iesi?"))
repo.store(Sentence("Blana de urs"))

ui.MainMenu()
