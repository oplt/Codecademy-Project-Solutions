# Frida Kahlo Retrospective

# list of the paintings:
paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]

# list of the dates:
dates = [1939, 1933, 1946, 1940]

# Zip both of these lists using using the list() function: 
paintings = list(zip(paintings, dates))
print (paintings)

"""Append the following paintings to the paintings list:
- 'The Broken Column', 1944
- 'The Wounded Deer', 1946
- 'Me and My Doll', 1937"""

paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print (paintings)

# Find the length of the paintings list:
len(paintings)

# generate a range of numbers starting from 1 and is equal in length to the list of items and save it a new variable called audio_tour_number:
audio_tour_number = list(range(1, 8))
print (audio_tour_number)

# Zip the audio_tour_number list to the paintings list and save it as master_list:
master_list = list(zip(audio_tour_number, paintings))
print(master_list)
