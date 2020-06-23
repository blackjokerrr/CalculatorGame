import time, threading
from tkinter import *
from random import *


class Windows:
    
    
    frame = Tk()
    
    frame.title('Calculatate Game')
    
    size = Frame(frame, width=300, height=40)
    
    
    def setFrame(self):
        self.size.pack()
        
    
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
    mode = 'Easy'
    label_mode = Label(box_question.frame, text = mode)
    label_mode.pack()
    
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
        
        
    def randomQuestion(self, mode = ''):
        
        
        if self.mode == 'Normal' or mode == 'Normal':
            self.listed_question = sample([randrange(10, 100), randrange(10, 100)], k=2)
            
        elif self.mode == 'Hard' or mode == 'Hard':
            self.listed_question = sample([randrange(100, 1000), randrange(100, 1000)], k=2)
        
        else:
            self.listed_question = sample([1, 2, 3, 4, 5, 6, 7 , 8, 9 , 10], k=2)
            
            
        question = str(self.listed_question[0]) + ' + ' + str(self.listed_question[1])
            
        return question
    
    
        
    def setMode(self, event):
        
        if event.char == 'n':
            self.mode = 'Normal'
            
        elif event.char == 'h':
            self.mode = 'Hard'
            
        else:
            self.mode = 'Easy'
            
        self.label_mode.config(text = self.mode)
        self.label_mode.pack()
        
    
    def show(self):
        
        self.box_question.size.bind_all('<e>', self.setMode)
        self.box_question.size.bind_all('<n>', self.setMode)
        self.box_question.size.bind_all('<h>', self.setMode)

        self.setQuestion()
        self.countingTime()
    
    
    
    
class Answer:
    
    box_answer = Windows()
    object_question = Question()
    txt = Text(box_answer.frame, width=20, height=0)
    user = User()
    user.name = 'A'
    label_user = Label(box_answer.frame, text = 'User: ' + user.name + ' Score: ' + str(user.score))
    label_user.pack()
    

    
        
    def checkAnswer(self, event):
        answer = self.txt.get(1.0, END)
        question = self.object_question.label.cget('text')
        mode = ''
        
        check_answer = question.split(' ')
        
        if len(check_answer[0]) > 2:
            mode = 'Hard'
        elif len(check_answer[0]) > 1:
            mode = 'Normal'
        else:
            mode = 'Easy'

        
        if (answer.strip('\n')).isdigit() and (int(check_answer[0]) + int(check_answer[2])) == int(answer.strip('\n')):
            self.object_question.setQuestion(self.object_question.randomQuestion(mode))
            self.user.score += 1
            self.label_user.config(text = 'User: ' + self.user.name + ' Score: ' + str(self.user.score))
            self.txt.delete(1.0, END)
        elif (answer.strip('\n')).isdigit():
            self.user.score -= 1
            self.label_user.config(text = 'User: ' + self.user.name + ' Score: ' + str(self.user.score))
            self.txt.delete(1.0, END)
        else:
            self.txt.delete(1.0, END)
            
    
    def show(self):
        
        btn = Button(self.box_answer.frame, text = 'Go').place(x = 137, y = 110)
        
        self.txt.pack()

        self.box_answer.size.bind_all('<Return>', self.checkAnswer)
        self.box_answer.size.pack()
        
        
        

game = Windows()

game_question = Question()
game_answer = Answer()


game_question.show()
game_answer.show()

game.run()