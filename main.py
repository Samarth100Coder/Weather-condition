temp=int(input('Enter the temperature in celsius: '))

def weather(t):
    if t>23:
        print('Its hot')
    else:
        print('Its cold')

weather(temp)