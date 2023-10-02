# Python Notes

### Data Types:


1. **Numeric Types:**
    - **int:** Integer type, e.g., `5`, `-3`, `42`
    - **float:** Floating point type, e.g., `3.14`, `-0.01`, `2.71`
    - **complex:** Complex number type, e.g., `3 + 4j`, `2 - 5j`

2. **Boolean Type:**
    - **bool:** Represents the truth values, `True` and `False`

3. **Sequence Types:**
    - **str:** String type, e.g., `'Hello'`, `"World"`
    - **list:** Ordered collection of items, e.g., `[1, 2, 3]`, `['apple', 'banana', 'cherry']`
    - **tuple:** Immutable ordered collection of items, e.g., `(1, 2, 3)`, `('a', 'b', 'c')`

4. **Set Types:**
    - **set:** Unordered collection of unique items, e.g., `{1, 2, 3}`, `{'apple', 'banana'}`

5. **Mapping Types:**
    - **dict:** Collection of key-value pairs, e.g., `{'name': 'John', 'age': 30}`

6. **Binary Types (not commonly used in daily programming, but worth noting):**
    - **bytes:** Immutable sequence of bytes
    - **bytearray:** Mutable sequence of bytes
    - **memoryview:** Memory view object of byte sequences

Note: Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type based on the value you assign to the variable


**.keys()** - returns a list of all the keys in a dictionary

>example:
```py
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

keys = person.keys()
# keys will be: ["name", "age", "city"]
```

