word = 'Manutha'

n = int(input("How many pass you want: "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']


def encoded_text(word, n):
    encoding_text = ""

    for letter in word:
        encode = letters.index(letter.lower()) + n
        cipher = encode % 26
        encoding_text += letters[cipher]

    return encoding_text


def decoded_text(encoding_text, n):
    decoding_text = ""

    for letter in encoding_text:
        decode = letters.index(letter.lower()) - n
        cipher = decode % 26
        decoding_text += letters[cipher]

    return decoding_text


encoded_word = encoded_text(word, n)
print("Encoded Text:", encoded_word)

decoded_word = decoded_text(encoded_word, n)
print("Decoded Text:", decoded_word)