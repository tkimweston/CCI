from collections import defaultdict

dd = defaultdict(list)

dd[0].append(1)
dd[0].append(2)
print(dd)
dd[1].append(3)
dd[2].append(4)
print(dd)