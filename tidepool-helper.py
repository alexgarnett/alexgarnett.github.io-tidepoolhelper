import requests
from bs4 import BeautifulSoup


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


def main():
    location_list = ['Half-Moon-Bay-California', 'Huntington-Beach', 'Providence-Rhode-Island',
                     'Wrightsville-Beach-North-Carolina']
    tides_object_list = []

    for location in location_list:
        tides_object_list.append(Tides(location))

    for tides_object in tides_object_list:
        get_tide_info(tides_object)
        print_tide_info(tides_object)


if __name__ == '__main__':
    main()
