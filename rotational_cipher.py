def rotate(text, key):

    new_text = []
    alphabet = ["a", "b", "c", "d", "e",
                "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y",
                "z"]
    alphabetUp = list(map(lambda x:x.upper(), alphabet))
    for letter in text:
        if letter in alphabet:
            if alphabet.index(letter) + key >= 26:
                key = (alphabet.index(letter) + key) % 26
                new_text.append(alphabet[key])
            else:
                new_text.append(alphabet[alphabet.index(letter) + key])

        elif letter in alphabetUp:
            if alphabetUp.index(letter) + key >= 26:
                key = (alphabetUp.index(letter) + key) % 26
                new_text.append(alphabetUp[key])
            else:
                new_text.append(alphabetUp[alphabetUp.index(letter) + key])
        else:
            new_text.append(letter)

    new_text = ''.join(new_text)
    return new_text