#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Aman Kumar
# Version: 1.0.0 

import re

email_conditions = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
user_email = input("Enter your email: ")

isValid = re.search(email_conditions, user_email)

if(isValid):
    print("Valid Email")
else:
    print("Invalid Email")
