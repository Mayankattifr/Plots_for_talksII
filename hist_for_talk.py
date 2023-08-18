#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:05:20 2023

@author: mayank
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 35
plt.rcParams['axes.labelsize'] = 35
plt.rcParams['xtick.labelsize'] = 35
plt.rcParams['ytick.labelsize'] =35
plt.rcParams['legend.fontsize'] = 24
plt.rcParams['figure.titlesize'] = 16




plt.rcParams['axes.linewidth'] = 3
plt.rcParams['xtick.major.size'] = 18
plt.rcParams['xtick.minor.size'] = 10
plt.rcParams['ytick.major.size'] = 18
plt.rcParams['ytick.minor.size'] = 10

plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['ytick.minor.visible'] = True



df= pd.read_csv("PS_2023.08.14_00.24.25.csv", )

a=0.5
b=10000
plt.figure(figsize=[16,9])
plt.hist(df['pl_orbper'], bins = 10 ** np.linspace(np.log10(a), np.log10(b), 20),edgecolor='black', linewidth=1.5)
plt.gca().set_xscale("log")
#plt.hist(period,bins=50,edgecolor='black', linewidth=1.2)
plt.ylabel('Number of planets')
plt.xlabel('Period (days)')
plt.axvline(x=365,c='b',ls='--',lw=5)

plt.text(375, 365, 'Earth', color='k', rotation=90,)

plt.axvline(x=88,c='r',ls='--',lw=5)

plt.text(95, 365, 'Mercury', color='k', rotation=90,)

plt.axvline(x=4332,c='k',ls='--',lw=5)
plt.text(4500, 365, 'Jupiter', color='k', rotation=90,)
plt.title('Total number of planets = '+str(len(df)))
plt.savefig('period.png',bbox_inches='tight')



df= pd.read_csv("PS_2023.08.14_00.24.25.csv", )

a=0.5
b=30
m=df['pl_rade']>0
df=df[m]
plt.figure(figsize=[16,9])
plt.hist(df['pl_rade'], bins = 10 ** np.linspace(np.log10(a), np.log10(b), 20),edgecolor='black', linewidth=1.5)
plt.gca().set_xscale("log")
#plt.hist(period,bins=50,edgecolor='black', linewidth=1.2)
plt.ylabel('Number of planets')
plt.xlabel('Radius (R$_\oplus$)')
plt.axvline(x=1,c='b',ls='--',lw=5)

plt.text(1.1, 500, 'Earth', color='k', rotation=90,)

plt.axvline(x=4,c='r',ls='--',lw=5)

plt.text(4.1, 500, 'Neptune', color='k', rotation=90,)

plt.axvline(x=11.2,c='k',ls='--',lw=5)
plt.text(11.5, 500, 'Jupiter', color='k', rotation=90,)
plt.title('Total number of planets = '+str(len(df)))
plt.savefig('radius.png',bbox_inches='tight')
