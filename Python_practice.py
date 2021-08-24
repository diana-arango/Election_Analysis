print("Hello World")
#Practice if statement
counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
# Creating a membership operator
counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list counties.")
else:   
    print("El Paso is not in the list of counties.")
# Membership and logical operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El paso is not in the list of counties.")
# Check if either "Arapahoe" or "El Paso" is in the counties list.
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe or El paso is not in the list of counties.")
# Iterate through lists and tuples
# Implementing a for loop by iterating through our lsit of counties.
for county in counties:
    print(county)
# Iterate through a dictionary
counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)
# Print each county from the counties dictionary using the key()method:
for county in counties_dict.keys():
    print(county)
# Get the values of a dictionary using the value method(). It will print all the values from a list in the order of entry
for voters in counties_dict.values():
    print(voters)
# Get the values of a dictionary using the key method()
for county in counties_dict:
    print(counties_dict[county])
# Get the values of a dictionary using the get method()
for county in counties_dict:
    print(counties_dict.get(county))
# Get the key-value pairs of a dictionary by using items() method:
for county,voters in counties_dict.items():
    print(county,voters)
for county,voters in counties_dict.items():
    print(county,"county has",voters,"registered voters.")
# Get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
# Get the values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# Retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])
# Retrieve the number of counties from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])
#Using F-Strings with dictionaries
counties_dict = {"Arapahoe": 422829, "Denver":463353, "Jefferson": 432438}
for county, voters in counties_dict.items():    
    print(f" {county} county has {voters} registered voters.")
# Multiple F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)
# Format Floating-Point Decimals
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
#Skill drill. Print county and register voters from counties_dict
counties_dict = {"Arapahoe": 4228929, "Denver":463353, "Jefferson": 432438}
for county, voters in counties_dict.items():    
    print((f"{county} county has {voters:,} registered voters."))
#Skill drill. Print county and register voters from voting_data
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in voting_data.items():    
    print((f"{county} county has {voters:,} registered voters."))