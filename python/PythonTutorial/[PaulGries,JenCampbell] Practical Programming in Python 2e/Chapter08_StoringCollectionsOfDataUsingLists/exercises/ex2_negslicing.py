

kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

# a
print(kingdoms[-6])

#b
print(kingdoms[-1])

# c
print(kingdoms[-6:-3])

# d
print(kingdoms[-4:-1])

# e
print([kingdoms[-2], kingdoms[-1]])
print(kingdoms[-2:])

# f
# as long as in range (-6 to -1) and (0 to 5) then when the smaller one comes
# last as in -1:-2 then we get empty list. 
print(kingdoms[-1:-2])
print(kingdoms[-1:-3])
print(kingdoms[-1:-4])
