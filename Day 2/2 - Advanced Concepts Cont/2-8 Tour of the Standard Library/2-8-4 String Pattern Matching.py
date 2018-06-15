### 2-8-4 String Pattern Matching ###
# The re module provides regular expression tools for advanced string processing. For complex matching
# and manipulation, regular expressions offer succinct, optimized solutions. Unfortunately they are
# quite often about as readable as an APL program.

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# When only simple capabilities are needed, string methods are preferred because they are easier to
# read and debug.

'cat in the the hat'.replace('the the', 'the')
