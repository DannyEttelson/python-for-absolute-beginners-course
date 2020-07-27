
bingo = True

while bingo == True:

    user_num = input('Gimme a number ya schmuck! Just not 0 ')
    num = int(user_num)

    odd_or_even = num % 2

    if num == 0:
        bingo = False
        print("You had to ruin it, didn't you. I'm done!")
        break
    elif odd_or_even == 0:
        print("That's obviously even.")
        print("gimme another one, it better not be zero!")
    else:
        print("That's odd, dummy.")
        print("gimme another one, it better not be zero!")