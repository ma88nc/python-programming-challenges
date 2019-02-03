import sys

def isPalindrome(strIn):
    slen = len(strIn)
    idx = 0
    while idx < slen - idx:
        if strIn[idx] == strIn[slen-idx-1]:
            idx = idx+1
        else:
            break
    if idx < slen-idx-1:   
        return False
    else:         
        return True


def main():
    if len(sys.argv) == 1:
        print("Please supply a string")
        return

    strIn = sys.argv[1]
    print("Palindromis determinis")
    result = isPalindrome(strIn)
    if result == True:
        print("{} is a palindrome!".format(strIn))
    else:
        print("I'm sorry. {} is not a palindrome".format(strIn))    


if __name__ == '__main__':
    main()

