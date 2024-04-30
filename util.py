import string


def cleanOutputText(text: str) -> str:
    words = text.split()
    result = []

    for word in words:
        if word.startswith("'") and word.endswith("'"):
            word = word[1:-1]  # Remove the single quotes from the word

        # Check if the word is a contraction and expand it
        if word.lower().endswith("'m"):
            word = word[:-2] + " am"
        elif word.lower().endswith("'s"):
            if word.lower() == "it's":
                word = "it is"
            else:
                word = word[:-2] + "s"
        elif word.lower().endswith("n't"):
            if word.lower() == "won't":
                word = "will not"
            elif word.lower() == "can't":
                word = "cannot"
            elif word.lower() == "shan't":
                word = "shall not"
            else:
                word = word[:-3] + " not"
        elif word.lower().endswith("'ll"):
            word = word[:-3] + " will"
        elif word.lower().endswith("'re"):
            word = word[:-3] + " are"
        elif word.lower().endswith("'ve"):
            word = word[:-3] + " have"
        elif word.lower().endswith("'d"):
            if word.lower() == "i'd":
                word = "i would"
            else:
                word = word[:-2] + " would"

        # Replace special characters with spaces
        word = "".join(char if char not in string.punctuation else " " for char in word)

        result.append(word)

    return " ".join(result)
