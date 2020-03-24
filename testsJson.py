import json

with open('data.json') as json_data:
        scores = json.load(json_data)
        
name = input("Nom: ")
score = input("Score: ")

if name not in scores:
        scores.update({name: str(score)})

if int(scores[str(name)]) < int(score):
        scores.update({name: str(score)})

s = []

for sc in scores:
     s.append(int(scores[sc]))

s = sorted(s)

scores.update({"Best score": (s[-1])})  

with open('data.json', 'w') as fp:
	json.dump(scores, fp, indent=4)


                