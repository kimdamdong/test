class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        print(f'other: {other.obj} / self: {self.obj}')
        return other.obj == self.obj

    def __lt__(self, other):
        print(f'other "{other.obj}" is lower than: "{self.obj}"')
        return other.obj < self.obj


ls = [
    ['tall', 'blue'],
    ['short', 'red'],
    ['tall', 'clue'],
    ['tall', 'zzz']
]

# ls_sort = sorted(ls, key = lambda x: (x[1], x[2]))
# print(ls_sort)

rev_sort = sorted(ls, key = lambda x: (x[0], reversor(x[1])))
print('\n', rev_sort)
