## Elements of Flow Control
- Flow control statements often start with a part called the condition and are always followed by a block of code
called the clause.

## Flow Control Statements
#### if Statements
 The most common type of flow control statement is the if statement. An if statement’s clause (that is, the
block following the if statement) will execute if the statement’s condition is True. The clause is skipped if the
condition is False. 


#### else Statements
An if clause can optionally be followed by an else statement. The else clause is executed only when the if
statement’s condition is False.

#### elif Statements
While only one of the if or else clauses will execute, you may have a case where you want one of many
possible clauses to execute. The elif statement is an “else if” statement that always follows an if or another
elif statement.

#### while Loop Statements
The code in a while clause
will be executed as long as the while statement’s condition is True.

#### break Statements
There is a shortcut to getting the program execution to break out of a while loop’s clause early. If the
execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement
simply contains the break keyword.

#### continue Statements
Like break statements, continue statements are used inside loops. When the program execution reaches a
continue statement, the program execution immediately jumps back to the start of the loop and reevaluates
the loop’s condition.

#### for Loops and the range() Function
The while loop keeps looping while its condition is True (which is the reason for its name), but what if you
want to execute a block of code only a certain number of times? You can do this with a for loop statement
and the ``` range(start, stop, step) ``` function.

