temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]


# b
temps.sort()
print(temps)

# c
coolTemps = temps[0:2]
warmTemps = temps[2:]
print(coolTemps, warmTemps)

# d
tempsInCelsius = coolTemps + warmTemps
print(tempsInCelsius)

coolTemps.extend(warmTemps)
print(coolTemps)
