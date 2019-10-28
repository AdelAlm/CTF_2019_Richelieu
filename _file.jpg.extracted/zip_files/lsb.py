#!/usr/bin/env python3

import sys
from PIL import Image

def extract(src):
    
    img = Image.open(src)
    
    dimX,dimY = img.size
    data = img.load()
    all_bits = ''
    
    for y in range(dimX):
        for x in range(dimY):
            r,g,b = data[y,x]
            r_bit = bin(r)[2:].zfill(8)[-1] # RED last bit
            g_bit = bin(g)[2:].zfill(8)[-1] # GREEN last bit
            b_bit = bin(b)[2:].zfill(8)[-1] # BLUE last bit
            all_bits += r_bit + g_bit + b_bit
    
    tab_all_bits = [all_bits[i:i+8] for i in range(0, len(all_bits), 8)]
    
    return''.join([chr(int(c,2)) for c in tab_all_bits])

print('Start')
open('lsb_data', 'wb').write(extract(src='lsb_RGB.png').encode())
print('Done')
