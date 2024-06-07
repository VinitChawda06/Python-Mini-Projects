## Define, Call, Pass, Argument, Parameter
The terms define, call, pass, argument, and parameter can be confusing. Let’s look at
a code example to review these terms:
```
➊ def sayHello(name):
print('Hello, ' + name)
➋ sayHello('Al') 
```
To define a function is to create it, just like an assignment statement like spam =
42 creates the spam variable. The def statement defines the sayHello() function ➊.
The sayHello('Al') line ➋ calls the now-created function, sending the execution to
the top of the function’s code. This function call is also known as passing the


## Return Values and return Statements
In general, the value that a function call evaluates to is called the return value of the function.

## Local and Global Scope
Parameters and variables that are assigned in a called function are said to exist in
that function’s local scope. Variables that are assigned outside all functions are said
to exist in the global scope.

