import sys, math

from PyQt5.QtWidgets import QApplication, QAction, QAbstractButton, QMenu, QMainWindow, QMessageBox, \
    QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, pyqtSignal

from pyqt_dark_calculator.inputLinedit import InputLineEdit
from pyqt_dark_calculator.calculatorPadWidget import CalculatorPadWidget
from pyqt_dark_calculator.resultWidget import ResultWidget
from pyqt_style_setter import StyleSetter


class Calculator(QMainWindow):
    newClicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__resultWidget = ResultWidget()
        self.__inputLineEdit = InputLineEdit()
        self.__inputLineEdit.equalPressed.connect(self.equalPressed)

        self.__numpadWidget = CalculatorPadWidget()

        lay = QVBoxLayout()
        lay.addWidget(self.__resultWidget)
        lay.addWidget(self.__inputLineEdit)
        lay.addWidget(self.__numpadWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

        self.setWindowTitle('Dark calculator')

        self.__initMenuUi()
        self.__initBtn()

        self.setFocusProxy(self.__inputLineEdit)

        StyleSetter.setWindowStyle(self, exclude_type_lst=[QAbstractButton])

    def __createActions(self):
        # File actions
        self.__newAction = QAction("New...", self)
        self.__newAction.setShortcut("Ctrl+N")
        self.__newAction.triggered.connect(self.__new)

    def __createMenuBar(self):
        self.__menubar = self.menuBar()
        self.__filemenu = QMenu('File', self)
        self.__menubar.addMenu(self.__filemenu)
        self.__filemenu.addAction(self.__newAction)
        self.setMenuBar(self.__menubar)

    def __initMenuUi(self):
        self.__createActions()
        self.__createMenuBar()

    def __initBtn(self):
        self.__btns = self.__numpadWidget.getBtns()
        for btn in self.__btns:
            btn.padBtnClicked.connect(self.__btnClicked)

    def __new(self):
        self.newClicked.emit()

    def __btnClicked(self, text):
        line_edit_text = self.__inputLineEdit.text()
        last_n = self.__inputLineEdit.getLastOperand()
        if text == 'Del':
            self.__inputLineEdit.backspace()
        elif text == '±':
            if last_n:
                self.__showResult('{0}*-1'.format(line_edit_text))
        elif text == 'Rnd':
            if last_n:
                self.__showResult('round({0})'.format(line_edit_text))
        elif text == '=':
            self.equalPressed()
        elif text == 'Sqrt':
            if last_n:
                n = eval(line_edit_text)
                if float(n) < 0:
                    QMessageBox.information(self, 'Warning',
                                            'You cannot pass the negative to calculate the square root.')
                else:
                    self.__showResult('math.sqrt({0})'.format(line_edit_text))
        elif text == 'x^2':
            if last_n:
                self.__showResult('math.pow({0}, 2)'.format(line_edit_text))
        elif text == '1/x':
            if last_n:
                self.__showResult('1/{0}'.format(line_edit_text))
        elif text == 'C':
            if self.__resultWidget.count() > 0:
                lastText = self.__resultWidget.getLastText()
                self.__inputLineEdit.clear()
                self.__inputLineEdit.setText(lastText)
            else:
                self.__inputLineEdit.clear()
        elif text == 'CA':
            self.__inputLineEdit.clear()
            self.__resultWidget.clear()
        else:
            self.__inputLineEdit.insert(text)
        self.__inputLineEdit.setFocus()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.equalPressed()
        return super().keyPressEvent(e)

    def equalPressed(self):
        text = self.__inputLineEdit.text()
        last_n = self.__inputLineEdit.getLastOperand()
        if last_n:
            self.__showResult(text)

    def __showResult(self, text):
        formula_text = str(text)
        value_number = eval(str(text))
        value_text = str(value_number)
        if isinstance(value_number, int):
            pass
        else:
            if value_number.is_integer():
                value_text = '{0:0.0f}'.format(value_number)
        self.__resultWidget.setText(formula_text, value_text)
        self.__inputLineEdit.setText(value_text)