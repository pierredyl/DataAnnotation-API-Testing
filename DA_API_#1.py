from flask import Flask, request, jsonify
import requests
import inflect

app = Flask(__name__)

#RAWG
YOUR_API_KEY = ""

@app.route('/get_app_news', methods=['GET'])
def get_app_news():
    appId = request.args.get('appId')
    count = request.args.get('count')


    if appId is None:
        return jsonify({'error': 'Specify an appId'}), 400
    if count is None:
        return jsonify({'error': 'Specify a count'}), 400


    url = f'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={appId}&count={count}&maxlength=300&format=json'


    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({'error': 'External API call failed'})


    return jsonify(data)

@app.route('/get_app_achievements_percentage', methods=['GET'])
def get_app_achievements_percentage():
    appId = request.args.get('appId')


    url = f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={appId}&format=json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({'error': 'External API call failed'})


    return jsonify(data)

@app.route('/search_games', methods=['GET'])
def search_games():
    search = request.args.get('search')
    genres = request.args.get('genres')
    tags = request.args.get('tags')


    if genres is None and tags is None:
        return jsonify({'error': 'Specify genres and tags'}), 400
    elif tags is None:
        return jsonify({'error': 'Specify tags'}), 400
    elif genres is None:
        return jsonify({'error': 'Specify genres'}), 400


    if search is None:
        url = f'https://api.rawg.io/api/games?key={YOUR_API_KEY}&genres={genres}&tags={tags}'
    elif search is not None:
        url = f'https://api.rawg.io/api/games?key={YOUR_API_KEY}&genres={genres}&tags={tags}&search={search}'


    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({'error': 'External API call failed'})


    return jsonify(data)

@app.route('/get_game_details', methods=['GET'])
def get_game_details():
    id = request.args.get('id')


    if id is None:
        return jsonify({'error': 'Specify an id'}), 400


    url = f'https://api.rawg.io/api/games/{id}?key={YOUR_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({'error': 'External API call failed'})


    return jsonify(data)


if __name__ == '__main__':
    app.run(debug= True)