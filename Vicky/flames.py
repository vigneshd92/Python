
def flamesMatch(x,y):

    he=x
    she=y
    str="FLAMES"
    dtnryHe=dict()
    dtnrySHe=dict()
    commonDtnry=dict()
    j = 0
    i = 0

# Logic to determine the count of
# remaining letters after eliminating the common characters

    for char in he:
        if char not in dtnryHe:
            dtnryHe.update({char:he.count(char)})
            i += 1
    print(dtnryHe)

    for char in she:
        if char not in dtnrySHe:
             dtnrySHe.update({char : she.count(char)})
             j += 1
    print(dtnrySHe)

    def charToBeDeleted():
        for keyz in dtnryHe:
            if keyz in dtnrySHe:
                commonDtnry.update({keyz:min(dtnryHe[keyz],dtnrySHe[keyz])})
    charToBeDeleted()

    print("common character are: ",commonDtnry)
    for char in commonDtnry:
        he=he.replace(char,'',commonDtnry[char])
        she=she.replace(char,'',commonDtnry[char])

    print('finally...: ',he,end=' ')
    print(she)

    # FLAMES Logic
    Rem=len(he)+len(she) #input to be cleaned
    print(Rem)

    for i in range(len(str),1,-1):
        print("i is :", i)
        print("Before:", str)
        print("char to be deleted: ",Rem % i )
        if (Rem % i ==0):
            str=str.replace(str[(Rem%i-1)],'')
            print("END:", str)
            print('\n')
        else:
            #print(str.replace(str[Rem%i-1],''))
            str=str.replace(str[(Rem%i-1)],'')
            print("After :", str)
            str= str[(Rem%i-1):]+str[:(Rem%i-1)]
            print ("END:",str)
            print('\n')


flamesMatch("mukund","sandhya ")

