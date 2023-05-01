a = {'imam': 12345, 'naima': 98765, 'samiul': 564738}
print(a)
print(a['imam'])

a['apon'] = 392837
print(a)

for number in a:
    print(f"keys: {number}, valus: {a[number]}")

for i in a:
    print(i)
    print(a[i])

for l, m in a.items():
    print(f"Keys: {l}, Valus: {m}")

del a['naima']
print(a)

a.clear()
print(a)