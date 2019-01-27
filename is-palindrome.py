import sys

def isPalindrome(strIn):
    return True


def main():
    if len(sys.argv) == 1:
        print("Please supply a string")
        return

    strIn = sys.argv[1]
    result = isPalindrome(strIn)
    if result == True:
        print("{0} is a palindrome!".format(strIn))
    else:
        print("I'm sorry. {0} is not a palindrome", format(strIn))    


if __name__ == '__main__':
    main()

