#read numbers and multiply them

def interact():
    print('Hello stream word')
    while True:
        try:
            reply = input('Enter a number>')
        except EOFError:
            break
        else:
            num = int(reply)
            print("%d squeared is %d" % (num, num ** 2))
        print('Bye')

if __name__ == '__main__':
    interact()
