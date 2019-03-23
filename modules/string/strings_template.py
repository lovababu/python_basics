from string import Template

template = Template('Hello, Mr. $name')
result = template.substitute(name="Lova")

print("After substitution : ", result)

d = dict(name="srilekha")
result = template.substitute(d)
print("After substitution with dict: ", result)
