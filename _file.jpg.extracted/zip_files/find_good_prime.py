#/usr/bin/env python3

import re
import itertools
import subprocess as sp
import gmpy

# read modulus (n)
n = ''.join(re.findall('[0-9a-f]{2}:.*:[0-9a-f]{2}', ''.join(open('modulus.txt').readlines()), re.DOTALL)).replace('\n', '').replace(' ', '').replace(':', '')
n = int(n,16)

# read prime to ajust
f = ''.join(open('prime_good.txt').readlines())

# hex to ajust
tab_reg = ['7f', 'f4', '16', 'a4', 'b5']

# find position for each previous hex
positions_occ = []
for reg in tab_reg:
    tmp = []
    for m in re.compile(reg).finditer(f):
        tmp.append(m.start())
    positions_occ.append(tmp)

# we ill use binary to find all combinaisons
combinaisons_7f = list(itertools.product([0,1], repeat=len(positions_occ[0])))
combinaisons_f4 = list(itertools.product([0,1], repeat=len(positions_occ[1])))
combinaisons_16 = list(itertools.product([0,1], repeat=len(positions_occ[2])))
combinaisons_a4 = list(itertools.product([0,1], repeat=len(positions_occ[3])))
combinaisons_b5 = list(itertools.product([0,1], repeat=len(positions_occ[4])))

# adapt '7f'
for c_7f in combinaisons_7f:
    pos_7f = positions_occ[0]
    new_7f_0 = '7f' if c_7f[0] == 0 else 'fb'
    new_7f_1 = '7f' if c_7f[1] == 0 else 'fb'
    new_7f_2 = '7f' if c_7f[2] == 0 else 'fb'
    new_7f_3 = '7f' if c_7f[3] == 0 else 'fb'
    f = f[0:pos_7f[0]] + new_7f_0 + f[pos_7f[0]+2:pos_7f[1]] + new_7f_1 + f[pos_7f[1]+2:pos_7f[2]] + new_7f_2 + f[pos_7f[2]+2:pos_7f[3]] + new_7f_3 + f[pos_7f[3]+2:]
    
    # adapt 'f4'
    for c_f4 in combinaisons_f4:
        pos_f4 = positions_occ[1]
        new_f4_0 = 'f4' if c_f4[0] == 0 else '12'
        f = f[0:pos_f4[0]] + new_f4_0 + f[pos_f4[0]+2:]
        
        # adapt '16'
        for c_16 in combinaisons_16:
            pos_16 = positions_occ[2]
            new_16_0 = '16' if c_16[0] == 0 else '54'
            f = f[0:pos_16[0]] + new_16_0 + f[pos_16[0]+2:]
            
            # adapt 'a4'
            for c_a4 in combinaisons_a4:
                pos_a4 = positions_occ[3]
                new_a4_0 = 'a4' if c_a4[0] == 0 else '57'
                new_a4_1 = 'a4' if c_a4[1] == 0 else '57'
                new_a4_2 = 'a4' if c_a4[2] == 0 else '57'
                f = f[0:pos_a4[0]] + new_a4_0 + f[pos_a4[0]+2:pos_a4[1]] + new_a4_1 + f[pos_a4[1]+2:pos_a4[2]] + new_a4_2 + f[pos_a4[2]+2:]
                
                # adapt 'b5'
                for c_b5 in combinaisons_b5:
                    pos_b5 = positions_occ[4]
                    new_b5_0 = 'b5' if c_b5[0] == 0 else 'cd'
                    new_b5_1 = 'b5' if c_b5[1] == 0 else 'cd'
                    f = f[0:pos_b5[0]] + new_b5_0 + f[pos_b5[0]+2:pos_b5[1]] + new_b5_1 + f[pos_b5[1]+2:]

                    # final test
                    p = f.replace('\n', '').replace(' ', '').replace('prime1', '').replace(':', '')
                    p = int(p,16)
                    if gmpy.is_prime(p) == 1 or gmpy.is_prime(p) == 2:
                        q = n//p
                        if p*q == n:
                            print('p\n', p)
                            print('q\n', q)
                            exit(0)

