from word2number import w2n

f = open("reservations")

for reservation in f:
    name, number = reservation.split(",")
    try:
        chairs_per_person = 50 / int(number)
    except ValueError:
        print("Please don't write numbers as text")
    except ZeroDivisionError:
        chairs_per_person = 0

    print("{} will get {} chairs per person".format(name, chairs_per_person))
