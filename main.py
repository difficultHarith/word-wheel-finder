requiredLetter = "l"
OPTIONAL4 = "baumcane"

OPTIONAL3 = list(OPTIONAL4)
REQUIRED3 = [requiredLetter]


def check_letters(string):
    OPTIONAL = list(OPTIONAL4)
    REQUIRED = [requiredLetter]
    REQUIRED2 = [requiredLetter]

    """ Checks whether a word is ONLY made up from the valid letter set """
    string = string.strip()

    if len(string) < 4:
        return False

    for let in string:
        # check each let(ter) of string against the lists
        if let not in OPTIONAL + REQUIRED:
            return False
        else:
            if let in OPTIONAL:
                OPTIONAL.remove(let)
            else:
                REQUIRED.remove(let)
                

    for let in REQUIRED2:
        # check the WORD against REQUIRED
        if let not in string:
            return False
        else:
            REQUIRED2.remove(let)

    return True


def print_longest(words):
    """ Prints the longest valid word, and how many letters long it is """
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("The longest valid word was '{}' at {} letters long"
          .format(longest, len(longest)))


valid_words = []
# by using a set - we won't have duplicates - saving some time
for letter in set(OPTIONAL3 + REQUIRED3):
    # only open + parse the dictionaries we need (as a slight time saving measure)
    f = open("./Dictionary/" + letter + ".txt", "r")

    for line in f:
        if check_letters(line):
            valid_words.append(line.strip())

valid_words.sort()
valid_words.sort(key=len, reverse = False)
print("Optional Letters - {}\tRequired Letters - {}"
      .format(" ".join(OPTIONAL3), " ".join(REQUIRED3)))
print("With that letter set, there are {} valid words\n"
      .format(len(valid_words)))
print("\n".join(valid_words) + "\n")
print_longest(valid_words)
