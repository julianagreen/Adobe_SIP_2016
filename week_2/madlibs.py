input1 = input("adjective: ")
input2 = input("name: ")
input3 = input("pronoun: ")
input4 = input("ing verb: ")
input5 = input("verb: ")
input6 = input("noun: ")
input7 = input("store name: ")
input8 = input("noun: ")
input9 = input("relative or aquaintence: ")
input10 = input("room in a house: ")
input11 = input("hobby in the present tense: ")

pronoun2 = "her"

if input3 == "she":
	pronoun2 = "her"

if input3 == "him":
	pronoun2 = "his"

if input3 == "they":
	pronoun2 = "their"


print ('''

here is your mad lib:

	''')
print ("One " + input1 + " afternoon, " + input2 + " was " + input4 + " along when suddenly " + input3 + " " + input5 + " into a " + input6 + ". Then, " + input2 + " walked into a " + input7 + " and bought a " + input8 + " for " + pronoun2 + " " + input9 + ". Finally, " + input2 + " went home and went to " + input10 + " to " + input11)