# What is the difference between the string methods find and index ?

# The string methods `find` and `index` are both used to search for a substring within a string, but they differ in their behavior when the substring is not found.

# - `find` returns -1 if the substring is not found.
# - `index` raises a ValueError if the substring is not found.    



x = "sowndhar"
print(x.find("ow"))  # Output: 5  
print(x.index("ow"))  # Output: -1