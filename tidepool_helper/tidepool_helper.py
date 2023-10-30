import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)


class Tides:
    def __init__(self, location):
        self.location = location
        self.low_times = []
        self.low_heights = []


def get_tide_info(tides_object: Tides):
    parsed_page = BeautifulSoup(requests.get('https://www.tide-forecast.com/locations/{}/tides/latest'
                                             .format(tides_object.location)).content, 'html.parser')
    # Using the class name below exactly as shown ensures that scraped data corresponds to only
    # low tides that occur during daylight hours on the day that the webpage is accessed
    table_part_list = parsed_page.find_all('td', class_='tide-table__part tide-table__part--low tide-table__part--tide')
    for part in table_part_list:
        time_list = part.find_all('span', class_='tide-time__time tide-time__time--low')
        for span in time_list:
            if span is not None:
                tides_object.low_times.append(str(span).strip('<span class="tide-time__time tide-time__time--low"> ')
                                              .strip('</span>'))
        height_list = part.find_all('span', class_='tide-time__height')
        for span in height_list:
            if span is not None:
                tides_object.low_heights.append(str(span).strip('<span class="tide-time__height">')
                                                .strip('</span>'))


def print_tide_info(tides_object: Tides):
    print(tides_object.location)
    for i in range(0, len(tides_object.low_times)):
        print(tides_object.low_times[i] + ', ' + tides_object.low_heights[i] + 'm')

    print('\n')


@app.route('/location', methods=['POST'])
def location_info_page():
    if request.method == 'POST':
        location = request.form.get('location')
        tides_obj = Tides(location)
        get_tide_info(tides_obj)
        tides_dict = {'Location': tides_obj.location, 'Low Times': tides_obj.low_times,
                      'Low Heights': tides_obj.low_heights}
        print(tides_dict)
        return render_template('location_info_page.html', tides_dict=tides_dict)


@app.route('/')
def home_page():
    return render_template('home_page.html')


if __name__ == '__main__':
    home_page()
