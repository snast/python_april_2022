import spotipy
from spotipy import SpotifyClientCredentials

cid = 'XXX'
secret = 'XXX'
auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
results= sp.search("Beyonce")
print(results)