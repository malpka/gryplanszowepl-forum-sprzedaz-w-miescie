import pandas
import matplotlib.pyplot as plt

debug = 0

games = pandas.read_csv("gry-planszowe.csv", delimiter=";", encoding="cp852")
games['ll']=games['location'].str.lower()

if debug == 1:
	print(games.columns)
	print(games.shape)

sorted = games.sort_values(['ll', 'nick'])

defaultloc = 'xxx'
print('[spoiler]')
for index, row in sorted.iterrows():
    if row['ll'] != defaultloc:
        print('[/spoiler]')
        print (row['ll'][0].upper()+ row['ll'][1:] + '[spoiler]')
        defaultloc = row['ll']
        
    print(row['nick'] + " - [url=" + row['url'] + ']LINK[/url]')
	
##grouppie = games.groupby('localisation')
##for name, group in grouppie:
##    for name2, group2 in group.groupby('nick'):
##        print(name +  ' - ' + name2)
##        print(group2['url'])

print('[/spoiler]')
