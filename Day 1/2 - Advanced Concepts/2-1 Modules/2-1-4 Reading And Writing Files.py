# There is a standard function open() which returns a file object, and is most commonly used with
# two arguments: open(filename, mode). Due to the historical (hysterical) use of CRLF (carriage
# return line feed) on Windows for textline endings opening a with the modes ‘r’ causes CRLF to be
# translated to LF, this causes havoc when using binary data files like JPEG or EXE, the data in
# these get corrupted. Text file with BOM (byte order marks) at the front also cause issues. These
# BOM's unfortunately require two kinds of action when reading these files.

# We will just be dealing with UTF8 containing ASCII mostly, here.

f = open('workfile.txt', 'w')
print f
# <open file 'workfile', mode 'w' at ...>

data = '''\
Mary had a little lamb
it's fleece was white a snow
and every where that Mary went
the lamb was sure to go.
'''

f.write(data)
f.close()

import sys
stdout = sys.stdout
stdout.write(data)

f = open('workfile.txt', 'r')
line = f.readline()
stdout.write(line)
# Mary had a little lamb
for line in f:
    stdout.write(line)
# it's fleece was white a snow
# and every where that Mary went
# the lamb was sure to go.
f.close()

f = open('workfile.txt', 'r')
list(f)
# Mary had a little lamb
# it's fleece was white a snow
# and every where that Mary went
# the lamb was sure to go.
f.seek(0)
lines = f.readlines()
for line in lines:
    stdout.write(line)
# Mary had a little lamb
# it's fleece was white a snow
# and every where that Mary went
# the lamb was sure to go.
f.close()

with open('workfile.txt', 'r') as f:
    list(f)
# Mary had a little lamb
# it's fleece was white a snow
# and every where that Mary went
# the lamb was sure to go.
print f.closed
# True

# a little json
import json
f = open('workfile.txt', 'r')
lines = f.readlines()
json.dumps(lines)
f.close()

f = open('workfile.txt', 'w')
json.dump(lines, f)
f.close()

f = open('workfile.txt', 'r')
lines = json.load(f)
f.close()
