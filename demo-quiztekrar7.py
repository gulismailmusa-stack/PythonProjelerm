# python demo-quiztekrar7.py
#Question
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer

# print(q1.checkAnswer("java"))
# print(q2.checkAnswer("python"))
# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestions(self):
        
        return self.questions[self.questionIndex]
    def displayQuestions(self):
        question=self.getQuestions()
        print(f"Soru {self.questionIndex + 1} : {question.text} ")
        for q in question.choices:
            print("-" + q)
        answer=input("cevap: ")
        self.guess(answer)
        
        
    def guess(self,answer):
        question=self.questions[self.questionIndex]
        if(question.checkAnswer(answer)):
            self.score+=1
        
        self.questionIndex+=1
        
        self.loadQuestions()
        
    def loadQuestions(self):
        if(len(self.questions)==self.questionIndex):
            print("Quiz bitti")
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestions()
    def showScore(self):
        print("score",self.score)
    def displayProgress(self):
        totalQuestions=len(self.questions)
        questionNumber=self.questionIndex
        print(f"Question {totalQuestions} of {questionNumber + 1}".center(100,"*"))
        
q1=Question("en iyi programlama dili hangisidir ?",["python","C#","java","javascript"],"python")
q2=Question("en anlaşilir programlama dili hangisidir ?",["python","C#","java","javascript"],"python")
q3=Question("en sade programlama dili hangisidir ?",["python","C#","java","javascript"],"python")
questions=[q1,q2,q3]
quiz=Quiz(questions)
quiz.loadQuestions()