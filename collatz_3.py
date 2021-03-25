def collatz (number):
    counter = 0
    if number > 1:
        while number > 1:
            if number % 2 == 0:
                number = number // 2 
                print (number)
                counter += 1
            else:
                number = number * 3 + 1
                print (number)
                counter += 1
        print ('collatz completed in: ' + str(counter) + ' steps')
    else: print(error)

print ('Hello. Enter a number over 1. I will run the collatz sequence on it.')
try:
    collatz(int(input('Number: ')))
except ValueError:
    print ("NAN. bye")
