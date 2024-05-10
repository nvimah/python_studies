import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My numer is 415-555-4242.')
print('phone number found: '+ mo.group())
#. matches any character except a new license
#\d - any digit btn 0-9
#\D -Not a digit 0-9
#\w - word charcters a-z A-Z 0-9 _
#\W - not a word character
#\s - white space space, tab, newline
#\S - Not whitespace 

   # word literals
#\b - word boundary
#\B - not a word boundary
#^ - Beginning of a string
#$ - End of a string
#pattern.finditer  - tosearch
#phoneNumRegex = re.compile(r'[89]00\d\d[.-]\d\d\d[.-]\d\d\d\d')
#phoneNumRegex = re.compile(r'[1-5]\d\d-\d\d\d-\d\d\d\d')
#phoneNumRegex = re.compile(r'[^b]at')matches everything except bat


