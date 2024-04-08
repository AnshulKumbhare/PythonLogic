"""
Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""

def add_tag(el, s):
    s = f"<{el}>{s}</{el}>"
    return s

print(add_tag("i", "Python"))