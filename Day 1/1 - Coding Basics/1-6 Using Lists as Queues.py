# It is also possible to use a list as a queue, where the first element added is he first element
# retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While
# appends and pops from the end of list are fast, doing inserts or pops from the beginning of a
# list is slow (because all of the other elements have to be shifted by one).

# To implement a queue, use collections.deque which was designed to have fast appends and pops
# from both ends. For example:

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print queue.popleft()           # The first to arrive now leaves
# 'Eric'
print queue.popleft()           # The second to arrive now leaves
# 'John'
print queue                     # Remaining queue in order of arrival
#deque(['Michael', 'Terry', 'Graham'])
