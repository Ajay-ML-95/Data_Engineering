# ============================================================
# Assignment: Lists, Tuples, Sets & Dictionaries
# ============================================================


# ============================================================
# THEORY QUESTIONS
# ============================================================

# Q1. Difference between List, Tuple, Set, and Dictionary
"""
LIST:
- Ordered collection of items
- Mutable (can be changed after creation)
- Allows duplicate values
- Defined using square brackets []
- Example: [1, 2, 3, "hello"]

TUPLE:
- Ordered collection of items
- Immutable (cannot be changed after creation)
- Allows duplicate values
- Defined using parentheses ()
- Example: (1, 2, 3, "hello")

SET:
- Unordered collection of items
- Mutable (can add/remove items)
- Does NOT allow duplicate values (auto-removes duplicates)
- Defined using curly braces {}
- Example: {1, 2, 3}

DICTIONARY:
- Unordered collection of key-value pairs
- Mutable (can be changed after creation)
- Keys must be unique; values can repeat
- Defined using curly braces {} with key: value pairs
- Example: {"name": "Alice", "age": 25}
"""


# Q2. Why are sets used in real-world systems? (3 real-time use cases)
"""
1. UNIQUE VISITOR TRACKING (Web Analytics):
   Websites use sets to count unique visitors. Even if a user visits
   multiple times, their ID is stored only once in the set — giving
   an accurate unique visitor count.

2. SPAM FILTERING (Email Systems):
   Email systems maintain a set of blacklisted email addresses or IPs.
   Sets allow O(1) fast lookup to instantly check if an incoming
   sender is blacklisted, without duplicate entries.

3. TAG / INTEREST DEDUPLICATION (Social Media):
   When users add tags or interests, sets ensure no duplicates are
   stored. For example, if a user adds "Python" twice, the set keeps
   only one instance, keeping the data clean.
"""


# Q3. Mutable vs Immutable datatypes
"""
MUTABLE (can be changed after creation):
- List    → you can add, remove, or update items
- Set     → you can add or remove items
- Dictionary → you can add, remove, or update key-value pairs

IMMUTABLE (cannot be changed after creation):
- Tuple   → once created, its items cannot be changed
- String  → characters cannot be changed in place
- Integer, Float, Boolean → their values cannot be changed in place

Summary Table:
| Collection   | Mutable | Ordered | Duplicates Allowed |
|-------------|---------|---------|-------------------|
| List        |   Yes   |   Yes   |        Yes        |
| Tuple       |   No    |   Yes   |        Yes        |
| Set         |   Yes   |   No    |        No         |
| Dictionary  |   Yes   |   Yes*  |  Keys: No, Values: Yes |
(*Dictionaries maintain insertion order in Python 3.7+)
"""


# ============================================================
# PROGRAMMING QUESTIONS
# ============================================================

print("=" * 55)
print("Q4. List Operations")
print("=" * 55)

cities = ["New York", "London", "Tokyo", "Paris", "Dubai"]

print("First element :", cities[0])
print("Last element  :", cities[-1])

cities.append("Sydney")
print("After append  :", cities)


print("\n" + "=" * 55)
print("Q5. Transaction Processing")
print("=" * 55)

transactions = [1200, 8500, 3400, 12000, 500, 7600, 4900, 9200]

print("Transactions greater than 5000:")
for amount in transactions:
    if amount > 5000:
        print(f"  ₹{amount}")


print("\n" + "=" * 55)
print("Q6. Tuple Operations")
print("=" * 55)

employee_ids = (101, 102, 103, 104, 105)

print("Tuple length    :", len(employee_ids))
print("Second element  :", employee_ids[1])

print("Looping through tuple:")
for emp_id in employee_ids:
    print(f"  Employee ID: {emp_id}")


print("\n" + "=" * 55)
print("Q7. Set Operations")
print("=" * 55)

numbers_with_duplicates = {10, 20, 30, 20, 10, 40, 30, 50}

print("Set with duplicates removed:", numbers_with_duplicates)
print("Note: Duplicate values were automatically removed by the set.")


print("\n" + "=" * 55)
print("Q8. Unique Visitors Counter")
print("=" * 55)

visitor_ids = {"U001", "U002", "U003", "U001", "U004", "U002", "U005"}

print("Visitor IDs set :", visitor_ids)
print("Total unique visitors:", len(visitor_ids))


print("\n" + "=" * 55)
print("Q9. Dictionary Operations — Student Record")
print("=" * 55)

student = {
    "name": "Alice Johnson",
    "age": 21,
    "course": "Computer Science"
}

print("Student details:")
for key, value in student.items():
    print(f"  {key}: {value}")


print("\n" + "=" * 55)
print("Q10. Employee Record System")
print("=" * 55)

employee = {
    "id": 101,
    "name": "John",
    "salary": 50000
}

print("Before update:", employee)

employee["salary"] = 65000

print("After update :", employee)
