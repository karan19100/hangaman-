import random
from tkinter import *
from tkinter import messagebox
from typing import List

def get_word() -> List[str]:
    # choosing word
    dictionary_word = {"Flower": ["Sunflower", "Rose", "Lily", "Lotus", "Jasmine"],
                        "Animal":["Bear", "Lion", "Tiger", "Wolf", "Horse"],
                        "Fruit":["Apple", "Banana", "Grapes", "Orange", "Guava"],
                        "City":["Delhi", "Mumbai", "Chennai", "Hyderabad", "Kolkata"],
                        "Emotion":["Angry", "Sad", "Love", "Excitement", "Surprise"]}

    word_hint_name = list(dictionary_word.keys())[random.randint(0,len(dictionary_word.keys()) - 1)]
    selected_word = dictionary_word[word_hint_name][random.randint(0,len(dictionary_word[word_hint_name]) - 1)].lower()
    return word_hint_name, selected_word

score = 0
run = True
is_played = 0

# main loop
while run:
    is_played += 1
    root = Tk()
    root.geometry('905x700')
    root.title('HANG MAN')
    root.config(bg = '#E7FFFF')
    root.resizable(False,False)
    count = 0
    win_count = 0

    hint, selected_word = get_word()

    # creation of word dashes variables
    print(hint," ",selected_word)

    x = 250
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={}, y={})'.format(i,x,450))
        
    #letters icon
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    
    for let in al:
        exec('{}=PhotoImage(file="alphabets/{}.png")'.format(let,let))

        
    # hangman images
    h123 = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', hint]
    for hangman in h123:
        exec('{}=PhotoImage(file="hangmanAndHint/{}.png")'.format(hangman,hangman))

    #letters placement
    button = [['b1', 'a', 0, 520], ['b2', 'b', 70, 520], ['b3', 'c', 140, 520], ['b4', 'd', 210, 520], ['b5', 'e', 280, 520],
              ['b6', 'f', 350,520], ['b7' ,'g' ,420, 520], ['b8', 'h', 490,520], ['b9', 'i', 560, 520], ['b10', 'j', 630, 520],
              ['b11' ,'k' ,700,520], ['b12' ,'l' ,770, 520], ['b13', 'm', 840, 520], ['b14', 'n', 0, 595], ['b15', 'o', 70, 595],
              ['b16' ,'p' ,140,595], ['b17' ,'q' ,210, 595], ['b18', 'r', 280, 595], ['b19', 's', 350, 595], ['b20', 't', 420, 595],
              ['b21','u',490,595], ['b22','v',560,595], ['b23', 'w', 630, 595], ['b24', 'x', 700, 595], ['b25', 'y', 770, 595],
              ['b26' ,'z' ,840, 595]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    #hangman placement
    han = [['c1', 'h1'], ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'], ['c5', 'h5'], ['c6', 'h6'], ['c7', 'h7'], ['c8', hint]]
    for p1 in han:
        exec(f'{p1[0]}=Label(root,bg="#E7FFFF",image={p1[1]})')
    
    # placement of first hangman image
    c1.place(x = 350,y = 50)

    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(root,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
    ex.place(x=770,y=10)
    s2 = 'SCORE:'+str(score)
    s1 = Label(root,text = s2,bg = "#E7FFFF",font = ("arial",25))
    s1.place(x = 10,y = 10)

    def instruction():
        list_of_instruction_points = ["Welcome to the Hangman Game",
                                        "You have to guess the letters of the word",
                                        "After three wrong attempts you will get a hint",
                                        "Guess the correct word and save yourself from hanging",
                                        "Let's start the Game"]
        
        for hint in list_of_instruction_points:
            messagebox.showinfo("Read Carefully",hint)

    # instruction calling
    if score == 0 and is_played == 1:
        instruction()

    # button press check function
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,350,50))

            # adding suggestion
            if count == 3:
                exec('c{}.place(x={},y={})'.format(count+5,100,100))


            if count == 6:
                answer = messagebox.showinfo('Word is', selected_word.upper())
                answer = messagebox.askyesno('GAME OVER', 'YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()  

    root.mainloop()