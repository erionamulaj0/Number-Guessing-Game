import random
import math

kufiri_poshtem = int(input("Ju lutem shkruani kufirin e poshtëm: "))

kufiri_siperm = int(input("Ju lutem shkruani kufirin e sipërm: "))

x = random.randint(kufiri_poshtem, kufiri_siperm)
print("\n\tJu keni vetëm ",
      round(math.log(kufiri_siperm - kufiri_poshtem + 1, 2)),
      " mundësi të gjeni numrin!\n")

count = 0

while count < math.log(kufiri_siperm - kufiri_poshtem + 1, 2):
    count += 1

    guess = int(input("Hamendësoni një numër: "))

    if x == guess:
        print("Urime ju e gjetët në ",
              count, " provime")
        break
    elif x > guess:
        print("Ju keni hamendësuar numër shumë të vogël!")
    elif x < guess:
        print("Ju keni hamendësuar numër shumë të madh!")

if count >= math.log(kufiri_siperm - kufiri_poshtem + 1, 2):
    print("\nNumri është %d" % x)
    print("\tPaçi fat më të mirë herën tjetër!")
else:
    print("\n Luani përseri!")
