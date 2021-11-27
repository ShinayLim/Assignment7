word_count = 0
char_count = 0
vowels=0
consonants=0

user_input = input("Type your sentence here: ")

split_string = user_input.split()

word_count = len(split_string)

for word in split_string:
    char_count += len(word)

for i in user_input:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels = vowels + 1
    else:
        consonants = consonants + 1
        
print("\nTotal words : {}".format(word_count))

print("\nTotal characters : {}".format(char_count))

print("\nTotal number of vowels:",vowels)

print("\nTotal number of consonant:",consonants)
