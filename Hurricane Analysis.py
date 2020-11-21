# PYTHON FUNDAMENTALS--- Hurricane Analysis

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

from collections import defaultdict
# write your update damages function here:

def update_damages(list):
    new_damage_list = []
    conversion = {"M": 1000000, "B": 1000000000}
    for damage in list:
        if damage == 'Damages not recorded':
            new_damage_list.append(damage)
        elif damage[-1] in conversion.keys():
            new_value = float(damage[:-1]) * conversion[damage[-1]]
            new_damage_list.append(new_value)

    return new_damage_list

updated_damages = update_damages(damages)
print(updated_damages)

# write your construct hurricane dictionary function here:
hurricanes = {}
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    for i in range(len(names)):
        hurricanes[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i],
                                'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i],
                                'Damage': damages[i], 'Death': deaths[i]}
    return hurricanes

print(hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))
print(hurricanes["Cuba I"])

# write your construct hurricane by year dictionary function here:

def hurricane_year(year):
  hurricane_year_dict = {}
  new_year_list =[]
  for k,v in hurricanes.items():
    if v['Year']==year: 
      new_year_list.append(v)
  hurricane_year_dict[year] = new_year_list
  return hurricane_year_dict

print(hurricane_year(1924))

# write your count affected areas function here:
affected_areas = {}

def count_affected_areas(dictionary):
    for name in dictionary:
        for area in dictionary[name]['Areas Affected']:
            if area in affected_areas:
                affected_areas[area] += 1
            else:
                affected_areas[area] = 1
    return affected_areas

print(count_affected_areas(hurricanes))
# write your find most affected area function here:

def most_affected_area(dict):
    values = sorted(list(dict.values()), reverse=True)
    for area in dict.keys():
        if values[0] == dict[area]:
            return area, dict[area]

print(most_affected_area(affected_areas))

# write your greatest number of deaths function here:

def deadliest_hurricane(hurricanes):
  max_mortality = 0
  deadliest_hurricane = ''
  for k,v in hurricanes.items():
    if v['Death'] > max_mortality:
      max_mortality = v['Death']
      deadliest_hurricane = k
  return deadliest_hurricane, max_mortality

print(deadliest_hurricane(hurricanes))

# write your catgeorize by mortality function here:

def hurricane_rating(dict):
    hurricane_rated = {0:[],1:[],2:[],3:[],4:[],5:[]}
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    for name in dict:
        if dict[name]['Death'] == mortality_scale[0]:
            hurricane_rated[0].append(name)
        elif mortality_scale[0] < dict[name]['Death'] <= mortality_scale[1]:
            hurricane_rated[1].append(name)
        elif mortality_scale[1] < dict[name]['Death'] <= mortality_scale[2]:
            hurricane_rated[2].append(name)
        elif mortality_scale[2] < dict[name]['Death'] <= mortality_scale[3]:
            hurricane_rated[3].append(name)
        elif mortality_scale[3] < dict[name]['Death'] <= mortality_scale[4]:
            hurricane_rated[4].append(name)
        else:
            hurricane_rated[5].append(name)
    return hurricane_rated

print(hurricane_rating(hurricanes))

# write your greatest damage function here:

def greatest_damage(dict):
    damages = []
    for name in dict:
        if dict[name]['Damage'] != 'Damages not recorded':
            damages.append(dict[name]['Damage'])
    greatest_damage = max(damages)
    for name in dict:
        if dict[name]['Damage'] == greatest_damage:
            return name, greatest_damage

print(greatest_damage(hurricanes))

# write your catgeorize by damage function here:

def rating_by_damage(dict):
    hurricane_damage_scale = {'No Damage': [], 1: [], 2: [], 3: [], 4: [], 5: []}
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    for name in dict:
        if dict[name]['Damage'] == 'Damages not recorded':
            hurricane_damage_scale['No Damage'].append(name)
        elif damage_scale[0] < dict[name]['Damage'] <= damage_scale[1]:
            hurricane_damage_scale[1].append(name)
        elif damage_scale[1] < dict[name]['Damage'] <= damage_scale[2]:
            hurricane_damage_scale[2].append(name)
        elif damage_scale[2] < dict[name]['Damage'] <= damage_scale[3]:
            hurricane_damage_scale[3].append(name)
        elif damage_scale[3] < dict[name]['Damage'] <= damage_scale[4]:
            hurricane_damage_scale[4].append(name)
        else:
            hurricane_damage_scale[5].append(name)
    return hurricane_damage_scale

print(rating_by_damage(hurricanes))