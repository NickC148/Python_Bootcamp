words = ['we', 'are', 'words', 'in', 'a', 'list']
for word in words:
    print word, len(word)
    # we 2
    # are 3
    # words 5
    # in 2
    # a 1
    # list 4

for n, word in enumerate(words):
    print n, word
    # 0 we
    # 1 are
    # 2 words
    # 3 in
    # 4 a
    # 5 list

for n, word in enumerate(sorted(words)):
    print n, word
    # 0 a
    # 1 are
    # 2 in
    # 3 list
    # 4 we
    # 5 words

print range(10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in range(len(words)):
    print n, words[n]
    # 0 we
    # 1 are
    # 2 words
    # 3 in
    # 4 a
    # 5 list

for n in range(len(words)):
    if n == 3:
        continue
    if n > 4:
        break
    print n, words[n]
    # 0 we
    # 1 are
    # 2 words
    # 4 a

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'
        continue
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3

for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num
# Found an even number 2
# Found a number 3
# Found an even number 4
# Found a number 5
# Found an even number 6
# Found a number 7
# Found an even number 8
# Found a number 9

i = 0
while i < 4:
    print i,
    i += 1
# 0 1 2 3
