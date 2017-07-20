import json


NC_BOE_JSON = 'nc_boe_data.json'


def open_json(json_file):
    # open json file we created
    with open(json_file) as data_file:
        return json.load(data_file)


def print_all_json(json_file):
    data = open_json(json_file)
    # loop board of elections
    for boe in data['nc-data']:
        boe_dict = parse_boe(boe)
        if boe_dict:
            print(boe_dict['county'] + ":")
            print("Physical Address: " + boe_dict['physical_address'])
            print("Mailing Address: " + boe_dict['mailing_address'])
            print("Phone #: " + boe_dict['phone'])
            print("Open: " + boe_dict['open'])
            print("Website: " + boe_dict['website'])
            print("\n")


def parse_boe(boe):
    if boe:
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

        return {'county': county,
                'physical_address': physical_address,
                'mailing_address': mailing_address,
                'phone': phone,
                'open': hours,
                'website': url,
                }
