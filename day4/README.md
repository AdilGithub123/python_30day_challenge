# Day 4 — String Manipulation Projects

Day 4 focuses on strengthening Python string manipulation skills.  
These projects build practical skills for cleaning data, validating input,  
and performing simple text analytics — all essential abilities for real-world software tasks.

---

## 📌 Project 1 — Name Normalizer
**Goal:** Clean messy user-entered names.

**Features:**
- Removes extra whitespace
- Normalizes spacing between words
- Capitalizes each word correctly

**Concepts Used:**
- `.strip()`
- `.split()`
- `.title()`
- `" ".join()`

---

## 📌 Project 2 — Email Validator
**Goal:** Perform basic email validation (non-RFC).

**Validation Rules:**
- Must contain exactly one `@`
- Must contain a `.` in the domain part
- Username (before @) cannot be empty
- Domain (after @) cannot be empty
- No spaces allowed

**Concepts Used:**
- `.count()`
- `.split()`
- `.strip()`
- String searching

---

## 📌 Project 3 — Word Frequency Counter
**Goal:** Count occurrences of each word in a sentence.

**Features:**
- Converts text to lowercase
- Removes simple punctuation
- Splits text into words
- Counts word frequency using a dictionary

**Concepts Used:**
- `.lower()`
- `.replace()`
- `.split()`
- `dict.get()`

---

## 🏁 What You Learned Today
- How to clean and normalize user input  
- How to build simple validation logic  
- How to process text and extract useful information  
- How to work with dictionaries for counting and data processing