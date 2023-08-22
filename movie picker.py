from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, 
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout, QTextEdit, QInputDialog, QMessageBox
)
import json
from random import* 

app = QApplication([])
ventana_principal = QWidget()
ventana_principal.setWindowTitle("Movie list")
ventana_principal.resize(500, 300)

with open("movielist.json", "r", encoding="utf-8") as file:
    movies = json.load(file)

#lineas
main_line = QHBoxLayout()
vertic1 = QVBoxLayout()
vertic2 = QVBoxLayout()
#botones 
delete = QPushButton("Delete")
add = QPushButton("Add")
random = QPushButton("Random")
printed = QPushButton("Print")
movielist = QListWidget()
proceed = QPushButton("Proceed")
#mix it
main_line.addLayout(vertic1)
main_line.addLayout(vertic2)
vertic1.addWidget(movielist)
vertic2.addWidget(add)
vertic2.addWidget(delete)
vertic2.addWidget(random)
vertic2.addWidget(printed)
ventana_principal.setLayout(main_line)

#movie magic begins

def hit_it():
    with open("movielist.json", "w") as file:
        json.dump(movies, file, sort_keys=True)

def rand_msg(a):
    error = QMessageBox()
    error.setWindowTitle("Movie Picker")
    error.setText(a)
    error.exec_()

delete_confirmation = False
def certain():
    global delete_confirmation
    delete_confirmation = True

def uncertain():
    global delete_confirmation
    delete_confirmation = False

def randomfilm():
        randomovie = randint(1, 35)
        randomovie -= 1
        ranflickres = movies["Lista"][randomovie]
        print(ranflickres)
        rand_msg(ranflickres)

def add_movie():
    flick_name, result = QInputDialog.getText(ventana_principal, "add movie", "name of movie:")
    if flick_name != "":
        movies["Lista"] += [flick_name]
        movielist.addItem(flick_name)
        hit_it()
    
def delmovie():
    global delete_confirmation
    key = movielist.selectedItems()[0].text()
    certified = QMessageBox()
    certified.setWindowTitle("Proceed?")
    proceedbutt = certified.addButton("OK", certified.AcceptRole)
    proceedbutt.clicked.connect(certain)
    cancelbutt = certified.addButton("Cancel", certified.AcceptRole)
    cancelbutt.clicked.connect(uncertain)
    certified.exec_()
    if delete_confirmation == True:
        movies["Lista"].remove(key)
        movielist.clear()
        movielist.addItems(movies["Lista"])
        hit_it()
    else:
        pass

n = 1
def printlist():
    global n
    for i in movies["Lista"]:
        print(str(n) + ". " + i)
        n += 1
    n = 1


movielist.addItems(movies["Lista"])
random.clicked.connect(randomfilm)
add.clicked.connect(add_movie)
delete.clicked.connect(delmovie)
printed.clicked.connect(printlist)

ventana_principal.show()
app.exec_() 
