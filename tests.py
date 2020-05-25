import json
gens = []
def afficherGens(gens):
	y = 0
	with open('data.json') as f:
		d = json.load(f)
	
	for i in d:
		gens.append(i + ": " + str(d[i]))

	for i in gens:
		print(i)
		y+=50
	return True

continuer = True

i = 0
fait = False
while i < 50:
	i+=1
	print(i)

	if not fait:
		fait = afficherGens(gens)