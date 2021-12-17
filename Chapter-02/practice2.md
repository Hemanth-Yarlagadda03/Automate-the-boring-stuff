# Practice Questions

### 1. What are the two values of the Boolean data type? How do you write them?
True and False resp

### 2. What are the three Boolean operators?
'And','or' and 'not'

### 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
for 'and'- TT--T;TF--F;FF-F,FT--F</br>
for 'or'- TT--T,TF--T,FT--T,FF-F</br>
for 'not' T--F,F--T

### 4. What do the following expressions evaluate to?

(5 > 4) and (3 == 5) ---False
not (5 > 4) ---False
(5 > 4) or (3 == 5) ---True
not ((5 > 4) or (3 == 5)) ---False
(True and True) and (True == False) --- False
(not False) or (not True) --- True

### 5. What are the six comparison operators?
<,>,>=,<=,==,!=,==

### 6. What is the difference between the equal to operator and the assignment operator?
equal to operator checks for equality bw two values while assignment operator assigns a value to a varibale.

### 7. Explain what a condition is and where you would use one.
Condition is an expression which decides which branch is to be executed.

### 8. Identify the three blocks in this code:

spam = 0 ---1
if spam == 10:----2
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')---3

### 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
check the py files
### 10. What keys can you press if your program is stuck in an infinite loop?
 CTRL-C

### 11. What is the difference between break and continue?
The break statement move the execution outside while the continue statement moves the execution to the start of the loop.

### 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
i. Iterates 11 times from 0 to 10
ii.does the same thing
iii.does the same thing 

### 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
check the py files

### 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()
