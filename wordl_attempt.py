# Importing necessary packages... 
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import math as m
import numpy as np
import random as rand
import sys
import json
import requests


# IMPORTING THE ACTUAL DICTIONARY!! FILLED WITH *ATUAL WORDS*
dictionary_url = 'https://raw.githubusercontent.com/tabatkins/wordle-list/main/words'
response = requests.get(dictionary_url)
text_content = response.text
words_list = text_content.split()
dictionary = {key: None for key in words_list}
#   CAN YOU DO ACTIVE SEARCHES FROM THE TERMINAL? MAYBE I CAN DO THAT FOR PROVIDED DEFINITION??

# Instantiating the tkinker root...
root = tk.Tk()
root.title("WALMART WORDL")
root.configure(background="white")
root.geometry("470x700")


# On-screen title instantiation...
'''
user_name = input("Before you begin, please INPUT your NAME!: ")
while True:
    if (len(user_name)>12):
        print("SORRY! Please choose a name that is 15 characters or less...")
    else:
        break
ow_title_title = "..." + str(user_name) + "'S WORDL..."
'''

ow_title_title = "               " #TEMPORARY PLACEHOLDER!!!
ow_title_title = ow_title_title.upper()
ow_title_fs = 20
ow_title_font = "Arial"
pady = 25
ow_title = tk.Label(
    root,
    text=ow_title_title,
    fg="black",
    bg="white",
    font=(ow_title_font, ow_title_fs,'bold','italic'))
ow_title.pack(pady=pady)
ow_title.pack()

# Instantiating background canvas for boxes...
canvas = tk.Canvas(
    root,
    width=2000,
    height=2000,
    bg="white")
canvas.pack()


# WORDL box array constants...
y0 = 15
lb_width = 80
lb_height = 90
border = 15
division_space = 10
box_width = 0

# Creating WORDL box array...
for i in range(5):
    for j in range(6):
        x_left = border+i*(lb_width+division_space)
        y_left = y0+j*(lb_height+division_space)
        x_right = border+i*(lb_width+division_space)+lb_width
        y_right = y0+j*(lb_height+division_space)+lb_height
        box = canvas.create_rectangle(x_left, y_left, x_right, y_right,
                outline="black", width=box_width, fill="whitesmoke")

root.update()



# IMPORTANT GRAPHICS STUFF FOR CONFETTI IMPLEMENTATION!!...
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Instantiaing memory mechanisms for confetti...
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
confetti = []


# ------- root.geometry("470x700") --------

# Confetti object definition...
def create_confetti():
    x = rand.randint(50, 420)
    y = rand.randint(100, 600)
    color = rand.choice(colors)
    size = rand.randint(5, 15)
    
    angle = rand.uniform(0, m.pi*2)
    speed = rand.uniform(1, 5)
    
    dx = speed * m.cos(angle)
    dy = speed * m.sin(angle)

    c = canvas.create_oval(
        x,
        y,
        x+size,
        y+size,
        fill=color)
    confetti.append([c, dx, dy])
    
def animate_confetti():
    # Move the confetti objects...
    for c in confetti:
        canvas.move(c[0], c[1], c[2])
        ####
        canvas.tag_raise(c[0], "all")
        
        # Added randomness to confetti motion...
        c[1] += rand.uniform(-0.1, 0.1)
        c[2] += rand.uniform(-0.1, 0.1)
    
    # Animation delay...
    root.after(50, animate_confetti)# Instantiaing memory mechanisms for confetti...
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
wordl = rand.choice(list(dictionary.keys())).upper()
#wordl = 'honor'
wordl_chars = [letter for letter in wordl]


# Constant letter characteristics...
l_fontsize = 45
l_font = "Arial"
l_color = "white"

# Determining canvas origin...
#   'c_'='canvas'
c_x0 = 3
c_y0 = y0+ow_title_fs+pady+20
c_border = 13


# Row and column counters...
n_rows = 6
n_columns = 5
row_counter = 0
column_counter = 0

print(wordl)
while (row_counter<n_rows):

    guess_ref_list = ['first','second','third','fourth','fifth','sixth and final']
    if (row_counter==5):
        # While loop to ensure proper input...
        while True:
            guess = input("Your " + guess_ref_list[row_counter] + " guess!?: ").upper()
            if (guess.isalpha()==True):
                guess = guess.upper()
                # Checking if the guess is the right length...
                if (len(guess)==5):
                    # Checking if the guess is in the word list...
                    if (guess.lower() in dictionary): 
                        break
                    else:
                        print("  SORRY! That word isn't in my word list!...")
                else:
                    print("  SORRY! Please input a five letter word...")
                    continue
            else:
                print("  SORRY! Please input a five letter word with only characters...")
    else:
        # While loop to ensure proper input...
        while True:
            guess = input("Your " + guess_ref_list[row_counter] + " guess?: ").upper()
            if (guess.isalpha()==True):
                guess = guess.upper()
                # Checking if the guess is the right length...
                if (len(guess)==5):
                    # Checking if the guess is in the word list...
                    if (guess.lower() in dictionary): 
                        break
                    else:
                        print("  SORRY! That word isn't in my word list!...")
                else:
                    print("  SORRY! Please input a five letter word...")
                    continue
            else:
                print("  SORRY! Please input a five letter word with only *actual letters*...")

    
    # WHEN THE GUESS IS COMPLETELY CORRECT!...
    if (wordl==guess):

        bg="forest green"
        fill=bg
    
        # Positioning letters...
        for l in range(len(guess)):
        
            # To re-color box backgrounds...
            x_left = (border)+l*(lb_width+division_space)
            y_left = (border)+row_counter*(lb_height+division_space)
            x_right = (border)+l*(lb_width+division_space)+lb_width
            y_right = (border)+row_counter*(lb_height+division_space)+lb_height


            box = canvas.create_rectangle(x_left, y_left, x_right, y_right,
                    outline="black", width=box_width, fill=fill)
            
            # Positioning letters...
            l_proj = tk.Label(root, text=guess[l], fg=l_color,
                    bg=bg, font=(l_font, l_fontsize))
            l_width = Label.winfo_reqwidth(l_proj)
            l_height = Label.winfo_reqheight(l_proj)
            l_proj.place(x=(c_x0+c_border+m.floor((lb_width-l_width)/2)+l*(lb_width+division_space)),
                    y=(c_y0+c_border+m.floor((lb_height-l_height)/2)+row_counter*(lb_height+division_space)))
            
        #root.update()
        
        # Spacing out the creation of individual confetti objects...
        for i in range(50):
            root.after(i*100, create_confetti)
        animate_confetti()
        root.update()
        print("You've guessed the Walmart Wordl! Congrats!")
        #print()
        break
    

    # WHEN THE GUESS IS INCORRECT / PARTIALLY CORRECT...
    for l in range(len(guess)):

        # Adjusting letter font background color...
        bg="gray34"
        for x in wordl:
            if (guess[l]==x):
                bg="gold"
        if (guess[l]==wordl[l]):
            bg="forest green"
        fill=bg

        # To re-color box backgrounds...
        x_left = (border)+l*(lb_width+division_space)
        y_left = (border)+row_counter*(lb_height+division_space)
        x_right = (border)+l*(lb_width+division_space)+lb_width
        y_right = (border)+row_counter*(lb_height+division_space)+lb_height

        box = canvas.create_rectangle(x_left, y_left, x_right, y_right,
                outline="black", width=box_width, fill=fill)

        # Positioning letters...
        l_proj = tk.Label(root, text=guess[l], fg=l_color,
                bg=bg, font=(l_font, l_fontsize, 'bold'))
        l_width = Label.winfo_reqwidth(l_proj)
        l_height = Label.winfo_reqheight(l_proj)
        l_proj.place(x=(c_x0+c_border+m.floor((lb_width-l_width)/2)+l*(lb_width+division_space)),
                y=(c_y0+c_border+m.floor((lb_height-l_height)/2)+row_counter*(lb_height+division_space)))
        
        root.update()

    row_counter += 1
    column_counter += 1
    if (row_counter==6):
        # Printing result...
        print("I'm sorry!! The Walmart Wordl was, ", str(wordl).upper(), ".", sep='')  #+ ": ")
        print("  Better luck next time!!")

# Running the window..
sys.exit()
root.mainloop()



'''
#how to make confetti at the end / a rainbow? -- can you make a sound w confetti?
#how to code it to reveal / 'flip' letters slowly?
#how to make it so you can actually only access this code once a day?
#how to code using GUI? how to make it slowly flip through each letter? color the box? etc
#HOW TO MAKE THIS BADDIE QUICKLY SURF A DUCTIONARY?
#   HOW TO MAKE IT MAYBE RANK LETTERS IN TERMS OF EASINESS? ~COMMONALITY~
#   MAYBE AT THE END IT CAN PROVIDE THE DEFITION OF THE WORDL???
'''

'''
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#test_word = "MONEY"
#test_word_ls = [letter for letter in test_word]

for l in range(n_columns):
    for r in range(n_rows):
        l_proj = tk.Label(root, text=test_word_ls[l], fg="black",
                      bg="whitesmoke", font=("American Typewriter", l_fontsize))
        l_width = Label.winfo_reqwidth(l_proj)
        l_height = Label.winfo_reqheight(l_proj)
        l_proj.place(x=(c_x0+c_border+m.floor((lb_width-l_width)/2)+l*(lb_width+division_space)),
                      y=(c_y0+c_border+m.floor((lb_height-l_height)/2)+r*(lb_height+division_space)))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
'''


'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
word_list = ['cloak', 'fight', 'muddy']
wordl = rand.choice(word_list).upper()
wordl_chars = [letter for letter in wordl]
print(wordl)
#while

#print("Welcome to WALMART WORDL:")
#print("   You have 6 tries to guess the Wordl! \n")
counter = 0
while (counter<6):

    guess_ref_list = ['first','second','third','fourth','fifth','sixth and final']
    if (counter==5):
        guess = input("Your " + guess_ref_list[counter] + " guess!?: ").upper()
    else:
        guess = input("Your " + guess_ref_list[counter] + " guess?: ").upper()
    guess_chars = [letter for letter in guess]

    # Comparing the letters...
    for i in range(len(wordl_chars)):
        if (wordl_chars[i] != guess_chars[i]):
            guess_chars[i] = '_'

    # Joining return word...
    return_word = ' '.join(guessc_chars)
    comparison_word = ''.join(guess_chars)
    print(wordl, comparison_word)
    if (wordl==comparison_word):
        print("You've guessed the Walmart Wordl! Congrats!")
        break

    print('Your word: ', return_word)
    counter += 1
    if (counter==5):
        # Printing result...
        print("I'm sorry -- it looks like you did not get the Walmart Wordl :( \n Better luck next time!!")

'''
# root.bind("<Control-+>", lambda event: increase_font_size())
