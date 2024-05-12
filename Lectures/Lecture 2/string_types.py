text = "   This is a sample TEXT string with SOME  Repeated words.   "

# Case manipulation
print(text.lower())         # "   this is a sample text string with some  repeated words.   "
print(text.upper())         # "   THIS IS A SAMPLE TEXT STRING WITH SOME  REPEATED WORDS.   "
print(text.capitalize())     # "   this is a sample text string with some  repeated words.   "
print(text.title())          # "   This Is A Sample Text String With Some  Repeated Words.   "

# Whitespace and replacement
stripped_text = text.strip()
print(stripped_text)        # "This is a sample TEXT string with SOME  Repeated words."
replaced_text = stripped_text.replace(" ", "_").replace("SOME", "some")
print(replaced_text)       # "This_is_a_sample_TEXT_string_with_some__Repeated_words."

# Splitting and joining
words = stripped_text.split()
print(words)                # ['This', 'is', 'a', 'sample', 'TEXT', 'string', 'with', 'SOME', 'Repeated', 'words.']
joined_text = "-".join(words)
print(joined_text)          # "This-is-a-sample-TEXT-string-with-SOME-Repeated-words."

# Searching and counting
index = stripped_text.find("sample")
print(index)                # 10 (zero-based index)
count = stripped_text.count("is")
print(count)                # 2

# Checking prefixes and suffixes
print(stripped_text.startswith("This"))  # True
print(stripped_text.endswith("words."))  # True

# String formatting
name = "Alice"
age = 30
formatted_string = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(formatted_string)     # "My name is Alice, and I am 30 years old."
