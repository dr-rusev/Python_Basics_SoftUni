# word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" \
# or word[0] == "y" or word[0] == "A" or word[0] == "E" or word[0] == "I" \
# or word[0] == "O" or word[0] == "U" or word[0] == "Y":

most_powerful_word = ""
word_power, haviest_word = 0, 0

word = input()

while word != "End of words":
    word_power = 0

    for letter in word:

        word_power += ord(letter)

    if word[0] in "aeiouyAEIOUY":
        word_power *= len(word)

    else:
        word_power //= len(word)

    if word_power > haviest_word:
        haviest_word = word_power
        most_powerful_word = word

    word = input()

print(f"The most powerful word is {most_powerful_word} - {haviest_word}")

# word = "Experience"
# word_power = 0
# for letter in word:
#     word_power += ord(letter)
#     print(word_power)
#

