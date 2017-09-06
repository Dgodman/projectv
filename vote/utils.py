import json
import urllib.request
import urllib.parse
import os
import re
import base64
from random import randint


GEO_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
GEO_API_KEY = os.environ.get('GEO_API_KEY', "")
PO_REGEX = r"((^|[^A-Z]+)((P[. ]*O[. ]*(B((O?X)|IN)?)?)|(P(OST(AL)?)?[. ]*((OFF(ICE)?)|(B((O?X)|IN)))))[^A-Z])"


# TESTING ONLY
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


# TESTING ONLY
def verify_address(address):
    if address:
        geo_data = _geocode(address)
        if geo_data.get('status', "UNKNOWN_ERROR") == "OK":
            return True
    return False


# TESTING ONLY
def is_pobox(address):
    re_pobox = re.compile(PO_REGEX, re.IGNORECASE)
    matches = re_pobox.search(address)
    if matches:
        return True
    else:
        return False


class GeoCode:
    """
    Class to get and parse Google's geocode api for USA addresses
    """
    def __init__(self, address):
        # get geocode data
        data = self.do_geo(address)
        # check returned data
        self.status = data.get('status', "GENERIC_ERROR")
        if self.status == "OK":
            self.geo_data = data
            # filter results
            results = self.parse_results()
            if results:
                # create address components
                self.address = results.get('formatted_address')
                self.partial_match = results.get('partial_match')
                self.street_number = ''
                self.route = ''
                self.town = ''
                self.city = ''
                self.state = ''
                self.county = ''
                self.neighborhood = ''
                self.country = ''
                self.zip = ''
                self.is_po = self.is_pobox(address)
                # regular expression to remove "county" from results
                re_county = re.compile('county', re.IGNORECASE)
                # set address components
                for address_component in results.get('address_components'):
                    type_list = address_component.get('types')
                    if len(type_list) > 0:
                        component_type = type_list[0]
                        component_value = address_component.get('short_name')
                        if component_type == 'street_number':
                            self.street_number = component_value
                        elif component_type == 'route':
                            self.route = component_value
                        elif component_type == 'locality' or component_type == 'postal_town':
                            self.town = component_value
                            self.city = component_value
                        elif component_type == 'administrative_area_level_1':
                            self.state = component_value
                        elif component_type == 'administrative_area_level_2':
                            # remove "county" from county name
                            county = re_county.sub("", component_value).strip().upper()
                            self.county = county
                        elif component_type == 'neighborhood':
                            self.neighborhood = component_value
                        elif component_type == 'country':
                            self.country = component_value
                        elif component_type == 'postal_code':
                            self.zip = component_value

                error_list = self.get_errors()
                if len(error_list) > 0:
                    print(error_list)
                else:
                    print("OK")

    def parse_results(self):
        # get results which should return a single list item
        results = self.geo_data.get('results')
        if results and len(results) > 0:
            return results[0]
        else:
            return None

    def get_errors(self):
        errors = []
        if not self.street_number:
            errors.append('street_number')
        if not self.route:
            errors.append('route')
        if not self.city:
            errors.append('city')
        if not self.zip:
            errors.append('zip')
        return errors

    def valid_address(self):
        error_list = self.get_errors()
        if len(error_list) > 0:
            return False
        else:
            return True

    def formatted_address(self):
        if self.valid_address():
            return "{0} {1}, {2}, {3} {4}".format(
                self.street_number,
                self.route,
                self.city,
                self.state,
                self.zip
            )
        else:
            return ""

    def get_all(self):
        if self.status and self.status == "OK":
            return {
                'formatted_address': self.address,
                'street_number': self.street_number,
                'route': self.route,
                'city': self.city,
                'state': self.state,
                'zip': self.zip,
                'country': self.country,
                'county': self.county,
                'neighborhood': self.neighborhood,
                'partial_match': self.partial_match,
                'is_po': self.is_po,
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

    @staticmethod
    def is_pobox(address):
        re_pobox = re.compile(PO_REGEX, re.IGNORECASE)
        matches = re_pobox.search(address)
        if matches:
            return True
        else:
            return False

ENCODE_KEY = 'd$#sbo61#fvq+z(c_6_-7&zf=yo51vwj*3+((a+-6@+d#vwm5_'


def random_num(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def encode(clear):
    key = ENCODE_KEY
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode('utf-8'))


def decode(enc):
    key = ENCODE_KEY
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    enc = enc.decode('utf-8')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def encode_test(max_range):
    # fake last 4 digits of ssn
    for num in range(1, max_range):
        # convert to string
        ssn = str(random_num(4))
        # encode
        encoded_ssn = encode(ssn)
        # decode
        decoded_ssn = decode(encoded_ssn)
        print("{0} : {1} : {2}".format(ssn, encoded_ssn, decoded_ssn))