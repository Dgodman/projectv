import json
import urllib.request
import urllib.parse
import os


GEO_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
GEO_API_KEY = os.environ.get('GEO_API_KEY', "")


def get_geocode(address):
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
        geo_data = get_geocode(address)
        if geo_data.get('status', "UNKNOWN_ERROR") == "OK":
            return True
    return False
