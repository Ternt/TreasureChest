class TreasureChest():
    #DECLARE question: STRING
    #DECLARE answer: INTEGER
    #DECLARE points: INTEGER
    question = ""
    answer = 0
    points = 0

    #question c)i)
    def getQuestion(self, questionNum):
        self.question = arrayTreasure[questionNum].question
        return print(self.question)
        

    #question c)ii)
    def checkAnswer(self, userAnswer):
        if userAnswer == answer:
            return True
        else:
            return False

    #question c)iii)
    def getPoints(self, attempts):
        if attempts == 1:
            return points
        elif attempts == 2:
            return(points//2)
        elif attempts == 3 or attempts == 4:
            return(points//4)
        else:
            return 0


#DECLARE arrayTreasure: 1D ARRAY
arrayTreasure = ["","","","","",""]

#DECLARE Questions: OBJECT
Questions = TreasureChest()

def readData():
    f = open("TreasureChestData.txt", "r")
    eof = False
    index = -1
    while eof == False:
            Questions.question = f.readline()
            Questions.answer = f.readline()
            Questions.points = f.readline()

            index += 1
            arrayTreasure[index] = TreasureChest()
            
            if Questions.question == "":
                eof = True

            
            

#question c)iv)
readData()

#DECLARE questionNum: INTEGER
questionNum = int(input("Please input a number between 1 and 5: "))

Questions.getQuestion(questionNum)





#DECLARE userAnswer: INTEGER
userAnswer = int(input())








        

