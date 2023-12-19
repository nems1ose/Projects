from tkinter import *
import random

time = 0
score = 0
level = 0

def addDigit(i):
    if (i != "-" or answerLabel['text'] == "") and len(answerLabel['text']) < 30:
        answerLabel['text'] += i

def deleteDigit():
    answerLabel['text'] = answerLabel['text'][:-1]

def generateExample():
    global time
    global level
    time = 10
    level += 1
    if level <= 5:
        num = random.randint(2, 4)
    elif level <= 10:
        num = random.randint(3, 5)
    elif level <= 15:
        num = random.randint(4, 6)
    else:
        num = random.randint(5, 7)
    example = ""
    valid = False
    while not valid:
        example = ""
        for i in range (num-1):
            example += str(random.randint(0, 10))
            if level > 10:
                ValTwoNum = random.randint(1, 2)
                if ValTwoNum == 2 and example[len(example)-1] != "0":
                    example += str(random.randint(0, 9))
            example += random.choice(["+", "-", "*", "/"])
        example += str(random.randint(0, 10))
        try:
            solved = eval(example)
            if isinstance(solved, int):
                valid = True
        except:
            pass
    return(example)

def skipExample():
    global score
    exampleLabel['text'] = generateExample()
    answerLabel['text'] = ""
    score -=  1
    scoreLabel['text'] = "SCORE: " + str(score)

def checkAnswer():
    global score
    if answerLabel['text'] != "":
        if eval(exampleLabel['text']) == int(answerLabel['text']):
            score += 5
        else:
            score -= 1
    else:
        score -= 1
    scoreLabel['text'] = "SCORE: " + str(score)
    answerLabel['text'] = ""
    exampleLabel['text'] = generateExample()

def startLevel():
    showLevel()
    global time
    global score
    global level
    time = 10
    score = 0
    level = 0
    scoreLabel['text'] = "SCORE: " + str(score)
    timeLabel['text'] = "TIME: " + str(time)
    answerLabel['text'] = ""
    exampleLabel['text'] = generateExample()
    updateDisplay()

def hideLevel():
    exampleLabel.grid_remove()
    answerLabel.grid_remove()
    for button in buttons:
        button.grid_remove()
    deleteButton.grid_remove()
    enterButton.grid_remove()
    skipButton.grid_remove()
    timeLabel.grid_remove()
    scoreLabel.grid_remove()
    root['bg'] = "pink"
    startButton.place(x = 80, y = 350)
    resultLabel.place(x = 0, y = 150)
    resultLabel['text'] = "YOUR SCORE: " + str(score)
    
def showLevel():
    exampleLabel.grid()
    answerLabel.grid()
    for button in buttons:
        button.grid()
    deleteButton.grid()
    enterButton.grid()
    skipButton.grid()
    timeLabel.grid()
    scoreLabel.grid()
    root['bg'] = "yellow"
    startButton.place_forget()
    resultLabel.place_forget()
    
def updateDisplay():
    global time
    if time == -1:
        hideLevel()
    else:
        timeLabel['text'] = "TIME: " + str(time)
        time -= 1
        root.after(1000, updateDisplay)

def keysControl(event):
    if event.char.isdigit() or event.char == "-":
        addDigit(event.char)

root = Tk()
root.title("Funny math")
root.resizable(width = False, height = False)
root.geometry("456x650")

exampleLabel = Label(root, height = 3, bg = "yellow", font = "Arial 20", text = generateExample())
exampleLabel.grid(columnspan = 4, row = 1, sticky = "ew")

answerLabel = Label(root, height = 3, bg = "yellow", font = "Arial 20")
answerLabel.grid(columnspan = 4, row = 6, sticky = "ew")

buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]

currentColumn = 0
currentRow = 2

for i in range (len(buttons)):
    buttons[i] = Button(root, width = 10, height = 5, bg = "pink", text = buttons[i], font = "Arial 10", command = lambda x = buttons[i]: addDigit(x))
    buttons[i].grid(column = currentColumn, row = currentRow)
    currentColumn += 1
    if currentColumn > 2:
        currentColumn = 0
        currentRow += 1

deleteButton = Button(root, bg = "pink", font = "Arial 10", text = "DELETE", command = deleteDigit)
deleteButton.grid(column = 2, row = 5, sticky = "ewns")

enterButton = Button(root, width = 22, bg = "pink", font = "Arial 10", text = "ENTER", command = checkAnswer)
enterButton.grid(column = 3, row = 2, rowspan = 3, sticky = "ns")

skipButton = Button(root, bg = "pink", font = "Arial 10", text = "SKIP", command = skipExample)
skipButton.grid(column = 3, row = 5, sticky = "ewns")
    
timeLabel = Label(root, height = 3, bg = "yellow", font = "Arial 15")
timeLabel.grid(column = 0, columnspan = 2, row = 0, sticky = "ew")

scoreLabel = Label(root, height = 3, bg = "yellow", font = "Arial 15")
scoreLabel.grid(column = 3, row = 0, sticky = "ew")

startButton = Button(root, height = 3, width = 25, bg = "yellow", text = "START", font = "Arial 15", command = startLevel)

resultLabel = Label(root, height = 5, width = 42, bg = "pink", font = "Arial 15")

hideLevel()
resultLabel.place_forget()

root.bind("<Return>", lambda event: checkAnswer())
root.bind("<BackSpace>", lambda event: deleteDigit())
root.bind("<space>", lambda event: skipExample())
root.bind("<Key>", keysControl)

root.mainloop()
