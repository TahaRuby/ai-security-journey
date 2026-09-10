# import variable and module

# create function
def clean_word(word):
    return "".join(ch for ch in word if ch.isalnum())


def find_longest_words(sentence):
    words = sentence.split()

    max_len = 0
    for word in words:
        cleaned = clean_word(word)
        if len(cleaned) > max_len:
            max_len = len(cleaned)

    longest_words = []
    for word in words:
        cleaned = clean_word(word)
        if len(cleaned) == max_len:
            longest_words.append(word)

    return longest_words, max_len


# running application
sentence = input("Enter a sentence: ")
longest_words, max_len = find_longest_words(sentence)

print("\nLongest word(s):")
for word in longest_words:
    print(f"{word} ({max_len} letters)")