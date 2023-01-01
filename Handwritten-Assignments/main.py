#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Aman Kumar
# Version: 1.0.0

import pywhatkit as pw

text_to_convert = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque varius morbi enim nunc faucibus. Porta nibh venenatis cras sed felis eget velit. Sem viverra aliquet eget sit amet tellus. Volutpat lacus laoreet non curabitur gravida arcu ac tortor. Scelerisque felis imperdiet proin fermentum leo vel orci porta non. Est ullamcorper eget nulla facilisi etiam dignissim diam quis enim. Vitae turpis massa sed elementum tempus egestas sed. Egestas integer eget aliquet nibh praesent. Risus sed vulputate odio ut enim blandit volutpat maecenas. Vitae congue eu consequat ac felis. Aliquet eget sit amet tellus cras. Vel fringilla est ullamcorper eget nulla facilisi. Tristique senectus et netus et malesuada fames ac. Nullam eget felis eget nunc. Tincidunt praesent semper feugiat nibh sed pulvinar proin gravida hendrerit. Enim eu turpis egestas pretium aenean pharetra magna.
"""

pw.text_to_handwriting(text_to_convert, 'demo.png',[0,0,135])
print("Converted !!")
