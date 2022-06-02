def make_shirt(shirt_size, shirt_phrase):
    """description"""
    print(f"\nI will need a size {shirt_size} shirt.")
    print(f"On the shirt I want it to say, '{shirt_phrase}'.")


make_shirt('large', 'I love dogs')
make_shirt(shirt_phrase='Dogs are awesome', shirt_size='medium')


def make_shirt(shirt_size='large', shirt_phrase='I love Python'):
    """description"""
    print(f"\nI will need a size {shirt_size} shirt.")
    print(f"On the shirt I want it to say, '{shirt_phrase}'.")


make_shirt()
make_shirt(shirt_phrase='Dogs are awesome', shirt_size='medium')


def describe_city(city, country):
    """description"""
    print(f"\n{city.title()} is in {country.title()}.")


describe_city('Dallas', 'USA')
describe_city('Los Angeles', 'USA')
describe_city('Torronto', 'Canada')
