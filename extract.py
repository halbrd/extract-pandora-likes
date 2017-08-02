from bs4 import BeautifulSoup

# excerpt starts from div with class 'FeedbackList__list'
soup = BeautifulSoup(open('html_excerpt.txt', 'r').read(), 'html.parser')

songs = soup.find_all('a', class_='StationDetailsListItem__primaryText')
artists = soup.find_all('a', class_='StationDetailsListItem__secondaryTextUrl')

songs = [song.contents[0] for song in songs]
artists = [artist.span.contents[0] for artist in artists]

def table(songlist):
	def row(left, right):
		row = [left]
		row += [' ' for _ in range(song_max_width - len(left))]
		row += ['   ']
		row += [right]
		row += [' ' for _ in range(artist_max_width - len(right))]
		row = ''.join(row) + '\n'
		return row

	song_max_width = max([len(pair[0]) for pair in songlist])
	artist_max_width = max([len(pair[1]) for pair in songlist])

	table = row('Song', 'Artist')
	table += row(''.join(['-' for _ in range(song_max_width)]), 
				''.join(['-' for _ in range(artist_max_width)]))

	for pair in songlist:
		table += row(pair[0], pair[1])

	return table

songlist = list(zip(songs, artists))

with open('pandora_likes.txt', 'w') as f:
	f.write(table(songlist))

