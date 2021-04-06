def commaCoder(aList):
    listLen = len(aList)
    miniList = aList[0:listLen-1]
    for i in miniList:
        print (i + ', ', end= '')
    print ('and ' + aList[listLen-1])

#Pass any correctly formatted list to commaCoder, and it will worl properly...
#Still working on how to take lists as an input, specifically because user-input...
# ... strings will be separated by character
