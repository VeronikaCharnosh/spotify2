'''Spotify 1'''
from dotenv import load_dotenv
import os 
import base64
from requests import post, get
import json

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# print(client_id, client_secret)

def get_token():
    '''
    Get token
    '''
    auth_string = client_id + ':' + client_secret
    auth_bites = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bites), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    result = post(url, headers = headers, data = data )
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

def get_auth_header(token):
    '''
    Get author header
    '''
    return {'Authorization': 'Bearer  ' + token}

def search_for_artist(token, artist_name):
    '''
    Search right artist name
    '''
    url = 	'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q={artist_name}&type=artist&limit=1'
    query_url = url + query 
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)['artists']['items']
    if len(json_result) == 0:
        print('No artist with this name exists...')
        return None
    return  json_result[0]
    # print(json_result)

def get_songs_by_artist(token, artist_id):
    '''
    Search songs by artist
    '''
    url =f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US'
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)['tracks']
    return json_result

def search_for_track(token, song_name, artist_name):
    '''
    Search available countries for track
    '''
    url = 	'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q={song_name}&type=track'
    query_url = url + query 
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    for i in range(len(json_result['tracks']['items'][0]['album']['artists'])):
        name = json_result['tracks']['items'][0]['album']['artists'][i]['name']
        if name == artist_name:
            # print(json_result)
            if len(json_result) == 0:
                print('No artist with this name exists...')
                return None
            return json_result['tracks']['items'][0]['album']['available_markets']
    
def user_input():
    '''
    Ask user for artist name
    '''
    print('Please enter artist name to check')
    name_for_check = input()
    return name_for_check
    
def for_return(name):
    '''
    Return result
    '''
    token = get_token()
    artist_name = search_for_artist(token, name)['name']
    artist_id = search_for_artist(token, name)['id']
    top_song_name = get_songs_by_artist(token, artist_id)[0]['name']
    countries = search_for_track(token, top_song_name, artist_name)
    return [artist_name, top_song_name, artist_id, countries]
# print(for_return())

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
