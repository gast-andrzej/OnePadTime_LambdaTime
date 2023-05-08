OnePadTime = lambda message, key: print(''.join(chr(i) for i in list(map(lambda *i: sum(i), *[list(ord(j) for j in message), list(ord(j) for j in key)]))))
OnePadTime("Hello Friend", "Hello Friend")