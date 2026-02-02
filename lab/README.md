# First Projects — Where It All Started

> First projects. Where the coding journey actually started.

---

## What I Learned Before This 

**The basics first** — `print()`, `input()`, variables, data types, and `type()`. How to show things, take input, and store values.

**Then strings and operators** — how `find()` locates something inside a string, how slicing cuts it into pieces, how to do math and compare values. And `int()` to convert input into actual numbers.

**And finally, decisions** — `if-elif-else`. How to make the code choose a path. And nesting — putting an `if` inside another `if`.

Didn't feel like much at the time. But turns out — that's all you need to build real things.

> No loops. No functions. No lists yet. Everything here is built with just what was learned so far.

---

## What's Inside This?

Two projects. Just brute force thinking and making it work.

- **Grade Checker** — nested if-elif-else
- **Basic Calculator** — string parsing with find() and slicing

---

# Project 1: Grade Checker

> Given a percentage, print the grade. Simple right? Not when you need A AND A+ to print together!

## The Problem

If someone scores 97, they deserve both "Grade A" and "Grade A+". But normally if-elif only prints ONE thing. So how do you make both print?

**Answer — nesting!** Put another if INSIDE the first if. Didn't know loops or functions at this point, so nesting was the way to make it work.

## How It Works

```python
if percentage >= 90:
    print("Grade : A")
    if percentage > 95:          # nested inside!
        print("Grade : A+")     # both print together!
```

So when percentage is 97 — it hits the `>= 90` check first, prints A. Then INSIDE that same block it checks `> 95`, prints A+ too. Both grades show up at the same time!

Without nesting this whole thing breaks. The ORDER of checks matters, and nesting lets you go deeper without losing the outer result.

---

# Project 2: Basic Calculator

> User types `5+3` as ONE single string. The code has to find the operator, split the numbers apart, and calculate — all by itself!

## The Problem

Most people would just ask for two numbers and an operator separately. But this calculator takes everything in ONE input like `12+25` or `10-3`. So the code has to be smart enough to break it apart on its own.

## How It Works

Think of it like this — user types `"12+25"`. This is ONE string, not two numbers. So the code has to figure everything out on its own.

**Step 1** — `find("+")` looks inside the string and says "yes, `+` is sitting at position 2!" If the operator wasn't there, it would return -1. That's how the code knows which operation to do.

**Step 2** — now it knows where `+` is. So it cuts the string into two parts. Everything before position 2 is `"12"`. Everything after is `"25"`.

**Step 3** — convert both into real numbers with `int()` and do the math. Done!

So the whole thing in one shot looks like this:

```python
calculation = input("What you want to calculate?:")

if calculation.find("+") != -1:
   value1 = int(calculation[0:calculation.find("+")])      # "12" → 12
   value2 = int(calculation[calculation.find("+") + 1:])   # "25" → 25
   print("Your answer is :", value1 + value2)              # 37!
```

Same exact thing repeats for `-`, `*`, `/`. Find the operator, cut, calculate.

---

## The Interesting Part 

The whole calculator works with just ONE concept — find where the operator is, cut the string there, do the math. Just `find()` and slicing used again and again.

That's the grind. Making something work with whatever you know at that moment, even if it's not the "clean" way.

---

## What Happened Here !

Grade Checker taught that nesting matters and order of checks matters. Calculator taught that `find()` and slicing can do more than you'd expect — you can actually parse real expressions with just those two things.

Didn't know the "right way" to do any of this. Didn't care. Made it work anyway.

---

> Two projects. Same tools. Same grind. But something clicked here — you don't need everything to build something real. You just need to push what you already have.
