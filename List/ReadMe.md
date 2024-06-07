# The List Data Type
A list is a value that contains multiple values in an ordered sequence.

* ### Slicing 
Just as an index can get a single value from a list, a slice can get several values from a list, in the form of a new list.

* ### len() Function
The len() function will return the number of values that are in a list value passed to it, just like it can count
the number of characters in a string value.

* ### List Concatenation and List Replication
Lists can be concatenated and replicated just like strings. The + operator combines two lists to create a new
list value and the * operator can be used with a list and an integer value to replicate the list.
```
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam
[1, 2, 3, 'A', 'B', 'C']
```

* ### del Statements
The del statement will delete values at an index in a list. All of the values in the list after the deleted value
will be moved up one index.
 ```
 spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
```

* ### The Multiple Assignment Trick
The multiple assignment trick (technically called tuple unpacking) is a shortcut that lets you assign multiple
variables with the values in a list in one line of code.

Example:
```
>>> cat = ['fat', 'gray', 'loud']
>>> size, color, disposition = cat
```

* ### enumerate() Function
enumerate() will return
two values: the index of the item in the list, and the item in the list itself.

``` 
>>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
>>> for index, item in enumerate(supplies):
...
print('Index ' + str(index) + ' in supplies is: ' + item)
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
```

## Methods
- ***index() Method***
```
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
```

- ***append() and insert()***

The insert() method can
insert a value at any index in the list.

``` 
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']
```
- ***remove() Method***

The remove() method is passed the value to be removed from the list it is called on

```
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
```
- ***sort() Method***

```
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']


>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
```

- ***reverse() Method***
```
>>> spam = ['cat', 'dog', 'moose']
>>> spam.reverse()
>>> spam
['moose', 'dog', 'cat']
```

