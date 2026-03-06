correct_pin = input()

for i in range(3):
    pin = input()
    if pin == correct_pin:
        print("ACCESS GRANTED")
        break
else:
    print("LOCKED")