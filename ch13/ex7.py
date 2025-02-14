#(Regular expression example to search for words starting with f)
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')) #\b is backspace
print('tea for too'.replace('too', 'two'))
# print(dir(re))