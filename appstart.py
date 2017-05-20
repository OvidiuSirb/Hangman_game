from controller.controller import Controller
from domain.entities import Sentence
from repository.repo import Repository
from repository.filerepo import FileRepo
from ui.console import Ui

repo = FileRepo()
controller = Controller(repo)

ui = Ui(controller)

repo.store(Sentence("N-avem saltele"))
repo.store(Sentence("Du-te si bateti coasa"))
repo.store(Sentence("blana urs yeah"))

ui.MainMenu()