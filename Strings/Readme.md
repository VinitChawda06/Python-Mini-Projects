- isalpha() Returns True if the string consists only of letters and isn’t blank
- isalnum() Returns True if the string consists only of letters and numbers and is not blank
- isdecimal() Returns True if the string consists only of numeric characters and is not blank
- isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
- istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by
- only lowercase letters

```
>> spam = 'Hello, world!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>> 'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
```

## The startswith() and endswith() Methods
```
>>> 'Hello, world!'.startswith('Hello')
True
>>> 'Hello, world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello, world!'.startswith('Hello, world!')
True
>>> 'Hello, world!'.endswith('Hello, world!')
True
```
## The join() and split() Methods
```
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'

>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

## Splitting Strings with the partition() Method

```
>>> 'Hello, world!'.partition('w')
('Hello, ', 'w', 'orld!')
>>> 'Hello, world!'.partition('world')
('Hello, ', 'world', '!')
>>> before, sep, after = 'Hello, world!'.partition(' ')
>>> before
'Hello,'
>>> after
'world!'
```
## Justifying Text with the rjust(), ljust(), and center() Methods
```
>>> 'Hello'.rjust(10)
'         Hello'
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
>>> 'Hello'.center(20)
'
Hello
'
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

## Removing Whitespace with the strip(), rstrip(), and lstrip() Methods
```
>>> spam = '        Hello, World        '
>>> spam.strip()
'Hello, World'
>>> spam.lstrip()
'Hello, World       '
>>> spam.rstrip()
'       Hello, World'
```