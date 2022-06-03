# **PythonNotes**

Line spacing and blank spaces in python (editor) will not affect the output except for the spaces in the print statement.

---

## **Comments**

Comments are used as in-code documentation to enhance code readability. 

| Syntax | Description |
| :---: | :--- |
| `#` | To start a single-line comment. |
| `'''` | To start a multi-line comment. |

Sample Code:

```py
# This is a single-line comment

'''
This is a 
multi-line
comment
'''
```

---

## **Input**

Gets input value from user and store in a variable. The general syntax is:

```py
variable_name = input("Prompt Message")
```

`=` is known as an assignment operator. It enables us to store a value into a variable by assigning it.

Sample Code:

```py
name = input("Enter a name: ");
```

By default, `input()` receive data  value in string datatype.  

---

## **Output**

`print()` is used to display the values into the terminal. 

Sample Code:

```py
print("This message will be printed out.") 

# Output: This message will be printed out.
```

---

## **Data Types**

Below are some syntax to convert value into a specific data type.

| Syntax | Description |
| :---: | :--- |
| `int()` | Converts the value into *integer*. |
| `float()` | Converts the value into *float* (number with decimals). |
| `str()` | Converts the value into *string*. |

Sample Code:

```py
five = int(5)
PI = float(3.141592653)
text = str("Cheah Zixu is good in JavaScript")
```

There are certain syntax that can be used to **concatenate** values of different data types into a single *string*.

| Syntax | Description |
| :---: | :--- |
| `%d` | Represents *integer* value to be concatenated into *strings*. |
| `%f` | Represents *float* value to be concatenated into *strings*. |
| `%s` | Represents *string* value to be concatenated into *strings*. |

Sample Code:

```py
name = "Cheah Zixu"
born = 2003

print("My name is %s. I born on %d." % (name, born))

# Output: My name is Cheah Zixu. I born on 2003.
```

Formatting *float* to a certain number of decimal points:

```py
total_price = 7.0
month = 3

price_per_month = total_price / month

print("The payment for one month is RM%.2f" % price_per_month)  # Prints the float value to 2 decimal places.
```

Printing *strings* to the same line:

```py
print("Cheah Zixu ", end = " ")
print("is ", end = "good in ")
print("JavaScript.")

# Output: Cheah Zixu is good in JavaScript.
```

To break the line in a *string*, we can use `\n`.

Sample Code:

```py
print("This is line 1\nThis is line2\nThis is line3")

'''
Output: This is line 1
        This is line 2
        This is line 3
'''
```

There are some functions associated to *strings* that can be useful:

| Syntax | Description |
| :---: | :--- |
| `.upper()` | Converts all characters in the *string* to uppercase character(s). |
| `.lower()` | Converts all characters in the *string* to lowercase character(s). |
| `.isdigit()` | Checks the *string*'s input value and return *Boolean* (`True`) if it contains only number(s). |
| `.isalpha()` | Checks the *string*'s input value and return *Boolean* (`True`) if it contains only letter(s). |

Sample Code:

```py
name_normal = "Cheah Zixu"

print(name_normal.upper())      # Output: CHEAH ZIXU
print(name_normal.lower())      # Output: cheah zixu

print(name_normal.isdigit())    # Output: False
print(name_normal.isalpha())    # Output: False
```

The reason that `name_normal.isalpha()` returns `False` is because the *string* contains whitespace, which is not counted as an alphabet. If the *string* is `"CheahZixu"`, then it will return `True`.

---

## **If-Else**

There are 3 general `if` syntax:

* Simple `if`
* Multi-Way `if`
* Nested `if`

### **Simple If Syntax**

The general syntax is:

```py
if(condition_or_expression):
    # statement(s)
else:
    # statement(s)
```

Flowchart View:

![simple_if](https://serve.zixucheah331.ml/static/simple-if.png)

Sample Code:

```py
if(a > b):
    print("a is larger than b")
else:
    print("b is larger than a")
```

### **Multi-Way If Syntax**

The general syntax is:

```py
if(condition_or_expression):
    # statement(s)
elif(condition_or_expression):
    # statement(s)
else:
    # statement(s)
```

Flowchart View:

![multiway_if](https://serve.zixucheah331.ml/static/multiway-if.png)

Sample Code:

```py
if(marks > 80):
    grade = 'A'
elif(marks > 70):
    grade = 'B'
elif(marks > 60):
    grade = 'C'
else:
    grade = 'F'
```

### **Nested If Syntax**

The general syntax is:

```py
if(condition_or_expression):
    if(condition_or_expression):
    	# statement(s)
    else:
    	# statement(s)
else:
    # statement(s)
```

Flowchart View:

![nested_if](https://serve.zixucheah331.ml/static/nested-if.png)

Sample Code:

```py
if(is_raining):                 # Assume is_raining stores a boolean value
    if(have_umbrella):          # Assume have_umbrella stores a boolean value
        print("Go Shopping!")
    else:
        print("Stay Home!")
else:
    print("Go Out and Play!")
```

---

## **Loops**

Generally, there are two main types of loops:

* Counter-Controlled Repetition / Loop
* Sentinel-Controlled Repetition / Loop

**Sentinel** is a value to stop the loop / repetition. It is **NOT** a limit.

The two loops commonly used are `while` loop and `for` loop.

### **While Loop**

The general syntax is:

```py
while(loop_condition):
    # statement(s)
```

Flowchart View:

![while_loop](https://serve.zixucheah331.ml/static/while-loop.png)

Sample Code:

```py
guess = input("Enter a number: ")

while(guess != 331):
    print("You guessed the wrong number, try again!")
    guess = input("Enter a number: ")

print("Congratulations, you guessed it correctly!")
```

### **For Loop**

There are 3 general syntax:

1. This loop starts counting from `i = 0` to `i < a` with an update of `i += 1` every round.

    ```py
    for i in range(a):
        # Statements
    ```

    Flowchart View:

    ![for_loop1](https://serve.zixucheah331.ml/static/for-loop-1.png)

2. This loop starts counting from `i = a` to `i < b` with an update of `i += 1` every round.

    ```py
    for i in range(a, b):
        # Statements
    ```
    
    Flowchart View:

    ![for_loop2](https://serve.zixucheah331.ml/static/for-loop-2.png)

3. This loop starts counting from `i = a` to `i < b` with an update of `i += k` every round.

    ```py
    for i in range(a, b, k):
        # Statements
    ```
    
    Flowchart View:

    ![for_loop3](https://serve.zixucheah331.ml/static/for-loop-3.png)

---

## **Lists**

Lists are arrays.

The general syntax to create a list is:

```py
list_name = [data1, data2, data3, ...]
```

Sample Code:

```py
blank_list = []
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random_list = ["Cheah Zixu", 331, 'Genesis', True]
```

The `.append()` function allows us to add more data into our lists. 

Sample Code:

```py
mastered_lang = ['JavaScript', 'ReactJS', 'CSS', 'HTML', 'Flutter']

mastered_lang.append("Python")

print(mastered_lang)

# Output: ['JavaScript', 'ReactJS', 'CSS', 'HTML', 'Flutter', Python']
```

The `sum()` function allows us to add up all data in our list.

Sample Code:

```py
numbered_list = [1, 2, 3, 4, 5, 1, 4, 5]

total = sum(numbered_list)

print(total)

# Output: 25
```

To combine all data into a string separated by a special character, we use `sep = 'separator'`.

Sample Code:

```py
dir = ['https://github.com', 'genesis331', 'pikaspace-app', 'android', 'app', 'src', 'main', 'java', 'com', 'pikaspaceapp', 'MainApplication.java']

print(*dir, sep = '/')

# Output: https://github.com/genesis331/pikaspace-app/android/app/src/main/java/com/pikaspaceapp/MainApplication.java
```

---

## **Functions**

To define a function, we use the `def` keyword. The general syntax of function is: 

```py
def function_name(parameter):
```

We can put as much parameters as we want for the function, we can leave it empty as well.

To call a function, we will just write the function name itself along with the parentheses. 

Sample Code:

```py
def say_hello():            # Defines a function
    print("Hello World!")   

say_hello()                 # Calls the function
```

There are two types of functions: **value-returning** function and **non-returning** function. 

For **value-returning function**, we will use the keyword `return` to return the value to the variable that called the function. The general syntax for value-returning function is:

```py
def function_name(parameter):
    # Code lines
    return variable
```

Sample Code:

```py
def get_max(num1, num2):
    if(num1 >= num2):
        return num1
    else:
        return num2

larger_number = get_max(3, 7)
```

The numbers 3 and 7 are known as arguments. They are passed into the parameters of the `get_max` function.

---

## **Using Modules**

The `import` keyword is used to import modules or functions. The general syntax is: 

```py
from module_name import function_name
```

---
