import random

def r():
     return random.randrange(0,121,10)

def main():
    count = 0
    while ( count != 100 ):
        count += 1
        print(r())

main()
