rivers = {
    'nile': 'Egypt',
    'thames': 'England',
    'amazon': 'Brazil',
}

print(rivers)

for river in rivers:
    creek = rivers[river].title()
    print(f"\n{river.title()} is the biggest river in {creek}.")

for x in rivers.keys():
    print(x)

for y in rivers.values():
    print(y)
