def minutes_to_hour(minutes):
    hours = int(minutes) / 60
    return hours

minutes = input("Enter Minutes To Calculate How Many Hours: ")
print(minutes_to_hour(minutes))
