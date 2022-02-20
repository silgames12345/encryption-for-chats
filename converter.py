#import math


letters = "abcdefghijklmnopqrstuvwxyz 0123456789,'.?!"
alphabeth = "abcdefghijklmnopqrstuvwxyz"

def str2int(str):
    global alphabeth
    strint = 0
    for i in str:
        if(i in alphabeth):
            encoded = i.encode("utf-8")
            charint = int(encoded[0] - 87)
            strint = (strint * 100) + charint
        else:
            if(i == " "):
                strint = (strint * 100) + 36
            elif(i == "0"):
                strint = (strint * 100) + 37
            elif(i == "1"):
                strint = (strint * 100) + 38
            elif(i == "2"):
                strint = (strint * 100) + 39
            elif(i == "3"):
                strint = (strint * 100) + 40
            elif(i == "4"):
                strint = (strint * 100) + 41
            elif(i == "5"):
                strint = (strint * 100) + 42
            elif(i == "6"):
                strint = (strint * 100) + 43
            elif(i == "7"):
                strint = (strint * 100) + 44
            elif(i == "8"):
                strint = (strint * 100) + 45
            elif(i == "9"):
                strint = (strint * 100) + 46
            elif(i == ","):
                strint = (strint * 100) + 47
            elif(i == "'"):
                strint = (strint * 100) + 48
            elif(i == "."):
                strint = (strint * 100) + 49
            elif(i == "?"):
                strint = (strint * 100) + 50
            elif(i == "!"):
                strint = (strint * 100) + 51
            
    return strint

def int2str(msg, math, split):
    global letters
    lenght = len(str(msg))
    splitted = split_str(str(msg), 10, split)
    fully_decrypted = ""
    for i in splitted:
        c = int(i)
        lenght2 = len(i)
        a = 1
        decrypted = ""
        #print(c)
        for b in range(0, lenght2 - 2):
            a = a * 10
        
        for b in range(0, int(lenght2/2)):
            charint = int(math.floor(c/a) - 10)
            #print(charint)
            char = letters[charint]
            decrypted = decrypted + char
            used = (charint + 10) * a
            c = c - (used)
            #print(c)
            a = int(a/100)
        fully_decrypted = fully_decrypted + decrypted
    return fully_decrypted

def split_str(seq, chunk, split, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

#msg1 = "hallo ik ben sil1234567890"
#msg = str2int(msg1)
#print(msg)
#decrypted = int2str(msg, math)
#print(decrypted)