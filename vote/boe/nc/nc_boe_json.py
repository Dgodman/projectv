import json
import urllib.request
import urllib.parse
from pprint import pprint


# open json file we created
with open('nc_boe_data.json') as data_file:
    data = json.load(data_file)

address_check = ""
# loop board of elections
for boe in data['nc-data']:
    # county name
    county = boe['Name']

    # physical address
    physical_address = boe['PhysicalAddr1']
    if not boe['PhysicalAddr2']:
        physical_address = physical_address + ", {}".format(boe['PhysicalAddrCSZ'])
    else:
        physical_address = physical_address + " {}, {}".format(boe['PhysicalAddr2'], boe['PhysicalAddrCSZ'])

    # mailing address
    mailing_address = boe['MailingAddr1']
    if not boe['MailingAddr2']:
        mailing_address = mailing_address + ", {}".format(boe['MailingAddrCSZ'])
    else:
        mailing_address = mailing_address + " {}, {}".format(boe['MailingAddr2'], boe['MailingAddrCSZ'])
    if mailing_address.split(' ', 1)[0] == "Same":
        mailing_address = physical_address

    # hours of operation
    hours = boe['OfficeHours']

    # phone #
    phone = boe['OfficePhoneNum']
    ext = boe['OfficePhoneNumExt']
    if ext:
        phone = phone + " x" + ext

    # website url
    url = boe['WebsiteAddr']

    address_check = physical_address
    print(county + ":")
    print("Physical Address: " + physical_address)
    print("Mailing Address: " + mailing_address)
    print("Phone #: " + phone)
    print("Hours: " + hours)
    print("Website: " + url)
    print("\n")


#pprint(data['nc-data'][0])

# test google address api
safe_address = urllib.parse.quote_plus(address_check)
GOOGLE_API_URL = "http://maps.googleapis.com/maps/api/geocode/json?"
url = GOOGLE_API_URL + "address={}".format(safe_address)
print(url)
response = urllib.request.urlopen(url)
data = json.load(response)
print(data)