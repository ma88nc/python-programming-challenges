# Implement an algorithm to determine if a string has all unique characters.
# From Laakman-McDowell, "Cracking the Code Interview", 6th edition, problem 1.1, p. 90

import sys

def isUnique(str):
    #Initialize bucket to zeroes
    bkt = [0] * (255-32)

    # Go through the input string one character at a time and check the count in the slot for the ASCII
    # value representing that character. If the value is zero, increment the count; if the count is >0,
    # the char was already seen, so exit with False. Otherwise, if we make it though the string,
    # it means that no unique chars were found, so return True.
    for i in range(0, len(str)):
        ascii = ord(str[i])
        if (bkt[ascii-32]) > 0:
            return False
        else:
            bkt[ascii-32] += 1            
    return True


def main():
    if len(sys.argv) == 1:
        print("Please enter a string")
        return

    print("Stringus checkus uniqueus!")
    print("Result for check of uniqueness of characters: {}".format(isUnique(sys.argv[1])))   


if __name__ == '__main__':
    main()