currencies = ["EUR", "JPY", "GBP", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD"]


@app.route('/get_currencies', methods=['GET'])
def get_currencies():
    return jsonify({'currencies': currencies})

@app.route('/convert', methods=['GET'])
def convert():
    amount = request.args.get('amount')
    convert_to = request.args.get('convert_to')


    if amount is None or convert_to is None:
        return jsonify({'error': 'Missing attributes'})


    if convert_to not in currencies:
        return jsonify({'error': 'Invalid Currency'})


    if convert_to == "EUR":
        converted = float(amount)*0.96
    elif convert_to == "JPY":
        converted = float(amount)*157.83
    elif convert_to == "CAD":
        converted = float(amount)*1.44
    elif convert_to == "GBP":
        converted = float(amount)*0.80
    elif convert_to == "AUD":
        converted = float(amount)*1.61
    elif convert_to == "CHF":
        converted = float(amount)*0.90
    elif convert_to == "CNY":
        converted = float(amount)*7.30
    elif convert_to == "SEK":
        converted = float(amount)*11.02
    elif convert_to == "NZD":
        converted = float(amount)*1.78


    return jsonify({'converted': converted}), 200



@app.route('/get_time_zones', methods=['GET'])
def get_time_zones():
    url = 'https://timeapi.io/api/timezone/availabletimezones'
    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({'error': 'Call Failed'}), 400


    return jsonify(data)


@app.route('/get_time', methods=['GET'])
def get_time():
    timezone = request.args.get('timezone')
    url = f'https://timeapi.io/api/time/current/zone?timeZone={timezone}'
    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({'error': 'Call Failed'}), 400


    return jsonify(data)


@app.route('/convert_time', methods=['GET'])
def convert_time():
    convert_from = request.args.get('convert_from')
    time = request.args.get('time')
    convert_to = request.args.get('convert_to')


    parameters = {
        'fromTimeZone': convert_from,
        'dateTime': time,
        'toTimeZone': convert_to,
        "dstAmbiguity": ''
    }


    url = 'https://timeapi.io/api/conversion/converttimezone'
    response = requests.post(url, json=parameters)


    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({'error': response.status_code})


    return jsonify(data["conversionResult"])