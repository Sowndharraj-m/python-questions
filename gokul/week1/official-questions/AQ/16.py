# Accept a positive integer,
# x , as input from the user. Without using the * symbol anywhere in your code, print 
# 10 * 𝑥, i.e. the product of the integer input and the number 10.

x = int(input())
print(int(str(x) + "0"))



# Thought for <1s

# Let me break it down step by step:

# print(int(str(x) + "0"))
# Working from the inside out, let's say x = 5:

# Step	Code	What happens	Result
# 1	x	The integer value	5 (int)
# 2	str(x)	Convert integer to string	"5" (string)
# 3	str(x) + "0"	Concatenate (join) the string "0" at the end	"50" (string)
# 4	int(str(x) + "0")	Convert the string back to an integer	50 (int)
# 5	print(...)	Print the result	prints 50
# Why does this work?
# In math, when you add a zero at the end of any number, it's the same as multiplying by 10:

# 3 → 30 (3 × 10)
# 12 → 120 (12 × 10)
# 99 → 990 (99 × 10)
# Why do we need str() and int()?
# str(x) — Because the + operator between two strings does concatenation (joining), not addition. We need x to be a string to "glue" "0" at the end.
# int(...) — After concatenation, the result is a string like "50". We convert it back to an integer so we get a proper number 50.
# Without str() it would fail:
# python
# x + "0"   # ❌ TypeError: can't add int and string
# Without int() at the end:
# python
# str(x) + "0"  # Would print "50" as a string — works for printing,
#                # but it's technically a string, not a number
# So the trick is: int → string → append "0" → back to int = multiplied by 10, no * used! 🎯

