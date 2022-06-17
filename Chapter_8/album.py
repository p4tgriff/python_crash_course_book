def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary describing a music album."""
    album = {'name': artist_name, 'title': album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album


while True:
    print("\nPlease tell me your favorite artist and album:")
    print("(enter 'q' at any time to quit)")

    artist_name = input('First name:')
    if artist_name == 'q':
        break

    album_title = input('Album name:')
    if album_title == 'q':
        break

artist = make_album('Bob Marley', 'No Woman No Cry')
print(artist)

artist = make_album('Queen', 'Pride')
print(artist)

artist = make_album('Eminem', '8-Mile', '12')
print(artist)
