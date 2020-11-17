def spacer():
    msg = input("Input message to space out: ")
    marr = []
    for a in range(len(msg)):
        marr.append(msg[a])
    final = ' '.join(marr)
    print(final)
    spacer()
spacer()