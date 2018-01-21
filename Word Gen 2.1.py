"""Random Word Generator V. 2.1
    By Leveles """

from random import randint
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

consenant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vowel = ['a', 'e', 'i', 'o', 'u', 'y']

softletter = ['c', 'h', 'l', 'm', 'n', 'r', 's', 'w', 'z']

verysoftletter = ['h', 'l', 'r', 's', 'w']

softishletter = ['c', 'm', 'n', 'z']

hardletter = ['b', 'f', 'd', 'g', 'j', 'k', 'p', 'q', 'v', 't', 'x']

phrase = ""

length = 0

"""Change word value for length of generated word"""
word = 5

while length < word:
    letter = (random.choice(alphabet))
    phrase = phrase + letter
    length += 1

    """Hard Letter Check"""
    if letter in hardletter:
        length += 1
        flacidity = randint(1,2)
        if flacidity == 1:
            lettertwo = (random.choice(vowel))
            phrase = phrase + lettertwo
        if flacidity == 2:
            lettertwo = (random.choice(softletter))
            phrase = phrase + lettertwo

    """Soft Letter/ Very Soft Letter Check"""
    if letter in softletter:
        length += 1

        """Very Soft Letter Check"""
        if letter in verysoftletter:
            flacidity = randint(1,4)
            if flacidity == 1:
                lettertwo = (random.choice(vowel))
                phrase = phrase + lettertwo
            if flacidity == 2:
                lettertwo = (random.choice(verysoftletter))
                phrase = phrase + lettertwo
            if flacidity == 3:
                lettertwo = (random.choice(softletter))
                phrase = phrase + lettertwo
            if flacidity == 4:
                lettertwo = (random.choice(hardletter))
                phrase = phrase + lettertwo

        """Soft Letter Check"""
        if letter in softishletter:
            flacidity = randint(1,2)
            if flacidity == 1:
                lettertwo = (random.choice(vowel))
                phrase = phrase + lettertwo
            if flacidity == 2:
                lettertwo = (random.choice(verysoftletter))
                phrase = phrase + lettertwo

    """Vowel Check"""
    if letter in vowel:
        length += 1
        flacidity = randint(1,4)
        if flacidity == 1:
            lettertwo = (random.choice(vowel))
            phrase = phrase + lettertwo
        if flacidity == 2:
            lettertwo = (random.choice(verysoftletter))
            phrase = phrase + lettertwo
        if flacidity == 3:
            lettertwo = (random.choice(softletter))
            phrase = phrase + lettertwo
        if flacidity == 4:
            lettertwo = (random.choice(hardletter))
            phrase = phrase + lettertwo

    """Repeating Consenant Check"""
    if letter in consenant:
        if lettertwo in consenant:
            length += 1
            lettertwo = (random.choice(vowel))
            phrase = phrase + lettertwo

print(phrase.upper())
