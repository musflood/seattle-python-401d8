# Strings
string = 'hello world'
string_cls = str(25)
string_formatting = '{}, {}, {}'.format('hello', 25, True)
# 'hello, 25, True'
string_formatting_a = '{2}, {0}, {1}'.format('hello', 25, True)
# 'True, hello, 25'

len(string)  # => 11
# In JS this is string.length


# Integers
num = 25
num + 5  # => 30 (num is still 25)
num += 5  # => 30 (num is now 30)
num / 5  # => 6.0
num //= 5  # => 6 (num is now 6)


# Booleans
t = True
f = False


# Lists
l = [1, 2, 3, 4]
l.append(5)  # => [1, 2, 3, 4, 5]
l.pop()  # => [1, 2, 3, 4] and return 5

l[-1]  # => 4
l[:-1] # => [1, 2, 3]

# for (start, stop, step) {} in JS
for item in l:
    # Do a thing...
    # item represents each object in the list
    print(item * 2)


# Dicts
user = {
    'name': 'spacecat',
    'ninja': True,
    'color': 'Purple'
}

user['name']  # => 'spacecat'
user.get('name')
user.items()

for key, value in user.items():
    print('{}: {}'.format(key, value))

In[29]: for key, value in user.items():
    ...: print('{}: {}'.format(key, value))
    ...:
name: spacecat
ninja: True
color: Purple

In[30]: for key in user.keys():
    ...: print(key)
    ...:
name
ninja
color

In[31]: for value in user.values():
    ...: print(value)
    ...:
spacecat
True
Purple
