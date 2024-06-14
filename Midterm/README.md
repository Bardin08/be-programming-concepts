## Level 2: Fix the mistakes

Each variant has 6 errors. Each error costs 0.5 points. If student corrected all 6 - he can get up to 3 points

The task contains errors (from 0 to 10) fix the all!

### FooBar

Write a program that prints the numbers from 1 to 100. For multiples of 4, print "Foo" instead of the number, and
for multiples of 6, print "Bar". For numbers which are multiples of both 4 and 6, print "FooBar".

#### Valid Code:

```python
def foo_bar():
    for i in range(1, 101):
        if i % 4 == 0 and i % 6 == 0:
            print("FooBar")
        elif i % 4 == 0:
            print("Foo")
        elif i % 6 == 0:
            print("Bar")
        else:
            print(i)

```

#### Invalid Code:

```python
for i in range(1, 100): # Will generate [1, 99]
    if i // 4 == 0: # Floor division instead of modulo 
        print("Foo")
    elif i % 6 != 0: # '!=' -> '=='
        print("Foo")# 'Foo' instead of 'Bar'
    elif i % 4 == 0 or i % 6 == 0:  # This condition will never be reached.
                                    # Messed up logical operators `or` instead of `and`
        print("FooBar")
    else:
        print(i)
```

### AlphaBeta

Write a program that prints the numbers from 1 to 100. For multiples of 2, print "Alpha" instead of the number, and for
multiples of 3, print "Beta". For numbers which are multiples of both 2 and 3, print "AlphaBeta".

#### Valid Code:

```python
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print("AlphaBeta")
    elif i % 2 == 0:
        print("Alpha")
    elif i % 3 == 0:
        print("Beta")
    else:
        print(i)
```

#### Invalid Code:

```python
for i in range(1, 100): # Will generate [1, 99]
    if i % 2 != 0: # '!=' -> '=='
        print("Alpha")
    elif i // 3 == 0: # Floor division instead of modulo
        print("Beta")
    elif i % 2 == 0 and not i % 3 == 0:  # This condition will never be reached
                                         # Redundant 'not'
        print("BetaAlpha") # 'AlphaBeta' -> 'BetaAlpha'
    else:
        print(i)
```

### DuckQuack

Write a program that prints the numbers from 1 to 100. For multiples of 5, print "Duck" instead of the number, and for
multiples of 9, print "Quack". For numbers which are multiples of both 5 and 9, print "DuckQuack".

#### Valid Code:

```python
for i in range(1, 101):
    if i % 5 == 0 and i % 9 == 0:
        print("DuckQuack")
    elif i % 5 == 0:
        print("Duck")
    elif i % 9 == 0:
        print("Quack")
    else:
        print(i)

```

#### Invalid Code:

```python
for i in range(1, 100): # Will generate [1, 99]
    if i % 5 != 0: # '!=' -> '=='
        print("Duck")
    elif i // 9 == 0: # Floor division instead of modulo
        print("Quack")
    elif not (i % 5 == 0 and i % 9 == 0):  # This condition will never be reached
                                           # Redundant 'not'
        print("DuckQuack")
    else:
        print(i * "Quack") # Invalid output. Expected only number
```

## Level 3: Write the game

1. Define the game board as a 2x3 grid and initialize it with random signs.
2. Display the grid with hidden signs.
3. Handle the user's moves:
   1. Allow the user to input their move by selecting a cell to uncover.
   2. Reveal the sign in the selected cell and display the updated grid.
4. Track the number of moves and check if the user has uncovered two matching signs.
5. Display a win or lose message based on the user's performance.
6. User has 3 attempts to uncover the cell.

