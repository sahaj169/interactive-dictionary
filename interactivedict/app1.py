import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
	w = w.lower()	
	if w in data:
		return data[w]
	elif len(get_close_matches(w,data.keys()))>0:
		A = get_close_matches(w,data.keys())[0]
		B = str(input((f'did you mean {A} instead ? Enter Y if yes or N if No:  ')))
		if B.lower() == "y":
			return data[A]
		elif B.lower() == "n": 
			return "This word is not available plz recheck "
		else:
			return "Invalid Entry"
	else:
		return "Invalid Input. entered word is not available"

while True:
	word = input("Enter word: ")

	meaning = translate(word)

	if type(meaning)== list:
		for i in meaning:
			print(i)
	else:
		print(meaning)

