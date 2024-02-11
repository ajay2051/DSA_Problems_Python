# nyc_weather.csv contains new york city weather for first few days in the month of January.
# Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem


arr = []

with open("nyc_weather.csv", 'r') as f:
    next(f)  # skip first row
    for line in f:
        tokens = line.split(",")
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except IndexError:
            print("Invalid")
print("Temperature data:", arr)

if arr:
    average = sum(arr[0:7]) // len(arr[0:7])
    print("Average temperature:", average)
    maximum_temp = max(arr[0:10])
    print("Maximum temperature:", maximum_temp)
else:
    print("No temperature data available.")


# nyc_weather.csv contains new york city weather for first few days in the month of January.
# Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

weather_dict = {}
with open("nyc_weather.csv", "r") as f:
    next(f)
    for rows in f:
        token = rows.split(",")
        try:
            day = token[0]
            temperature = int(token[1])
            weather_dict[day] = temperature
        except ValueError:
            print("Invalid")
print(dict(weather_dict))
print(weather_dict["Jan 9"])
