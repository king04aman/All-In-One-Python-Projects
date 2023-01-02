#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Aman Kumar
# Version: 1.0.0 

import qrcode as qr

qrImg = qr.make("https://github.com/king04aman/All-In-One-Python-Projects/")
qrImg.save('demo.png')
