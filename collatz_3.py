def collatz(number):
    if number > 1:
        steps = 0
        while number != 1:
            if number % 2 == 0:
                print (int(number//2))
                number = number/2
                steps += 1
            else:
                print (int(number*3+1))
                number = number * 3 + 1
                steps += 1
        print('collatz finished in ' + str(steps) + ' steps')
    else:
        print ('I quit')

try:
    collatz(int(input('choose any integer greater than 1: ')))
except ValueError:
    print('non-int, try again')
