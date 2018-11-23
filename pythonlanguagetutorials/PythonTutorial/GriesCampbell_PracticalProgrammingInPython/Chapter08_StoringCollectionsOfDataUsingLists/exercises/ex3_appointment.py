

appointments = ["9:00", "10:30", "14:00", "15:00", "15:30"]

# a --- append modifies list
appointments.append("16:30")
print(appointments)

# b -- creates new list
print(appointments.pop(-1))
appointments += ["16:30"]
print(appointments)

