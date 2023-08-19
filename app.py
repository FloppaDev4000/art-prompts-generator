# AUTHOR: Adam Noonan
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
        "*Lord of the","adventurous","dinosaur"]

nons = ["assassin","goth","pizza delivery person",
        "stand-up comic","antique dealer","lighthouse keeper",
        "meteorologist","IT consultant","vampire",
        "tattoo artist","pirate","conspiracy theorist",
        "lawyer","ghost","thief"]

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
    full = (f"DRAW: {a} {adjective} {noun}")
    return full

# set up window
win = tk.Tk()
win.title("app")
win.geometry("640x480")

# text label for prompt to go in
label = tk.Label(win, text="ART IDEAS GENERATOR.\n Click the buttons to start!",
font=('Calibri 15 bold'))
label.pack(pady=20)

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
btnA = tk.Button(win, text="NEW ADJECTIVE", command=on_click_btnA)
btnA.pack(pady=40)

btnN = tk.Button(win, text="NEW NOUN", command=on_click_btnN)
btnN.pack(pady=40)

btnF = tk.Button(win, text="GENERATE", command=on_click_btnF)
btnF.pack(pady=40)

# begin
win.mainloop()