import keyboard

pw = []
num_pw = []
unlock_pw = [3]
print ("start key")

while True:
    pw.append(keyboard.read_key())

    if "enter" in pw:
        pw.remove("enter")

    print (pw)

    if keyboard.read_key() == "enter":
        print("enter")
        for num in pw:
            try:
                num_pw.append(int(num))
            except ValueError:
                num_pw = []

        status = open('./lock.status', 'r')
        lock_status = status.read()
        status.close()

        if num_pw == unlock_pw:
            print("pw_open")
            status = open('./lock.status', 'w')
            status.write('open-close')
            status.close()

        elif num_pw != unlock_pw and lock_status != "=close":
            print ("pw_close")
            status = open('./lock.status', 'w')
            status.write('=close')
            status.close()

        num_pw = []
        pw = []