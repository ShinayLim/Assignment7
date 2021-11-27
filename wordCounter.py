word_count = 0
char_count = 0

user_input = input("Type your sentence here: ")

split_string = user_input.split()

word_count = len(split_string)

for word in split_string:
    char_count += len(word)
