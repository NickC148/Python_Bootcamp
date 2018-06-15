### 2-8-8 Data Compression ###
# Common data archiving and compression formats are directly supported by modules including: zlib,
# gzip, bz2, zipfile and tarfile.

import zlib
s = 'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
print len(t)
print zlib.decompress(t)
# 226805979
