from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Cиний', 'Белый'))
app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo Card')

'''Интерфейс прилож-я Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('В каком году была основана Москва?') # текст ?а

RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране д переключателей с ответами
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')

AnsGroupBox = QGroupBox('Результат вопроса')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() # вертикальн будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # 2 ответа в I столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # 2 ответа во II столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в 1 строке

RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов

layout_line1 = QHBoxLayout() # ?
layout_line2 = QHBoxLayout() # варианты ответов // рез-т теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка дб большой
layout_line3.addStretch(1)

# Now созд-н строки разместим друг под др:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_questions():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroupBox.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_questions
    
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(test)

window.show()
app.exec()