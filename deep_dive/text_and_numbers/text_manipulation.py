song = 'Here comes the sun'
print(song)
print('concatenate: ' + song)
print('tab:\t' + song)
print('new line:\n' + song)
print('startswith: ' + str(song.startswith('H')))
print('contains: ' + str('sun' in song))
print('split: ' + str(song.split(' ')))
print('get index: ' + str(song.find('the')))
print('slices: ' + song[5:10])
print('index: ' + song[11])
print('text length: ' + str(len(song)))
print('list length: ' + str(len(song.split(' '))))
song_list = song.split(' ')
print('join: ' + ','.join(song_list))
print('all capital: ' + song.upper())
print('all lower case: ' + song.lower())
print('Capital: ' + 'hi'.capitalize())
