def rotate(text, key):

    new_text = []
    alphabet = ["a", "b", "c", "d", "e",
                "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y",
                "z"]
    for letter in text:
        if alphabet.index(letter) + key >= 26:
            key = (alphabet.index(letter) + key) % 26
            new_text.append(alphabet[key])
        else:
            new_text.append(alphabet[alphabet.index(letter) + key])

    new_text = ''.join(new_text)
    return new_text