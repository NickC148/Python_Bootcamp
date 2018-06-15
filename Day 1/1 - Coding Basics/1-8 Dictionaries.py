# Dictionaries are a (key, value) mapping type. They are denoted by braces (curly brackets.)
# The keys must be unique and can be any immutable type; strings and number are generally used
# but tuples can be keys if the do not contain mutable elements.

course = {'VB6': 'Rory', 'JScript': 'Martin'}
course['C++'] = "Craig"
course['COBOL'] = None
print course
#{'JScript': 'Martin', 'COBOL': None, 'VB6': 'Rory', 'C++': 'Craig'}

print sorted(course)
# ['C++', 'COBOL', 'JScript', 'VB6']

for key in sorted(course):
    print key, course[key]
#C++ Craig
# COBOL None
# JScript Martin
# VB6 Rory

print course.keys()
# ['JScript', 'COBOL', 'VB6', 'C++']

kd = []
for key in course:
    kd.append((key, course[key]))
print kd
#[('JScript', 'Martin'), ('COBOL', None), ('VB6', 'Rory'), ('C++', 'Craig')]

xyz = dict(kd)
print xyz['COBOL']
# None

if 'VB6' in xyz:
    print xyz['VB6']
# Rory
