import shelve

integers = [1, 2, 3, 4, 5, 6]

with shelve.open('shelve-file', 'c') as shelf:
    shelf['ints'] = integers

with shelve.open('shelve-file', 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key]))

        