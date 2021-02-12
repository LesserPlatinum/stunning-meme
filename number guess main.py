# program to choose a number and allow player to guess

print("Can you guess the number I choose? But first how good are you fortune telling skills?"
      "(N)ormal (L)ucky (O)ricalesk (G)odly")
difficulty = str(input())  # input for difficulty
for set_range in range(1):
    if difficulty.lower()[0] == "n":
        x = randint(1, 10)
        q = 10
    elif difficulty.lower()[0] == "l":
        x = randint(1, 100)
        q = 100
    elif difficulty.lower()[0] == "o":
        x = randint(1, 1000)
        q = 1000
    else:
        x = randint(1, 10000)
        q = 10000

print("Beep Boop. What number am I thinking of between 1 and " + str(q) + "?")
y = int(input())


def attempt():  # 3 guessing attempts using
    for test in range(2):
        if x != y:
            print("Nope")
            y = int(input())
        else:
            print("No you beat me! It was " + str(x))
            break


def hints():  # guess hints
    hint_type = randint(1, 3)
    a = "Nope. Have a hint "
    if x == y:
        pass
    else:
        if hint_type == 1:
            if y > 1 and y % 2 == 0:
                print(a + "it's even.")
            else:
                print(a + "it's odd.")
        elif hint_type == 2:
            if y > 2 and y % 3 == 0:
                print(a + "it's divisible by 3.")
            else:
                print(a + "it's not divisible by 3.")
        else:
            if y > 1:  # check prime
                for i in range(2, y):
                    if (y % i) == 0:
                        print(a + "it's not prime.")
                        break
                    else:
                        print(a + "it's prime.")
                        break
    y = int(input())


attempt()
hints()
attempt()
if x != y:  # game over statement
    print("Har Har Har, I win. It was " + str(x))
