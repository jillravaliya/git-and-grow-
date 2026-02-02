# Comparison Calculator + Logical Calculator

> Taking the calculator idea and pushing it way further.

---

## What I Learned Before This

Already knew `if-elif-else`, nesting, `find()`, slicing, `int()`, and operators from the previous projects. Now using all of that together in more complex ways.

The basic calculator taught how to parse one operation. This time — handling comparison operators and even combining multiple comparisons with `and`/`or` logic.

> Still no loops. Still no functions. Just pushing what's already there harder.

---

## What's Inside This?

Two calculators. Same parsing technique, bigger scope.

- **Comparison Calculator** — handles `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Calculator** — handles `and`, `or` with full expressions

---

# Project 1: Comparison Calculator

User types `5>3` and the code returns `True` or `False`. Not math anymore — logic.

## The Problem

The basic calculator handled `+`, `-`, `*`, `/`. But what about comparing values? What if someone wants to check if `5>3` or `10==10`?

Same parsing technique works — find the operator, split, but instead of calculating, compare the values and return True or False.

## How It Works

**Step 1** — `find()` looks for comparison operators. Unlike basic calculator which had single characters, some operators are two characters like `==`, `!=`, `>=`, `<=`.

**Step 2** — once the operator is found, split the string. Everything before the operator is the left value, everything after is the right value.

**Step 3** — convert both to `int()` and compare them. Print `True` or `False`.

So the whole thing looks like this:

```python
calculation = input("What you want to calculate?: ")

if calculation.find("==") != -1:
   value1 = int(calculation[0:calculation.find("==")].strip())
   value2 = int(calculation[calculation.find("==") + 2:].strip())
   print("Your answer is :", value1 == value2)

elif calculation.find("!=") != -1:
   value1 = int(calculation[0:calculation.find("!=")].strip())
   value2 = int(calculation[calculation.find("!=") + 2:].strip())
   print("Your answer is :", value1 != value2)
```

Notice `.strip()` — cleans up extra spaces. And for two-character operators like `==`, skip 2 positions not 1.

Same pattern repeats for `>`, `>=`, `<`, `<=`. Find, split, compare.

## The Interesting Part

The basic calculator returned numbers. This one returns True or False. Same technique, different output. That's the real learning — the parsing logic works for anything, not just math.

---

# Project 2: Logical Calculator

User types `5>3 and 2==2` and the code evaluates BOTH sides, then combines them with `and` or `or` logic.

## The Problem

Comparison calculator handles one comparison. But what if someone wants to combine multiple checks? Like "is 5 greater than 3 AND is 2 equal to 2?"

Now the code has to:
1. Find the logical operator (`and` or `or`)
2. Split the string into LEFT expression and RIGHT expression
3. Evaluate LEFT side (could be any comparison)
4. Evaluate RIGHT side (could be any comparison)
5. Combine both results with `and` or `or`

That's way more complex. But still — no loops, no functions. Just nesting if-elif inside if-elif.

## How It Works

Think of it like this — user types `"5>3 and 2==2"`.

**Step 1** — find `and` in the string. Split at `and` to get two parts: `"5>3"` and `"2==2"`.

**Step 2** — now EACH part needs to be evaluated separately. So for `"5>3"`:
- Check if it has `==`? No.
- Check if it has `!=`? No.
- Check if it has `>=`? No.
- Check if it has `>`? Yes! Evaluate it → `True`.

**Step 3** — same thing for `"2==2"`:
- Check if it has `==`? Yes! Evaluate it → `True`.

**Step 4** — combine both: `True and True` → `True`. Print result.

So the code has nested if-elif blocks:

```python
if "and" in calculation:
    value1 = calculation[:calculation.find("and")].strip()
    value2 = calculation[calculation.find("and") + 3:].strip()
    
    result1 = False
    result2 = False
    
    # Evaluate LEFT side
    if "==" in value1:
        a = value1[:value1.find("==")].strip()
        b = value1[value1.find("==") + 2:].strip()
        result1 = a == b
    elif "!=" in value1:
        # ... same pattern for all operators
    
    # Evaluate RIGHT side
    if "==" in value2:
        a = value2[:value2.find("==")].strip()
        b = value2[value2.find("==") + 2:].strip()
        result2 = a == b
    elif "!=" in value2:
        # ... same pattern for all operators
    
    # Combine results
    result = result1 and result2
    print("Your answer is:", result)
```

Same logic repeats for `or` instead of `and`.

## The Grind

Look at the code — it's LONG. Repetitive. The same if-elif pattern for checking operators repeats for the left side, then again for the right side, then again for `or` logic.

This is what happens when you don't know loops or functions yet. You just write it all out manually. Every single case. Every single check.

It works. It's not clean. But it works.

---

# What Happened Here

Comparison Calculator taught that the same parsing technique works for logic, not just math. Logical Calculator taught that you can handle complex expressions by breaking them into parts and evaluating each part separately.

The code got way longer. The nesting got deeper. But the core idea stayed the same — find, split, evaluate.

---

> Same tools. Bigger problems. Still made it work. That's the pattern.
