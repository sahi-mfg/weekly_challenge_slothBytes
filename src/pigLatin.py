"""
week 2: Pig Latin Translation

Write a function that converts a sentence into pig latin.
Rules for converting to pig latin:
    - For words that begin with a vowel (a, e, i, o, u), add "way".
    - Otherwise, move all letters before the first vowel to the end and add "ay".
    - For simplicity, no punctuation will be present in the inputs
"""


def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "way")
        else:
            for i in range(len(word)):
                if word[i] in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(result)


if __name__ == "__main__":
    print(pig_latin("Cats are great pets."))
    print(pig_latin("Tom got a small piece of pie."))
    print(pig_latin("He told us a very exciting tale."))
    print(pig_latin("She sells seashells by the seashore."))
