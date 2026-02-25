# The following string is encoded using the Caesar cipher with a shift of 5: udymts . 
# Decode the string!

encoded = "udymts"
shift = 5
decoded = ""
for ch in encoded:
    decoded += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
print(decoded)  # python
