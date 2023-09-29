# AUTHOR: Adam N
# PROGRAM: Art Ideas Generator

# import nonsense
import tkinter as tk
import random

# KEY FOR EXTRA GRAMMAR NONSENSE:
# $ -> put adjective at end
# ^ -> adjective ends with "a"
# * -> noun must be plural

# Lists
adjs = ["mystical","eccentric","snobbish","nervous",
        "^lost soul of a","agitated","^sworn enemy of a",
        "furious","zen","mysterious","$action figure","moody",
        "*Lord of the","adventurous","dinosaur",
        "science-based","deep-sea","extra-terrestrial",
        "$outfit","off-their-freaking-gourd","tiefling",
        "$who found Jesus","computer-rendered","influencer",
        "underwhelming"]

nons = ["assassin","goth","pizza delivery person",
        "stand-up comic","antique dealer","lighthouse keeper",
        "meteorologist","IT consultant","vampire",
        "tattoo artist","pirate","conspiracy theorist",
        "lawyer","ghost","thief","cow","wojak",
        "art teacher","streamer","game dev","puppeteer",
        "astronaut","Mothman","cosplayer","vampire hunter",
        "diver","hand model","baby","furry"]

# instantiate variables
vowels = "aeiouAEIOU"
adj = random.choice(adjs)
non = random.choice(nons)

# regenerate one of the words
def regenerate(word):
    if word in adjs:
        word = random.choice(adjs)
    elif word in nons:
        word = random.choice(nons)
    else:
        print("ERROR!")
    return word

# put together the sentence
def makethestuff(adjective, noun):
    a = "a"
    global vowels
    if adjective[0] == "*":
        adjective = adjective[1:]
        noun += "s"
    elif adjective[0] == "^":
        adjective = adjective[1:]
        if noun[0] in vowels:
            adjective += "n"
    elif adjective[0] == "$":
        adjective = adjective[1:]
        middle = adjective
        adjective = noun
        noun = middle
        
    if adjective[0] in vowels:
        a = "an"
    full = (f"YOU SHOULD DRAW: {a} {adjective} {noun}")
    return full

# set up window
win = tk.Tk()
win.title("Art Ideas Generator")
win.minsize(800,450)
win.geometry("800x450")

dfont = "calibri bold"

# main frames
frame1 = tk.Frame(win, width=100, height=220, bg="white")
frame1.pack(fill=tk.BOTH, expand=True)
frame2 = tk.Frame(win, width=100, height=100, bg="white")
frame2.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

bottomLeft = tk.Frame(frame2, bg="white", width=100, height=40)
bottomLeft.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
bottomRight = tk.Frame(frame2, bg="white", width=400, height=40)
bottomRight.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT)

# text label for prompt to go in
title = tk.Label(frame1,text="ART IDEAS Generator", bg="white", width=600, height=1, font=(dfont, 25))
title.pack(expand=True, fill=tk.Y)
label = tk.Label(frame1, text="Click to get started!", bg="white", width=80, height=5, font=(dfont, 18))
label.pack(expand=True, fill=tk.Y)

# button functions
def on_click_btnF():
    global adj
    global non
    adj = regenerate(adj)
    non = regenerate(non)
    label["text"] = makethestuff(adj, non)
    
def on_click_btnA():
    global adj
    global non
    adj = regenerate(adj)
    label["text"] = makethestuff(adj, non)
    
def on_click_btnN():
    global adj
    global non
    non = regenerate(non)
    label["text"] = makethestuff(adj, non)

#the actual buttons
btnF = tk.Button(bottomRight, text="GENERATE!", width=1, font=(dfont, 18), command=on_click_btnF)
btnF.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

btnA = tk.Button(bottomRight, text="NEW ADJECTIVE",  width=20, font=(dfont, 12), command=on_click_btnA)
btnA.pack(expand=True, side=tk.TOP, fill=tk.BOTH)

btnN = tk.Button(bottomRight, text="NEW NOUN",  width=20, font=(dfont, 12), command=on_click_btnN)
btnN.pack(expand=True, side=tk.TOP, fill=tk.BOTH) 

# begin
win.mainloop()
