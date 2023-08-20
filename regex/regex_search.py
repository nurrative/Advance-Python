import re

s = 'egg000ham'

zeros = re.search('000', s)

# if zeros:
#     print("Match")
#
# else:
#     print("No Match")

# print(re.search('[0-9][0-9][0-9]', 'egg000ham')) #<re.Match object; span=(3, 6), match='000'>

# print(re.search('[0-9][0-9][0-9]', '000eggham')) #<re.Match object; span=(0, 3), match='000'>

# print(re.search('[0-9][0-9][0-9]', '00eggham0')) #None

print(re.search('0.0', s)) #<re.Match object; span=(3, 6), match='000'>

s = '00eggham'

print(re.search('0.', s)) #<re.Match object; span=(0, 2), match='00'>

### []


print(re.search('co[dn]e', 'avecoder')) #<re.Match object; span=(3, 7), match='code'>

print(re.search('co[dn]e', 'cones')) #<re.Match object; span=(0, 4), match='cone'>

print(re.search('[a-z]', 'avecoder')) #<re.Match object; span=(0, 1), match='a'>

print(re.search('[A-Z]', 'avecoder')) #None

print(re.search('[0-9]', '000avecoder')) #<re.Match object; span=(0, 1), match='0'>

### ^ - ищет что не находится в этом диапозоне

print(re.search('[^0-9]', '000avecoder')) #<re.Match object; span=(3, 4), match='a'>

### - поиск самого символа дефиса (не диапозон)

print(re.search('[-ave]', '000-ave')) #<re.Match object; span=(3, 4), match='-'>

print(re.search('[ave-]', '000-ave')) #<re.Match object; span=(3, 4), match='-'>

print(re.search('[a\-ve]', '000-ave')) #<re.Match object; span=(3, 4), match='-'>

###  ] - поиск квадратной скобки

print(re.search('[]]', 'ave :]')) #<re.Match object; span=(5, 6), match=']'>

print(re.search('[\]]', 'ave :]')) #<re.Match object; span=(5, 6), match=']'>

### (.)

print(re.search('av.coder', 'avecoder')) #<re.Match object; span=(0, 8), match='avecoder'>

print(re.search('ave.coder', 'avecoder')) #None

### \w == [a-zA-Z0-9_]
print(re.search('\w', 'avecoder')) #<re.Match object; span=(0, 1), match='a'>

print(re.search('\w', '.v-#?]|[')) #<re.Match object; span=(1, 2), match='v'>

### \W != [a-zA-Z0-9_]

print(re.search('\W', '.v-#?]|[')) #<re.Match object; span=(0, 1), match='.'>

print(re.search('\W', 'a*coder')) #<re.Match object; span=(1, 2), match='*'>

### \d - поиск чисел

print(re.search('\d', 'av3coder')) #<re.Match object; span=(2, 3), match='3'>

### \D - поиск не чисел

print(re.search('\D', '1234567O')) #<re.Match object; span=(7, 8), match='O'>

### \s - поиск пробелов и перенос строки

print(re.search('\s', 'ave coder')) #<re.Match object; span=(3, 4), match=' '>

### \S - поиск не пробелов и переноса строки

print(re.search('\S', '          |        ')) #<re.Match object; span=(10, 11), match='|'>

###
print(re.search('[\d\w\s]', '------0------')) #<re.Match object; span=(6, 7), match='0'>
###

### \

print(re.search('.', 'avecoder.com')) #<re.Match object; span=(0, 1), match='a'>

print(re.search('\.', 'avecoder.com')) #<re.Match object; span=(8, 9), match='.'>

rs = r'directory\folder'

# print(re.search('\\', rs)) #Error

# print(re.search(r'\', rs)) #Error

print(re.search(r'\\', rs)) #<re.Match object; span=(9, 10), match='\\'>

print(re.search('\\\\', rs)) #<re.Match object; span=(9, 10), match='\\'>
