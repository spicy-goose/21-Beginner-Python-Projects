fillerText = {
    "properNoun": "",
    "adjective1": "",
    "color" : "",
    "animal" : "",
    "place" : "",
    "adjective2" : "",
    "magicalCreatures1": "",
    "adjective3" : "",
    "magicalCreatures2": "",
    "room": "",
    "pluralNoun1": "",
    "noun1": "",
    "noun2": "",
    "adjective4" : "",
    "pluralNoun2" : "",
    "number" : "",
    "measureOfTime" : "",
    "verbEndingInING" : "",
    "adjective5" : "",
    "noun3": "",
}

for word in fillerText:
    fillerText[word] = input(word+ ": ")

text = f"Dear {fillerText['properNoun']}, \n\
I am writing to you from a {fillerText['adjective1']} castle in an enchanted forest. I found myself here one day after \n\
going for a ride on a {fillerText['color']} {fillerText['animal']} in {fillerText['place']}. There are \n\
{fillerText['adjective2']} {fillerText['magicalCreatures1']} and {fillerText['adjective3']} {fillerText['magicalCreatures2']} here! In the \n\
{fillerText['room']} there is a pool full of {fillerText['pluralNoun1']}. I fall asleep each night on a {fillerText['noun1']} of \n\
{fillerText['noun2']} and dream of {fillerText['adjective4']} {fillerText['pluralNoun2']}. It feels as though I have lived here for \n\
{fillerText['number']} {fillerText['measureOfTime']}. I hope one day you can visit, although the only way to get here now is \n\
{fillerText['verbEndingInING']} on a {fillerText['adjective5']} {fillerText['noun3']}!!"

print(text)