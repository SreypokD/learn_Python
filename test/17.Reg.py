# search function 
#  searches the string for a match, and returns a Match object if there is a match.
import re
 
s = 'GeeksforGeeks: A computer science portal for geeks'
match = re.search(r'portal', s)
# print('Start Index:', match.start())
# print('End Index:', match.end())

# ========backslace========== 
s = 'geeks.forgeeks'
# without using \
match = re.search(r'.', s)
# print(match)
# using \
match = re.search(r'\.', s)
# print(match)


# =========================================================
#The split() Function
# returns a list where the string has been split at each match

txt = "The rain in Spain jj-w"
x = re.split("\s", txt)
# print(x)


# ===========================================================
# The sub() Function 
#  :function replaces the matches with the text of your choice

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
# print(x)

# ==========================================================

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# =====================


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())