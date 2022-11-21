tt = int(input("Tors tid ? "))
mt = int(input("Mors tid ? "))

carrots = 40

t, m = 0, 0
i = 0
while carrots > 0:
    if carrots == 1 and i % tt == 0 and i % mt == 0:
        break
    if i % tt == 0:
        t += 1
        carrots -= 1
    if i % mt == 0:
        m += 1
        carrots -= 1
    i += 1

print(f"Svar: Tor {t}, Mor {m}")
