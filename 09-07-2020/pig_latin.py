import sys

VOWEL = 1
CONSONANT = 2
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def main():
	print("running")
	sentence = "piG latin banana will butler happy duck me smile string stupid glove trash floor store eat omelet are egg explain always ends honest I"
	pig_latin_check = "iGpay atinlay ananabay illway utlerbay appyhay uckday emay ilesmay ingstray upidstay oveglay ashtray oorflay orestay eatyay omeletyay areyay eggyay explainyay alwaysyay endsyay onesthay Iyay"
	
	pig_latin_check_list = pig_latin_check.split(" ")
	word_list = sentence.split(" ")

	pig_latin_list = []
	for word in word_list: 
		type = get_first_character(word)
		txt = word
		if type == VOWEL:
			txt = txt + "yay"
		else:
			txt = get_consonant_type(txt)

		pig_latin_list.append(txt)

	if len(word_list) != len(pig_latin_check_list) != len(pig_latin_list):
		print("Error in the number of words")
	else:
		idx = 0
		txt_list = sentence.split(" ")

		for pig_latin_word in pig_latin_list:
			if pig_latin_word != pig_latin_check_list[idx]:
				print("ERROR")
				print("original text:"+word_list[idx])
				print("converted pig latin text:"+pig_latin_word)
				print("correct pig latin text:"+pig_latin_check_list[idx])
				sys.exit()
			idx += 1
		print("Original sentence is '"+sentence +"'")
		print("Pig latin sentence is '" + ' '.join(pig_latin_list) +"'")

def get_consonant_type(text):
	num_consonants = 0
	for char in text:
		if vowels.count(char) > 0 :
			consonants = text[0:num_consonants]
			break
		else:
			num_consonants += 1

	text = text.replace(consonants, '')
	pig_latin = text + consonants + "ay"
	return pig_latin


def get_first_character(text):
	global vowels
	if vowels.count(text[0]) > 0 :
		return VOWEL
	else:
		return CONSONANT
		
main()
