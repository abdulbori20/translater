from PyQt5.QtWidgets import *
import googletrans
from deep_translator import GoogleTranslator


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setting()
        self.initUI()
        self.event_handler()

        self.show()

    #Settings
    def setting(self):
        self.setGeometry(760, 370, 680, 400)
        self.setWindowTitle("Translator")

    #UI
    def initUI(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        main_layout = QHBoxLayout()
        vertical1 = QVBoxLayout()
        vertical2 = QVBoxLayout()
        vertical3 = QVBoxLayout()

        self.orginal_text = QTextEdit()
        self.orginal_box = QComboBox()
        vertical1.addWidget(self.orginal_text)
        vertical1.addWidget(self.orginal_box)
        main_layout.addLayout(vertical1)

        self.btn_translate = QPushButton("Translate")
        self.btn_clear = QPushButton("Clear")
        vertical2.addWidget(self.btn_translate)
        vertical2.addWidget(self.btn_clear)
        main_layout.addLayout(vertical2)

        self.new_text = QTextEdit()
        self.new_box = QComboBox()
        vertical3.addWidget(self.new_text)
        vertical3.addWidget(self.new_box)
        main_layout.addLayout(vertical3)

        self.languages = googletrans.LANGUAGES
        self.language_list = list(self.languages.values())

        self.orginal_box.addItems(self.language_list)
        self.new_box.addItems(self.language_list)
        self.orginal_box.setCurrentText("uzbek")
        self.new_box.setCurrentText("english")

        widget.setLayout(main_layout)

    #events
    def event_handler(self):
        self.btn_clear.clicked.connect(lambda: self.clear_clicked())
        self.btn_translate.clicked.connect(lambda: self.translate_clicked())

    #style
    def style(self):
        pass

    def clear_clicked(self):
        self.orginal_text.setText("")
        self.new_text.setText("")

        self.orginal_box.setCurrentText("uzbek")
        self.new_box.setCurrentText("english")

    def translate_clicked(self):
        try:
            for key, value in self.languages.items():
                if value == self.orginal_box.currentText():
                    source = key
            for key, value in self.languages.items():
                if value == self.new_box.currentText():
                    target = key

            words = self.orginal_text.toPlainText()

            result = GoogleTranslator(source=source, target=target).translate(words)
            self.new_text.setText(str(result))
        except Exception as e:
            QMessageBox.about(self, "Warning", "Nimadir xato ketti!")




if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()

    app.exec_()