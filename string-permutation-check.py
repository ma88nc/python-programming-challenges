# Given two strings, write a method to decide if one is a permutation of the other.
# From Laakman-McDowell, "Cracking the Code Interview", 6th edition, problem 1.2, p. 90

import sys


def buildBucket(str, bkt):
    # print("Length of bkt is {}".format(len(bkt)))
    for i in range(0,len(str)):
        ascii = ord(str[i])
        bkt[ascii-32] += 1

def main():
    if len(sys.argv) < 3:
        print("Please invoke with two strings. This script will check if one is a permutation of the other.")
        return

    print("Permutatus determinus!")
    str1 = sys.argv[1]
    str2 = sys.argv[2]

    # First check if the strings are of same length. If not, conclude one cannot be a permutation of the other.
    if len(str1) != len(str2):
        print("{} is not a permutation of {}".format(str1, str2))       
        return   

    # Build buckets for the two strings.
    bkt1 = [0] * (255-32)
    buildBucket(str1, bkt1)
    bkt2 = [0] * (255-32)
    buildBucket(str2, bkt2)    
    
    # Now compare the buckets. They should be identical. If not, the permutation check fails.
    perms = True
    for i in range(0, 255-32):
        if bkt1[i] != bkt2[i]:
            perms = False
            
    print("Strings are permutations") if perms == True else print("Strings are not permutations")
            

if __name__ == '__main__':
    main()