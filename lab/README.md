# ATM System

> My father asked about his ATM card. I didn't know what a loop was. One full day later — this happened.

---

## What I Learned Before This

Already knew if-elif-else, nesting, string methods, and basic input/output. But there was always one problem — the code ran once and stopped. No way to repeat anything.

That changed here. Learned `while` loop — how to make code keep running until a condition is met. Also learned how to use a counter variable to track attempts.

> First time using loops. Everything before this ran once. This runs until you say stop.

---

## What's Inside This?

One project. One new concept. Full day of grinding to make it work.

- **ATM System** — password retry with 3 attempts, restart option

---

# ATM System

User enters a password. If wrong — try again. Only 3 attempts allowed. After 3 wrong tries — option to restart or exit. Correct password — access granted.

## The Story

Didn't know what a loop was. Was trying to understand what repeating means in code. Then my father asked if I had seen his ATM card — and it clicked. ATM machines repeat. Wrong password? Try again. Too many attempts? Locked out. Restart? Start over.

That became the project. Took 4 hours just to understand while. Full day to make the whole thing work.

## How It Works

Two loops — one inside the other. Outer loop handles restart. Inner loop handles the 3 attempts.

**The outer loop:**
```python
restart = "yes"

while restart == "yes":
    attempts = 0
    restart = input("Machine : Do you want to start again? (yes/no): ").lower()
```

**The inner loop:**
```python
while attempts < 3:
    password = int(input("Machine : Enter your password : "))

    if password != real_password:
        attempts = attempts + 1
        print("Machine : Wrong password, try again!")
    else:
        attempts = attempts + 3
        print("Machine : Wait few seconds for your amount!")
```

## The Interesting Part

Look at the correct password case — `attempts = attempts + 3`. That is not the clean way. The clean way would be `break`. But `break` was not known yet.

So instead — jump the counter to 3. Loop condition is `attempts < 3`. Counter hits 3, loop exits. It works!

---

# What Happened Here

First time using loops. Took a whole day. But the idea clicked because of a real ATM machine.

The code is not clean. The +3 hack is funny in hindsight. But it works exactly like a real ATM.

---

> Four hours to understand while. One full day to build this. That is how loops started.
