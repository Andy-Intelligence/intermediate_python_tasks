import random


def pwGen():
    lists = []
    for i in range(4):
        randomdigit = random.randrange(0,9)
        lists.append(randomdigit)

    return lists

def userguess():
    glists = []
    for i in range(4):
        guess = int(input(" Enter your four digit code here: "))
        glists.append(guess)

    return glists 




def comparator(lists,glists):
    anslist = []
    B = "B"  #If any digit out of the guessed four-digit code is wrong, the computer should print out “B”
    R = "R"  # If the digit is correct but at the wrong place, the computer should print “Y”
    Y = "Y"  # If the digit is correct but at the wrong place, the computer should print “Y”


    for i in range(len(glists)):
        if glists[i] == lists[i]:
            anslist.append(R)


        # elif glists.count(lists[i])>0:
        #     anslist.append(Y)

        elif glists[i] in lists:
            anslist.append(Y)


        elif glists[i] != lists[i]:
            anslist.append(B)

        else:
            print("something is wrong with the program please contact the developer")
            exit(1)

    return anslist 


def main():
    lists =pwGen()
    print(lists)
    for _ in range(10):        
        glists = userguess()
        anslist = comparator(lists=lists, glists=glists)
        print(anslist)
        if glists == lists:
            print("Welldone you are right!!! ", glists)
            exit(1)


main()