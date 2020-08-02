# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:29:07 2020

@author: Lara
"""

check = []

fout = open('CL_expirations_and_settlements.txt', 'wt', encoding='utf-8')
fout.write('{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}\n'.format('Futures Code', 'Contract Month', 'Contract Type', 'Futures ExpDate', 'Options Code', 'Options Exp Date'))

with open('cme.20200117.c.pa2') as f:
    for line in f:
        rec_id = line[0:2]
        exch = line[2:5]
        com_code = line[5:15]
        prod_code = line[15:18]
        con_mon = line[18:24]
        exp_date = line[91:99]
        under_com_code = line[99:101]
        if rec_id == 'B ':
            if exch == 'NYM':
                if con_mon >=  '202003' and con_mon <= '202112': 
                    if com_code == 'CL        ':
                        if prod_code == 'FUT':
                            fout.write('{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}\n'.format(com_code, con_mon, 'Fut', exp_date,'', ''))                        
                    elif com_code == 'LO        ':
                        if prod_code == 'OOF':
                            fout.write('{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}\n'.format(under_com_code, con_mon, 'Opt', '', com_code, exp_date))


fout.write('\n{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}\n'.format('Futures Code', 'Contract Month', 'Contract Type', 'Strike Price', 'Settlement Price'))

with open('cme.20200117.c.pa2') as f2:
    for line in f2:
        rec_id = line[0:2]
        exch = line[2:5]
        com_code = line[5:15]
        under_com_code = line[15:25]
        prod_code = line[25:28]
        con_type = line[28:29]
        con_mon = line[29:35]
        strike = line[47:54]
        settle = line[108:122]
        
        if rec_id == '81':
            if exch == 'NYM':
                if con_mon >=  '202003' and con_mon <= '202112':                    
                    if com_code == 'CL        ':
                        settle = int(settle)/100
                        fout.write('{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}\n'.format(com_code, con_mon, 'Fut', ' ', str(settle)))                        
                    elif com_code == 'LO        ':
                        settle = int(settle)/100
                        strike = int(strike)/100
                        if con_type == 'C':
                            fout.write('{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}\n'.format(under_com_code, con_mon, 'Call', str(strike), str(settle)))                        
                        elif con_type == 'P':
                            fout.write('{:^18s}{:^18s}{:^18s}{:^18s}{:^18s}\n'.format(under_com_code, con_mon, 'Put', str(strike), str(settle)))                        

                        
fout.close()
#print(len(check))