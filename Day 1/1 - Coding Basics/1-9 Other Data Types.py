# Sets

amounts = [12.00, 15.12, 12.00, 6.25, 15.12]
values = set(amounts)
print values
#set([6.25, 12.0, 15.12])
print sorted(values)
#[6.25, 12.0, 15.12]

for value in sorted(values):
    print value
# 6.25
# 12.0
# 15.12

petrenella = set('petrenella')
peterson = set('peterson')
print petrenella
#set(['a', 'e', 'l', 'n', 'p', 'r', 't'])
print peterson
#set(['e', 'o', 'n', 'p', 's', 'r', 't'])
print petrenella - peterson
#set(['a', 'l'])
print petrenella | peterson
#set(['a', 'e', 'l', 'o', 'n', 'p', 's', 'r', 't'])
print petrenella & peterson
#set(['p', 'r', 'e', 't', 'n'])
print petrenella ^ peterson
#set(['a', 's', 'l', 'o'])

# List comprehension

a = {x for x in peterson if x not in petrenella}
print a
#set(['s', 'o'])
b = {x for x in peterson if x in petrenella}
print b
#set(['p', 'r', 'e', 't', 'n'])

squares1 = []
for x in range(10):
    squares1.append(x**2)

print squares1
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares2 = [x**2 for x in range(10)]

print squares2
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

combs1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

print combs1
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs2 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs2.append((x, y))

print combs2
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
