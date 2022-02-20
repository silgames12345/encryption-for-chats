import time
import math
import random
import findprimes
import findprimitiverootmodulov2
import converter
from posixpath import split

common_private_min = 1000
common_private_max = 3000

secret_min = 1000
secret_max = 100000

print("Choose person you are")
person = input("1 or 2: ")

if(person == str(1)):
    common_private_a = findprimes.findprime(time, math, random, common_private_min, common_private_max)
    _common_private_b = findprimitiverootmodulov2.primroots(common_private_a, math)
    length = random.randrange(0, len(_common_private_b))
    common_private_b = _common_private_b[length]
    common_private = str(common_private_a) + "." + str(common_private_b)
    print("")
    print(f"send {common_private} this into the chat")
    _ = input("press enter if you put the thing above into the chat")
    print("")
else:
    common_private = input("Input common_private ")

common_private_list = common_private.split(".")
common_private_a = int(common_private_list[0])
common_private_b = int(common_private_list[1])

secret = findprimes.findprime(time, math, random, secret_min, secret_max)

#public_my = math.fmod(common_private_b ^ secret, common_private_a)
public_my = pow(common_private_a, secret, common_private_b)

print("")
print(f"send this {int(public_my)} into the chat")
_ = input("press enter if you put the thing above into the chat")
print("")

public_him = input("input the number that you recieved from the other messenger ")
print("")
public_him = int(public_him)

#shared_secret = int(math.fmod(public_him ^ secret, 23))
shared_secret = int(pow(public_him, secret, common_private_b))
print(f"shared secret is {shared_secret}")
print("")

while True:
    send_recv = input("send(1) or recive(2) message 1 or 2 ")
    if(send_recv == str(1)):
        msg = input("enter your message here: ")
        msgint = converter.str2int(msg)
        msglist = converter.split_str(str(msgint), 8, split)
        encrypted = ""
        for i in msglist:
            semi_encrypted = int(i) * shared_secret
            encrypted = encrypted + str(semi_encrypted) + "."
        
        _ = input(f"put this {encrypted} into the chat then press enter")
    else:
        msg = input("input recived message here: ")
        msglist = msg.split(".")
        completemsg = 0
        for i in msglist:
            if(i):
                decrypted = int(i)/shared_secret
                msglength = len(str(decrypted)) - 2
                lengthen = pow(10, msglength)
                completemsg = completemsg * lengthen
                completemsg += int(decrypted)
        fully_decrypted = converter.int2str(int(completemsg), math, split)
        print(fully_decrypted) 

