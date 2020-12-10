# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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

# write your update damages function here:
def updated_damages(damage):
  new_list = []
  conversion = {"M": 1000000, "B": 1000000000}
  for i in damages:
    if i == "Damages not recorded":
      new_list.append("Damages not recorded")
    elif i[-1] == "M" or "B":
      new_list.append(int(float(i[:-1])*conversion[i[-1]]))
  return new_list

#print(updated_damages(damages))




# write your construct hurricane dictionary function here:

def hurricane_dict():
  master_hurricane_dict = {}
  for i in range(33):
    hurricane = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages(damages)[i], "Deaths": deaths[i]}
    master_hurricane_dict[names[i]] = hurricane
  return master_hurricane_dict

print(hurricane_dict())



# write your construct hurricane by year dictionary function here:

def canes_by_year(cane_list):
  canes_by_year_dict = {}
  for cane in hurricane_dict():
    current_cane = hurricane_dict()[cane]
    current_year = hurricane_dict()[cane]["Year"]
    if canes_by_year_dict.get(current_year) == None:
      canes_by_year_dict[current_year] = [current_cane]
    else:
      year_list = canes_by_year_dict.get(current_year)
      year_list.append(current_cane)
      canes_by_year_dict[current_year] = year_list
  return canes_by_year_dict
    

#print(canes_by_year(hurricane_dict()))


# write your count affected areas function here:

def count_areas_affected(cane_list):
  counted_areas_affected = {}
  for cane in hurricane_dict():
    for place in hurricane_dict()[cane]["Areas Affected"]:
      if counted_areas_affected.get(place) == None:
        counted_areas_affected[place] = 1
      else:
        counted_areas_affected[place] = counted_areas_affected[place] + 1
  return counted_areas_affected

#print(count_areas_affected(hurricane_dict()))


# write your find most affected area function here:

def most_affected_area(areas_affected):
  max_area = ""
  max_area_count = 0
  for area in count_areas_affected(hurricane_dict()):
    if count_areas_affected(hurricane_dict())[area] > max_area_count:
      max_area = area
      max_area_count = count_areas_affected(hurricane_dict())[area]
  return "Most affected place: " + max_area + ", " + str(max_area_count) + " times."
  
#print(most_affected_area(count_areas_affected))



# write your greatest number of deaths function here:

def greatest_deaths_cane(cane_list):
  max_deaths_cane = ""
  max_deaths_count = 0
  for cane in hurricane_dict():
    if hurricane_dict()[cane]["Deaths"] > max_deaths_count:
      max_deaths_cane = cane
      max_deaths_count = hurricane_dict()[cane]["Deaths"]
  return str(max_deaths_count) + " during hurricane " + max_deaths_cane

print(greatest_deaths_cane(hurricane_dict()))





# write your catgeorize by mortality function here:

def mortality_scale_to_cane(cane_list):
  mortality_ranked_canes_dict = {0:[], 1:[], 2:[], 3:[], 4:[]} 
  for cane in hurricane_dict():
    if hurricane_dict()[cane]["Deaths"] == 0:
      mortality_ranked_canes_dict[0].append(hurricane_dict()[cane])
    if hurricane_dict()[cane]["Deaths"] <= 100:
      mortality_ranked_canes_dict[1].append(hurricane_dict()[cane])
    if hurricane_dict()[cane]["Deaths"] <= 500:
      mortality_ranked_canes_dict[2].append(hurricane_dict()[cane])
    if hurricane_dict()[cane]["Deaths"] <= 1000:
      mortality_ranked_canes_dict[3].append(hurricane_dict()[cane])
    if hurricane_dict()[cane]["Deaths"] <= 10000:
      mortality_ranked_canes_dict[4].append(hurricane_dict()[cane])  
  
  return(mortality_ranked_canes_dict)

#print(mortality_scale_to_cane(hurricane_dict()))





# write your greatest damage function here:

def greatest_damage_cane(cane_list):
  max_damage_cane = ""
  max_damage_count = 0
  for cane in hurricane_dict():
    if hurricane_dict()[cane]["Damage"] == "Damages not recorded":
      pass
    elif hurricane_dict()[cane]["Damage"] > max_damage_count:
      max_damage_cane = cane
      max_damage_count = hurricane_dict()[cane]["Damage"]
  return str(max_damgage_count) + " during hurricane " + max_damgage_cane

print(greatest_damage_cane(hurricane_dict()))





# write your catgeorize by damage function here:






