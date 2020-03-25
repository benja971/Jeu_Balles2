from tkinter import *
import json

fen=Tk()
scores = {}
secondes = 24

def verif():
	with open('data.json') as json_data:
		scores = json.load(json_data)
		scores.update({"Best score": 0})
					
	if saisie.get() not in scores:
		scores.update({saisie.get(): str(secondes)})

	if int(scores[str(saisie.get())]) < int(secondes):
		scores.update({saisie.get(): str(secondes)})

	s = []

	for sc in scores:
		s.append(int(scores[sc]))

	s = sorted(s)

	scores.update({"Best score": (s[-1])}) 

	with open('data.json', 'w') as fp:
		json.dump(scores, fp, indent=4)
    
	fen.destroy()


texte=Label(fen, text='Veuillez entrer votre pseudo', width=30, height=3, fg="black")
texte.pack()
saisie=StringVar()
entree=Entry(fen,textvariable=saisie, width=30)
entree.pack()
bou1=Button(fen , text='Valider', command=verif)
bou1.pack()
fen.mainloop()
