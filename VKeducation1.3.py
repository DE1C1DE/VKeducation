valid, g1, g2 = True, int(input()), int(input())
while True:
    g3 = input()
    if g3 == '':
        break
    valid &= g1 <= int(g3) <= g2
print(valid)