

def strClassifier(givenStr):
    givenStr = givenStr
    subStr = ""
    lists = []
    subStrFirstChar = 0
    

    for i in givenStr:
        for j in range(subStrFirstChar, len(givenStr)):
            subStr += givenStr[j]


            if subStr.count(givenStr[j])>1:
                        lists.append(subStr[:-1])
                        
                        subStrFirstChar+= 1
                        subStr = ""
                        break


    maxi =""
       
    for word in lists:
           
        if len(word)>len(maxi):
            maxi = word
               
    if len(maxi)<3:
        return "-1"
    else:
        return maxi
       
# Driver code
print(strClassifier("character"))
print(strClassifier("standfan"))
print(strClassifier("class"))        

    

    


def main():
    strClassifier("hello")


main()