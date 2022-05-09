rivers = {
    'nile': 'Egypt',
    'thames': 'England',
    'amazon': 'Brazil',
}

print(rivers)

for river in rivers:
    creek = rivers[river].title()
    print(f"\n{river.title()} is the biggest river in {creek}.")
