
def findprime(time, math, random, rmin, rmax):
    print("finding prime number for encryption")
    time = time.time()
    time = round(time)
    random.seed(time)
    number = random.randrange(rmin, rmax, 1)
    c = 0
    while(c == 0):
        anwsers = []
        for i in range(2, number-1):
            answer = number/i
            if(answer.is_integer()):
                anwsers.append(answer)      
        if(anwsers == []):
            break
        number += 1
    return number
    
        