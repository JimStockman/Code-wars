def song_decoder(song):
  return " ".join(c for c in song.split('WUB') if c != '').strip()

# I had this solution, but for some reason it was crashing on the web interpreter
def best_song_decoder(song):
  return " ".join(song.replace('WUB', ' ').split())


phrase = 'WUBJEWUBM\'APPELLEWUBWUBJIMWUB'

print(song_decoder(phrase))
