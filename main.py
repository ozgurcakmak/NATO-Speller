#!/usr/bin/python3

NATO_ALPHABET = {
	"a":"Alpha",
	"b":"Bravo",
	"c":"Charlie",
	"d":"Delta",
	"e":"Echo",
	"f":"Foxtrot",
	"g":"Golf",
	"h":"Hotel",
	"i":"India",
	"j":"Juliet",
	"k":"Kilo",
	"l":"Lima",
	"m":"Mike",
	"n":"November",
	"o":"Oscar",
	"p":"Papa",
	"q":"Quebec",
	"r":"Romeo",
	"s":"Sierra",
	"t":"Tango",
	"u":"Uniform",
	"v":"Victor",
	"w":"Whiskey",
	"x":"X-Ray",
	"y":"Yankee",
	"z":"Zulu",
	"1" : "One",
	"2" : "Two",
	"3" : "Three",
	"4" : "Four",
	"5" : "Five",
	"6" : "Six",
	"7" : "Seven",
	"8" : "Eight",
	"9" : "Nine",
	"0" : "Zero"

}

def sanitize_turkish(character):
	if character in "çöışüğ":
		character = character.replace("ç","c")
		character = character.replace("ö","o")
		character = character.replace("ı","i")
		character = character.replace("ş","s")
		character = character.replace("ü","u")
		character = character.replace("ğ","g")
	return character

def spell(words):
	message = f"You inserted {" ".join(words)}. Its NATO spelling is:\n\n"
	for word in words:
		for char in word:
			if char.isalpha() == False and  char.isnumeric()==False:
				continue
			alphabet = NATO_ALPHABET[sanitize_turkish(char.lower())]
			message += alphabet + "\n"
		message += "\n"
	return message

def main():
	import sys
	if len(sys.argv)==1:
		raise Exception("python3 main.py <word to nato-ize>")
	arguments = sys.argv	
	words = arguments.copy()
	del words[0]
	
	message = spell(words)
	print(message)

main()
