# Log File Parser

> Heard about automation with Python. Tried it myself with what I knew.

---

## What I Learned Before This

Already knew strings, `if-elif-else`, operators, and `input()` from the previous projects. This time — learned three new string methods: `.split()`, `.replace()`, and `.endswith()`. Also learned f-strings for cleaner output.

These small tools opened up automation. `.split()` breaks strings into pieces. `.replace()` swaps text. `.endswith()` checks file types. That's enough to parse structured data.

> Still no loops. Still no functions. Just discovered new tools and used them.

---

## What's Inside This?

One script with two parts. First part shows the new string methods. Second part uses them to automate log file parsing.

- **String Methods Demo** — f-strings, `.split()`, `.replace()`
- **Log File Parser** — automatic parsing using `.split()` and indexing

---

# The Script

Two sections that build on each other. First shows what the tools do, then uses them for real automation.

## Part 1: String Methods Demo

Shows f-strings for formatted output, `.split()` to break comma-separated hobbies into a list, and `.replace()` to swap words.

```python
name = "jill"
age = 21
work = "Engineer"
hobby = "music,photography,coding"
pursuits = hobby.split(",")
routine = "programming"
daily_routine = routine.replace("programming", "coding")

print(f"Hi, my name is {name}, my age is {age}, and i work as an {work}")
print("My hobbies are basically ", pursuits)
print(f"But believe me my mostly time goes in {daily_routine} !\n")
```

**What happens:**
- `hobby.split(",")` breaks `"music,photography,coding"` into `['music', 'photography', 'coding']`
- `routine.replace("programming", "coding")` changes the word
- f-strings make printing clean: `f"Hi, my name is {name}"` instead of string concatenation

Simple demo. But it shows the tools work.

## Part 2: Log File Parser

User pastes a log file line like `-rw-r----- 1 root admin 7349974 24 Jan 17:51 wifi.log` and the code automatically extracts every piece — permissions, owner, group, size, date, time, filename.

### The Problem

Log files have structured data — all in one line, separated by spaces. Reading it manually is annoying. What if the code could automatically break it apart?

That's automation. Not with loops or complex logic. Just with `.split()` and knowing where each piece sits.

### How It Works

**Step 1** — check the file type using `.endswith()`:

```python
filename = input("Paste here your files, i will ask you type ! : \n").strip().lower()

if filename.endswith(".txt"):
    print("These is a text file !\n")
elif filename.endswith(".log"):
    print("These is a log file !\n")
else:
    print("These filetype is unknown!")
```

**Step 2** — `.split()` breaks the string at every space and puts the pieces into a list:

```python
your_data = filename.split()
# Input: "-rw-r----- 1 root admin 7349974 24 Jan 17:51 wifi.log"
# Result: ['-rw-r-----', '1', 'root', 'admin', '7349974', '24', 'Jan', '17:51', 'wifi.log']
```

**Step 3** — each piece has a position (index). Position 0 is permissions, position 2 is owner, position 4 is size, etc. Just grab them:

```python
permissions = your_data[0]   # '-rw-r-----'
hard_links = your_data[1]    # '1'
owner = your_data[2]         # 'root'
group = your_data[3]         # 'admin'
size = your_data[4]          # '7349974'
date = your_data[5]          # '24'
month = your_data[6]         # 'Jan'
time = your_data[7]          # '17:51'
filename = your_data[8]      # 'wifi.log'

print("Your permissions are : ", permissions)
print("Your hard_links are : ", hard_links)
# ... and so on for each piece
```

Done. Automated parsing without loops or functions.

### The Discovery

The interesting part — this is automation. Not with fancy libraries or complex code. Just with `.split()` and knowing the structure.

Log files are always formatted the same way. Permissions first, then owner, then group, etc. So you don't need to search or parse intelligently. Just split at spaces and grab by position.

That's the small discovery. Automation doesn't always need loops or functions. Sometimes it just needs understanding the pattern.

---

# What Happened Here

Heard about automation with Python. Didn't know loops or functions yet. But found `.split()`, `.replace()`, `.endswith()`, and f-strings. That was enough to build something that automatically parses structured text.

Small project. But the idea clicked — if data has a pattern, you can automate it with simple tools.

---

> Automation doesn't need to be complex. It just needs to work.
