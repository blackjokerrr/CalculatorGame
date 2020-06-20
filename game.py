import time, threading
from tkinter import *
from random import *


class Windows:
    
    frame = Tk()
    
    def setFrame(self):
        size = Frame(self.frame, width=400, height=400)
        size.pack()
        
    
    def run(self):
        self.setFrame()
        self.frame.mainloop()
        
class User:
    
    name = ''
    score = 0
    
    def setScore(self, score):
        
        self.score = score
    
    
    
class Question:
    
    box_question = Windows()
    name = ''
    counting_time = 0
    label = Label(box_question.frame)
    random_question = ''
    listed_quesion = []
    
    def setQuestion(self, name_of_question = ''):
        
        if name_of_question == '':
            self.name = self.randomQuestion()
        else:
            self.name = name_of_question
        self.label.config(text = self.name)
        self.label.pack()
    
        
    def countingTime(self):
        label = Label(self.box_question.frame)
        label.pack()
        
        def counting():
        
            while self.counting_time < 10:
                
                self.counting_time += 1
                label.config(text = str(self.counting_time))
                time.sleep(1)
                
            self.setQuestion(self.randomQuestion())
            self.counting_time = 0
            counting()
        
        
        t = threading.Thread(target = counting)
        t.start()
        
        
    def randomQuestion(self):
        
        self.listed_question = sample([1, 2, 3, 4, 5, 6, 7 , 8, 9 , 10], k=2)
        
        question = str(self.listed_question[0]) + ' + ' + str(self.listed_question[1])
        
        return question
        
        
    
    def show(self):
        
        
        self.setQuestion()
        self.countingTime()
    
    
    
class Answer:
    
    box_answer = Windows()
    object_question = Question()
    txt = Text(box_answer.frame, width=20, height=2)
    user = User()
    user.name = 'A'
    label_user = Label(box_answer.frame, text = 'User: ' + user.name + ' Score: ' + str(user.score))
    label_user.pack()
    

        
    def checkAnswer(self):
        answer = self.txt.get(1.0, END)
        question = self.object_question.label.cget('text')
        
        check_answer = question.split(' ')
        
        if (int(check_answer[0]) + int(check_answer[2])) == int(answer.strip('\n')):
            self.object_question.setQuestion(self.object_question.randomQuestion())
            self.user.score += 1
            self.label_user.config(text = 'User: ' + self.user.name + ' Score: ' + str(self.user.score))

    
    def show(self):
        
        btn = Button(self.box_answer.frame, text = 'Go', command = self.checkAnswer)
        
        self.txt.pack()
        btn.pack()
        
        
        

game = Windows()

game_question = Question()
game_answer = Answer()


game_question.show()
game_answer.show()

game.run()