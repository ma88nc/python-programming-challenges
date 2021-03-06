# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
#
# From Laakman-McDowell, Cracking the Code Interview, 6th ed, p. 91
import sys

def simpleStringCompress(strIn):
    current_ch = ''
    current_ch_cnt = 0
    strOut = ''
    for ch in strIn:
        if ch != current_ch:
            if current_ch != '':
                strOut += current_ch + str(current_ch_cnt)
            current_ch = ch
            current_ch_cnt = 1
        else:
            current_ch_cnt += 1
    strOut += current_ch + str(current_ch_cnt)
   
   # If compressed string is not shorter than original string,
   # then just return the original.
    print ("Input str on len={} compressed to {}".format(len(strIn), len(strOut)))
    return strOut if len(strOut) < len(strIn) else strIn

def main():
    if len(sys.argv) == 1:
        print("Please supply string to compress. Example: aaabccccaddee")
        return

    ret = simpleStringCompress(sys.argv[1])
    print('Stringis compressis')
    print(ret)

if __name__ == '__main__':
    main()
