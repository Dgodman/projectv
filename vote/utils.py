import json
import urllib.request
import urllib.parse
import os
import re


GEO_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
GEO_API_KEY = os.environ.get('GEO_API_KEY', "")


def _geocode(address):
    try:
        # convert address string to url safe characters
        safe_address = urllib.parse.quote_plus(address)
        # create url request
        url = GEO_API_URL + "address={}&key={}".format(safe_address, GEO_API_KEY)
        # send url request
        response = urllib.request.urlopen(url)
        # get json data
        data = json.load(response)
        return data
    except:
        return None


def verify_address(address):
    if address:
        geo_data = _geocode(address)
        if geo_data.get('status', "UNKNOWN_ERROR") == "OK":
            return True
    return False


class GeoCode:

    def __init__(self, address):
        # get geocode data
        data = self.do_geo(address)
        # check returned data
        self.status = data.get('status', "UNKNOWN_ERROR")
        if self.status == "OK":
            self.geo_data = data
            # filter results
            results = self.parse_results()
            if results:
                # get address information
                self.address = results.get('formatted_address')
                # regular expression to remove "county" from results
                re_county = re.compile('county', re.IGNORECASE)
                for address_component in results.get('address_components'):
                    type_list = address_component.get('types')
                    if len(type_list) > 0:
                        component_type = type_list[0]
                        component_value = address_component.get('short_name')
                        if component_type == 'street_number':
                            self.street_number = component_value
                        elif component_type == 'route':
                            self.route = component_value
                        elif component_type == 'locality':
                            self.town = component_value
                            self.city = component_value
                        elif component_type == 'administrative_area_level_1':
                            self.state = component_value
                        elif component_type == 'administrative_area_level_2':
                            county = re_county.sub("", component_value).strip().upper()
                            self.county = county
                        elif component_type == 'neighborhood':
                            self.neighborhood = component_value
                        elif component_type == 'country':
                            self.country = component_value
                        elif component_type == 'postal_code':
                            self.zip = component_value

    def parse_results(self):
        # get results which should return a single list item
        results = self.geo_data.get('results')
        if results and len(results) > 0:
            return results[0]
        else:
            return None

    def get_all(self):
        if self.status == "OK":
            return {
                'address': self.address,
                'street_number': self.street_number,
                'route': self.route,
                'city': self.city,
                'state': self.state,
                'zip': self.zip,
                'country': self.country,
                'county': self.county,
            }

    @staticmethod
    def do_geo(address):
        try:
            # convert address string to url safe characters
            safe_address = urllib.parse.quote_plus(address)
            # create url request
            url = GEO_API_URL + "address={}&key={}".format(safe_address, GEO_API_KEY)
            # send url request
            response = urllib.request.urlopen(url)
            # get json data
            data = json.load(response)
            return data
        except:
            return None
