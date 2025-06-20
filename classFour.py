
name = input("Enter your name: ")
print("Good Afternoon, " + name + "!")

letter = 'Dear <|Name|>, You are selected! <|Date|>'

letter_name = input("Enter your name for the letter: ")
letter_date = input("Enter the date (e.g. 20 June 2025): ")

letter = letter.replace("<|Name|>", letter_name)
letter = letter.replace("<|Date|>", letter_date)

print(letter)

sentence = input("Enter a sentence to check for double spaces: ")

double_space_index = sentence.find("  ")

fixed_sentence = sentence.replace("  ", " ")

print(fixed_sentence)
