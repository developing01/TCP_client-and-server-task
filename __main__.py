from PySide2 import QtWidgets, QtGui

import server  #DON`T REMOVE

import client_tcp #імпортую клієнт щоб запустити весь процес через __main__


def client():
    path_to_image = "byte_info.jpg" #додаю шлях до картинки
    return path_to_image


def main():
    path = client()
    app = QtWidgets.QApplication([])
    label = QtWidgets.QLabel()
    label.setMinimumSize(100, 100)
    label.setPixmap(QtGui.QPixmap(path))
    label.show()
    app.exec_()


if __name__ == '__main__':
    main()
