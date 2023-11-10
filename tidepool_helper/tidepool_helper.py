import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


class Tides:
    def __init__(self, location):
        self.location = location
        self.dates = []
        self.low_times = []
        self.low_heights = []

    def do_location(self):
        return self.location.replace('-', ' ')

    def do_low_times(self):
        if len(self.low_times) == 1:
            return str(self.low_times[0])
        elif len(self.low_times) == 0:
            return 'No daylight low tides on this day'
        else:
            all_times = ''
            for time in self.low_times:
                all_times += time + ', '
            return all_times[:-2]

    def do_low_heights(self):
        if len(self.low_heights) == 1:
            return str(self.low_heights[0])
        elif len(self.low_heights) == 0:
            return ''
        else:
            all_heights = ''
            for height in self.low_heights:
                all_heights += height + ', '
            return all_heights[:-2]


def _get_tide_info(tides_object: Tides):
    # Get full page and scrape date tables, organizing them in a list
    parsed_page = BeautifulSoup(requests.get(
        'https://www.tide-forecast.com/locations/{}/tides/latest'
        .format(tides_object.location)).content, 'html.parser')
    all_tide_day_tables = parsed_page.find_all('div', class_='tide-day')
    for day_table in all_tide_day_tables:
    # day_table = all_tide_day_tables[0]      # This is temporary, replace with above

        # Get the sunrise and sunset times
        sunrise_element = day_table.find(string="Sunrise:")
        sunrise_str = sunrise_element.findNext(
            "span", class_="tide-day__value").get_text()
        sunrise_str = sunrise_str[1:-2] + ' ' + sunrise_str[-2:]    # Drop leading space and add space after minutes
        sunrise_time = to_time(sunrise_str)

        sunset_element = day_table.find(string="Sunset:")
        sunset_str = sunset_element.findNext(
            "span", class_="tide-day__value").get_text()
        sunset_str = sunset_str[1:-2] + ' ' + sunset_str[-2:]
        sunset_time = to_time(sunset_str)

        # Get the date
        heading = day_table.find("h4", class_="tide-day__date")
        date = str(heading).split(':')[1].strip('</h4>')[1:]
        tides_object.dates.append(date)

        # Get the daylight lows and heights
        low_times = ''
        low_heights = ''
        low_tides = day_table.findAll(string='Low Tide')
        for entry in low_tides:
            low_str = entry.findNext('b').get_text()
            low_str = low_str[1:]                           # Drop leading space
            low_time = to_time(low_str)
            if sunrise_time <= low_time <= sunset_time:
                low_times += low_str + ', '
                tide_height = str(entry.findNext(
                    'b', class_='js-two-units-length-value__primary').get_text())
                # tide_height = str(entry.findNext(
                #     'b', class_='js-two-units-length-value__primary'))
                # tide_height = tide_height.strip('<b class="js-two-units-length-value__primary">')

                low_heights += tide_height + ', '

        if low_times == '':     # If no daylight lows were found
            tides_object.low_times.append('None')
            tides_object.low_heights.append('---')
        else:
            tides_object.low_times.append(low_times[:-2])
            tides_object.low_heights.append(low_heights[:-2])

    return tides_object


def to_time(time_str: str):
    # strptime requires specific, zero-padded formats
    try:
        split = time_str.split(':')
        if len(split[0]) == 1:
            time_str = '0' + time_str
            split = time_str.split(':')
        if split[0] == '00':
            time_str = '12' + time_str[2:]

        _datetime = datetime.strptime(time_str, "%I:%M %p")

    except ValueError:
        _datetime = datetime.strptime('12:00 AM', "%I:%M %p")

    return _datetime.time()


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
                                                .strip('</span>') + 'm')


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
        _get_tide_info(tides_obj)
        table = []
        for i, date in enumerate(tides_obj.dates):
            table.append([tides_obj.dates[i],
                          tides_obj.low_times[i], tides_obj.low_heights[i]])

        return render_template('location_info_page.html', tbl=table)


@app.route('/')
def home_page():
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    # tides = Tides('Half-Moon-Bay-California')
    # _get_tide_info(tides)

