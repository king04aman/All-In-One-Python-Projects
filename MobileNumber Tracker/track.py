#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Aman Kumar
# Version: 1.0.0 

import phonenumbers
from phonenumbers import timezone, carrier, geocoder

number = input("Enter number to track (with +91): ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carr = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, 'en')

print("STD Code: ", phone.country_code)
print("Number: ", phone.national_number)
print("Region: ", time)
print("Carrier: ", carr)
print("Country: ", reg)
