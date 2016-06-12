import datetime
import json
import requests


def time_converter(time):
    """
    Converts the time format
    """
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder_city(city):
    """
    Builds the url to access the OpenWeatherMap API passing a place as parameter
    """
    # valid OpenWeatherMap API key
    api_key = '4723ead7e237c638e42b499385b39a16'
    unit = 'metric'
    api = 'http://api.openweathermap.org/data/2.5/weather?q='
    full_api_url = api + str(city) + '&mode=json&units=' + unit + '&APPID=' + api_key
    return full_api_url

def url_builder_coords(latitude, longitude):
    """
    Builds the url to access the OpenWeatherMap API passing coordinates as parameter
    """
    # valid OpenWeatherMap API key
    api_key = '4723ead7e237c638e42b499385b39a16'
    unit = 'metric'
    api = 'http://api.openweathermap.org/data/2.5/weather?lat='+str(latitude)+ '&lon='+str(longitude)
    full_api_url = api + '&mode=json&units=' + unit + '&APPID=' + api_key
    return full_api_url

def data_fetch(full_api_url):
    """
    Fetches the data processing the get request returning the raw data
    """
    url = requests.get(full_api_url)
    output = url.text
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    """
    Organizes the data inside the raw data dictionary in the propper way
    """
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    """
    Outputs the data in the terminal and builds a brief and detailed reports of
    the weather
    """

    m_symbol = '\xb0' + 'C'


    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')

    m_symbol = 'Celsius'
    detailed_report = 'There is a temperature of {}'.format(data['temp']) +" degrees " \
             + m_symbol + ". Sky status: {}".format(data['sky']) + ". "+ \
             'Maximum and minimum temperatures of: {}. and. {} degrees Celsius respectively. '.format(data['temp_max'], data['temp_min']) + \
             'Wind Speed of {} meters per second, Degree: {}.'.format(data['wind'], data['wind_deg']) + \
             ' Humidity: {}.'.format(data['humidity']) + ' Cloudiness: {}. '.format(data['cloudiness']) + \
             'Pressure: {} hPa'.format(data['pressure'])

    brief_report = 'There is a temperature of {}'.format(data['temp']) +" degrees " \
             + m_symbol + ". Sky status: {}".format(data['sky']) + "."

    return (brief_report, detailed_report)
