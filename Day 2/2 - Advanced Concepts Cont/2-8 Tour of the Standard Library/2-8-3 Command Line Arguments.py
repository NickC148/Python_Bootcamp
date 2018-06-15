### 2-8-3 Command Line Arguments ###
# Common utility scripts often need to process command line arguments. These arguments are stored
# in the sys module’s argv attribute as a list. Starting python with extra arguments,
# say python - this is more than one. There are many treasures im module sys, for example stdout
# or stderr could be used for writing info or errors. You could even use the dread exit to terminate
# the session. In programs running using exception handling, exit is generally to be avoided.

import sys
print sys.argv
sys.stdout.write('info\n')
sys.stderr.write('error\n')
sys.exit(1)
