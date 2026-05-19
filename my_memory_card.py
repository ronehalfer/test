from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QLabel, QPushButton)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(700, 500)

lb_question = QLabel("Question")
radio_group_box = QGroupBox("answer options")
rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")
btn_ok = QPushButton("Answer")

radio_group = QButtonGroup()
radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

layout_ans_1 = QHBoxLayout()
layout_ans_2 = QHBoxLayout()
layout_ans_main = QVBoxLayout()

layout_ans_1.addWidget(rbtn_1)
layout_ans_1.addWidget(rbtn_2)

layout_ans_2.addWidget(rbtn_3)
layout_ans_2.addWidget(rbtn_4)

layout_ans_main.addLayout(layout_ans_1)
layout_ans_main.addLayout(layout_ans_2)
radio_group_box.setLayout(layout_ans_main)

ans_group_box = QGroupBox("Result")
lb_result = QLabel("Right or wrong")
lb_correct = QLabel("Right answer")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
ans_group_box.setLayout(layout_res)

layout_row_1 = QHBoxLayout()
layout_row_2 = QHBoxLayout()
layout_row_3 = QHBoxLayout()
layout_card = QVBoxLayout()

layout_row_1.addWidget(lb_question, alignment = Qt.AlignCenter)
layout_row_2.addWidget(radio_group_box)

layout_row_2.addWidget(ans_group_box)
ans_group_box.hide()

layout_row_3.addStretch(1)
layout_row_3.addWidget(btn_ok, stretch=2)
layout_row_3.addStretch(1)

layout_card.addLayout(layout_row_1, stretch=2)
layout_card.addLayout(layout_row_2, stretch=8)
layout_card.addLayout(layout_row_3, stretch=1)

layout_card.setSpacing(5)
window.setLayout(layout_card)

def show_result():
    radio_group_box.hide()
    ans_group_box.show()
    btn_ok.setText("Next question")

def show_question():
    ans_group_box.hide()
    radio_group_box.show()
    btn_ok.setText("Answer")
    radio_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_group.setExclusive(True)

class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3): 
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

from random import shuffle

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct!")
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("Wrong!")

def next_question():
    window.cur_q += 1
    if window.cur_q > len(questions_list) -1:
        shuffle(questions_list)
        window.cur_q = 0
    q = questions_list[window.cur_q]
    ask(q)

def click_ok():
    if btn_ok.text()=="Answer":
        check_answer()
    else:
        next_question()

q = Question("What is the value of the acceleration due to gravity on Earth?", "9.8", "15.3", "6.7", "3.2")
q1 = Question("What is Pi?", "3.14", "2.14859230414", "3.41", "2.49",)
q2 = Question("How much is 1 liter of distiled water?", "1kg", "1.4kg", "0.5kg", "1.2kg",)
q3 = Question("What is the most expencive part in a gaming PC?", "GPU", "CPU", "RAM", "Motherboard",)
q4 = Question("Whats the most popular song ever made?", "Happy Birthday to You", "Smooth Criminal", "We Wish You Merry Christmas", "Never Gonna Give You Up",)
q5 = Question("Which theorem states that every finite group whose order is divisible by a prime number p contains an element of order p?", "Cauchys Theorem", "Lagranges Theorem", "Cayleys Theorem", "Fermats Little Theorem",)
q6 = Question("In quantum mechanics, what does the Pauli exclusion principle state?", "No two identical fermions can occupy the same quantum state", "Particles can exist in two places at once", "Energy is always conserved in closed systems", "Light behaves only as a wave",)

questions_list = [q, q1, q2, q3, q4, q5, q6]
shuffle(questions_list)
window.cur_q = -1

btn_ok.clicked.connect(click_ok)
next_question()


window.show()
app.exec_()