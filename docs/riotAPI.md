# How We Use Riot API

### No API Key Required

### Relation to Personality Test:
- Ask the user what their favorite preference in professions would be: 
    - Mage, Assassin, Tank	
``` python
def tags(attributes):
    tags = [len(attributes)]
    for x in attributes:
        tags.append(x)
    tags.pop(0)
    return tags
print(tags(parse_json['data']["Ahri"]["tags"]))
```

- Ask the user if they are interested in normal or slightly weird people.
    - Mana: Normal
    - Anything else (Fury, Blood Well, Energy, …)
```python
def partype(partype):
    type = "Weird"
    if(partype == "Mana"):
        type = "Normal"
    return type
#(partype(parse_json['data']["Aatrox"]["partype"])) #tests the tags function above
```

- Ask the user if their preference is skinny or big people
    - Using the armor and spell block to simulate weight
```python
def weight(armor, spellblock): #tests the league character's bodytype
   weight = "Skinny"
   #print(armor, spellblock) #test
   if(int(armor) > 35 and int (spellblock) > 31):
       weight = "Big"
   return weight
#print(weight(parse_json['data']["Aatrox"]["stats"]["armor"], parse_json['data']["Aatrox"]["stats"]["spellblock"]))
#tests the tags function above
```

- Ask the user if their preference is strong or weak but kind people:
    - Using attackdamage, and attackdamageperlevel to simulate if the character is kind or tough people.
```python
def strength(attackdamage, attackdamageperlevel): #tests to see if the league character is kind or tough
   strength = "Kind"
   #print(armor, spellblock) #test
   if(int(attackdamage) > 55 or int (attackdamageperlevel) >= 4):
       strength = "Strong"
   return strength
#print(strength(parse_json['data']["Aatrox"]["stats"]["attackdamage"], parse_json['data']["Aatrox"]["stats"]["attackdamageperlevel"]))
#tests the strength function above
```

### One Function to Rule them All: 
- It uses all the helper functions in one function that just needs the name of the champion to work
```python
def League(champion):
   file = parse_json['data'][str(champion)]
   characteristics = []
   characteristics.append(file["id"])
   characteristics.append(tags(file['tags']))
   characteristics.append(partype(file["partype"]))
   characteristics.append(weight(file["stats"]["armor"], file["stats"]["spellblock"]))
   characteristics.append(strength(file["stats"]["attackdamage"], file["stats"]["attackdamageperlevel"]))
   return characteristics #Name, Attributes, Weird/Normal, Big/Skinny, Kind/Strong
print(League("Aatrox"))
```