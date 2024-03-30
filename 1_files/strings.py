greeting = "Hello, World!"
name = "Stiven"
age = 20
personal_greeting = "My name is " + name + " and I\'m " + str(age) + " years old."
word = "supercallifragilisticexpialidocious"
message = "The word {word} contains {word_length} letters.".format(word = word, word_length = len(word))
animals = "giraffes"
city = "London"
zoo_message = f"{ animals.capitalize() } are the tallest animals in the { city } Zoo."
hamburger = "bun\nlettuce\ncheese\nketchup\npatty\nbun"

print(zoo_message)