x = 'ravi'
print(x)
print(id(x))

y = '''raviteja'''
print(y)
print(type(y))

z = "sai"
print(z)
print(type(z))  # single quoted strings does not support multi line text while triple quoted will support.

a = """satya"""
print(a)
print(type(a))
print(len(a))

b = '''hai
hello
how are you??? '''
print(b)
print(len(b))

print(y)
print(y[2])  # string class objects supports indexing both positive and negative.
print(y[-2])  # positive indexing starts from 0 and negative indexing starts from -1.
print(y[2:8])  # : is a slicing operator.
print(y[2:])
print(y[:5])
print(y[7:2])
print(y[-7:-2])
print(y[-2:-7])
print(y[2:-2])