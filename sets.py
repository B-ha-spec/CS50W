# Empty set
s = set()

# add elements
s.add(1)
s.add(2)
s.add(3)
s.add(2)
s.add(1)

s.remove(2)

s.add(4)

print(f"The set has {len(s)} elements.")
