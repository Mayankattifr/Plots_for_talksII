#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:06:09 2018

@author: mayank
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 14:22:30 2018

@author: mayank
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 25
plt.rcParams['axes.labelsize'] = 25
plt.rcParams['xtick.labelsize'] = 25
plt.rcParams['ytick.labelsize'] =25
plt.rcParams['legend.fontsize'] = 24
plt.rcParams['figure.titlesize'] = 16




plt.rcParams['axes.linewidth'] = 3
plt.rcParams['xtick.major.size'] = 18
plt.rcParams['xtick.minor.size'] = 10
plt.rcParams['ytick.major.size'] = 18
plt.rcParams['ytick.minor.size'] = 10

plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['ytick.minor.visible'] = True



df= pd.read_csv("PSCompPars_2023.08.14_02.08.36.csv", )

m=df.disc_year<=2024 
#m=(df.discoverymethod=='Radial Velocity')

stlr=df[m]
plt.figure()

m1=(stlr.discoverymethod=='Radial Velocity')
m2=(stlr.discoverymethod=='Transit')
m3=(stlr.discoverymethod=='Imaging')
m4=(stlr.discoverymethod=='Pulsar Timing')  
m5=(stlr.discoverymethod=='Microlensing')
#m6=(stlr.disc_facility=='Kepler')
#m5=(stlr.disc_facility=='Transiting Exoplanet Survey Satellite (TESS)')

semi=np.array(stlr.pl_orbsmax)
mass=np.array(stlr.pl_bmasse)



plt.figure(figsize=[16,9])





ax = plt.subplot(111)
#ax.hist(semi, bins = 10 ** np.linspace(np.log10(a), np.log10(b), 20),edgecolor='black', linewidth=1.2)
plt.scatter(df.pl_orbsmax,df.pl_bmasse,color='r',edgecolor='k',linewidth=1.5, s =70,label=None)

plt.scatter(stlr.pl_orbsmax[m1],stlr.pl_bmasse[m1],color='b',edgecolor='k',linewidth=1.5, s =70,label='Radial Velocity',zorder=10)
plt.scatter(stlr.pl_orbsmax[m2],stlr.pl_bmasse[m2],color='y',edgecolor='k',linewidth=1.5, s =70,label='Transit',zorder=10)
plt.scatter(stlr.pl_orbsmax[m3],stlr.pl_bmasse[m3],color='g',edgecolor='k',linewidth=1.5, s =70,label='Directly Imaged',zorder=11)
plt.scatter(stlr.pl_orbsmax[m4],stlr.pl_bmasse[m4],color='m',edgecolor='k',linewidth=1.5, s =70,label='Pulsar Timing',zorder=20)
plt.scatter(stlr.pl_orbsmax[m5],stlr.pl_bmasse[m5],color='C1',edgecolor='k',linewidth=1.5, s =70,label='Micro lensing',zorder=30)
plt.legend(title="Method of Discovery",loc=4)

plt.gca().set_xscale("log")
plt.gca().set_yscale("log")
#plt.hist(period,bins=50,edgecolor='black', linewidth=1.2)
plt.ylabel('Planet Mass (in units of Earth mass)')
#plt.xlabel('Planet Radius $(R_\oplus)$')
plt.xlabel('Orbital Distance (in units of Earth-Sun distance)')
plt.text(0.0025,100000, "Total number of Exoplanets: "+str(len(df)) ,  )
plt.text(300,57000, str(date.today()) ,size=40  )
         
plt.xlim(0.002,3500)  
plt.ylim(0.01,30000) 
ax.set_yticks((0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,10000,))
ax.set_yticklabels(('0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000','10000',))

ax.set_xticks((0.003,0.01,0.03,0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,))
ax.set_xticklabels(('0.003','0.01','0.03','0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000',))
       

ss_period=(0.39,0.723,1,1.52,5.2,9.5,19.19,30.1)
ss_radius=(0.055,0.81,1,0.1,317.8,95,14.37,17.14)

ssa2=(0.45,0.8,1.1,1.7,5.5,10,15,35,)
ssa1=(0.05,0.4,0.7,0.11,320,100,6.5,18,)

plt.scatter(ss_period,ss_radius,c='c',edgecolor='k',linewidth=1.5,alpha=1,label='Solar system planets',s=150)

name=('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', )

for label, x, y in zip(name, ssa2, ssa1):
    plt.annotate(label, xy=(x, y), xytext=(x, y), fontsize=20)

def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)
    

plt.savefig('2023.png')



#%%


df= pd.read_csv("PSCompPars_2023.08.14_02.08.36.csv", )

m=df.disc_year<=1992

stlr=df[m]
plt.figure()

m1=(stlr.discoverymethod=='Radial Velocity')
m2=(stlr.discoverymethod=='Transit')
m3=(stlr.discoverymethod=='Imaging')
m4=(stlr.discoverymethod=='Pulsar Timing')  
#m6=(stlr.disc_facility=='Kepler')
m5=(stlr.disc_facility=='Transiting Exoplanet Survey Satellite (TESS)')

semi=np.array(stlr.pl_orbsmax)
mass=np.array(stlr.pl_bmasse)



plt.figure(figsize=[16,9])





ax = plt.subplot(111)
#ax.hist(semi, bins = 10 ** np.linspace(np.log10(a), np.log10(b), 20),edgecolor='black', linewidth=1.2)

#plt.scatter(stlr.pl_orbsmax[m1],stlr.pl_bmasse[m1],color='b',edgecolor='k',linewidth=1.5, s =70,label='Radial Velocity',zorder=1)
#plt.scatter(stlr.pl_orbsmax[m2],stlr.pl_bmasse[m2],color='y',edgecolor='k',linewidth=1.5, s =70,label='Transit')
#plt.scatter(stlr.pl_orbsmax[m3],stlr.pl_bmasse[m3],color='g',edgecolor='k',linewidth=1.5, s =70,label='Directly Imaged')
plt.scatter(stlr.pl_orbsmax[m4],stlr.pl_bmasse[m4],color='m',edgecolor='k',linewidth=1.5, s =70,label='Pulsar Timing',zorder=1)
#plt.scatter(stlr.pl_orbsmax[m6],stlr.pl_bmasse[m6],color='r',edgecolor='k',linewidth=1.5, s =70,label='Kepler')
#plt.scatter(stlr.pl_orbsmax[m5],stlr.pl_bmasse[m5],color='C1',edgecolor='k',linewidth=1.5, s =70,label='TESS')
plt.legend(title="Method of Discovery",loc=4)

plt.gca().set_xscale("log")
plt.gca().set_yscale("log")
#plt.hist(period,bins=50,edgecolor='black', linewidth=1.2)
plt.ylabel('Planet Mass (in units of Earth mass)')
#plt.xlabel('Planet Radius $(R_\oplus)$')
plt.xlabel('Orbital Distance (in units of Earth-Sun distance)')
plt.text(0.0025,100000, "Total number of Exoplanets: "+str(len(stlr)) ,  )
plt.text(300,57000, str(1992) ,size=40  )
         
plt.xlim(0.002,3500)  
plt.ylim(0.01,30000) 
ax.set_yticks((0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,10000,))
ax.set_yticklabels(('0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000','10000',))

ax.set_xticks((0.003,0.01,0.03,0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,))
ax.set_xticklabels(('0.003','0.01','0.03','0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000',))
       

ss_period=(0.39,0.723,1,1.52,5.2,9.5,19.19,30.1)
ss_radius=(0.055,0.81,1,0.1,317.8,95,14.37,17.14)

ssa2=(0.45,0.8,1.1,1.7,5.5,10,15,35,)
ssa1=(0.05,0.4,0.7,0.11,320,100,6.5,18,)

plt.scatter(ss_period,ss_radius,c='c',edgecolor='k',linewidth=1.5,alpha=1,label='Solar system planets',s=150)

name=('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', )

for label, x, y in zip(name, ssa2, ssa1):
    plt.annotate(label, xy=(x, y), xytext=(x, y), fontsize=20)

def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)
    

plt.savefig('1992.png')

#%%

df= pd.read_csv("PSCompPars_2023.08.14_02.08.36.csv", )

m=df.disc_year<=2002

stlr=df[m]
plt.figure()

m1=(stlr.discoverymethod=='Radial Velocity')
m2=(stlr.discoverymethod=='Transit')
m3=(stlr.discoverymethod=='Imaging')
m4=(stlr.discoverymethod=='Pulsar Timing')  
m5=(stlr.discoverymethod=='Microlensing')
#m6=(stlr.disc_facility=='Kepler')
#m5=(stlr.disc_facility=='Transiting Exoplanet Survey Satellite (TESS)')

semi=np.array(stlr.pl_orbsmax)
mass=np.array(stlr.pl_bmasse)



plt.figure(figsize=[16,9])





ax = plt.subplot(111)
#ax.hist(semi, bins = 10 ** np.linspace(np.log10(a), np.log10(b), 20),edgecolor='black', linewidth=1.2)
plt.scatter(stlr.pl_orbsmax,stlr.pl_bmasse,color='r',edgecolor='k',linewidth=1.5, s =70,label=None)

plt.scatter(stlr.pl_orbsmax[m1],stlr.pl_bmasse[m1],color='b',edgecolor='k',linewidth=1.5, s =70,label='Radial Velocity',zorder=10)
plt.scatter(stlr.pl_orbsmax[m2],stlr.pl_bmasse[m2],color='y',edgecolor='k',linewidth=1.5, s =70,label='Transit',zorder=10)
#plt.scatter(stlr.pl_orbsmax[m3],stlr.pl_bmasse[m3],color='g',edgecolor='k',linewidth=1.5, s =70,label='Directly Imaged',zorder=11)
plt.scatter(stlr.pl_orbsmax[m4],stlr.pl_bmasse[m4],color='m',edgecolor='k',linewidth=1.5, s =70,label='Pulsar Timing',zorder=20)
#plt.scatter(stlr.pl_orbsmax[m5],stlr.pl_bmasse[m5],color='C1',edgecolor='k',linewidth=1.5, s =70,label='Micro lensing',zorder=30)
plt.legend(title="Method of Discovery",loc=4)

plt.gca().set_xscale("log")
plt.gca().set_yscale("log")
#plt.hist(period,bins=50,edgecolor='black', linewidth=1.2)
plt.ylabel('Planet Mass (in units of Earth mass)')
#plt.xlabel('Planet Radius $(R_\oplus)$')
plt.xlabel('Orbital Distance (in units of Earth-Sun distance)')
plt.text(0.0025,100000, "Total number of Exoplanets: "+str(len(stlr)) ,  )
plt.text(300,57000, str(2002) ,size=40  )
         
plt.xlim(0.002,3500)  
plt.ylim(0.01,30000) 
ax.set_yticks((0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,10000,))
ax.set_yticklabels(('0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000','10000',))

ax.set_xticks((0.003,0.01,0.03,0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,))
ax.set_xticklabels(('0.003','0.01','0.03','0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000',))
       

ss_period=(0.39,0.723,1,1.52,5.2,9.5,19.19,30.1)
ss_radius=(0.055,0.81,1,0.1,317.8,95,14.37,17.14)

ssa2=(0.45,0.8,1.1,1.7,5.5,10,15,35,)
ssa1=(0.05,0.4,0.7,0.11,320,100,6.5,18,)

plt.scatter(ss_period,ss_radius,c='c',edgecolor='k',linewidth=1.5,alpha=1,label='Solar system planets',s=150)

name=('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', )

for label, x, y in zip(name, ssa2, ssa1):
    plt.annotate(label, xy=(x, y), xytext=(x, y), fontsize=20)

def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)
    

plt.savefig('2002.png')


#%%

df= pd.read_csv("PSCompPars_2023.08.14_02.08.36.csv", )

m=df.disc_year<=2005

stlr=df[m]
plt.figure()

m1=(stlr.discoverymethod=='Radial Velocity')
m2=(stlr.discoverymethod=='Transit')
m3=(stlr.discoverymethod=='Imaging')
m4=(stlr.discoverymethod=='Pulsar Timing')  
m5=(stlr.discoverymethod=='Microlensing')
#m6=(stlr.disc_facility=='Kepler')
#m5=(stlr.disc_facility=='Transiting Exoplanet Survey Satellite (TESS)')

semi=np.array(stlr.pl_orbsmax)
mass=np.array(stlr.pl_bmasse)



plt.figure(figsize=[16,9])





ax = plt.subplot(111)
#ax.hist(semi, bins = 10 ** np.linspace(np.log10(a), np.log10(b), 20),edgecolor='black', linewidth=1.2)
plt.scatter(stlr.pl_orbsmax,stlr.pl_bmasse,color='r',edgecolor='k',linewidth=1.5, s =70,label=None)

plt.scatter(stlr.pl_orbsmax[m1],stlr.pl_bmasse[m1],color='b',edgecolor='k',linewidth=1.5, s =70,label='Radial Velocity',zorder=10)
plt.scatter(stlr.pl_orbsmax[m2],stlr.pl_bmasse[m2],color='y',edgecolor='k',linewidth=1.5, s =70,label='Transit',zorder=10)
plt.scatter(stlr.pl_orbsmax[m3],stlr.pl_bmasse[m3],color='g',edgecolor='k',linewidth=1.5, s =70,label='Directly Imaged',zorder=11)
plt.scatter(stlr.pl_orbsmax[m4],stlr.pl_bmasse[m4],color='m',edgecolor='k',linewidth=1.5, s =70,label='Pulsar Timing',zorder=20)
plt.scatter(stlr.pl_orbsmax[m5],stlr.pl_bmasse[m5],color='C1',edgecolor='k',linewidth=1.5, s =70,label='Micro lensing',zorder=30)
plt.legend(title="Method of Discovery",loc=4)

plt.gca().set_xscale("log")
plt.gca().set_yscale("log")
#plt.hist(period,bins=50,edgecolor='black', linewidth=1.2)
plt.ylabel('Planet Mass (in units of Earth mass)')
#plt.xlabel('Planet Radius $(R_\oplus)$')
plt.xlabel('Orbital Distance (in units of Earth-Sun distance)')
plt.text(0.0025,100000, "Total number of Exoplanets: "+str(len(stlr)) ,  )
plt.text(300,57000, str(2005) ,size=40  )
         
plt.xlim(0.002,3500)  
plt.ylim(0.01,30000) 
ax.set_yticks((0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,10000,))
ax.set_yticklabels(('0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000','10000',))

ax.set_xticks((0.003,0.01,0.03,0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,))
ax.set_xticklabels(('0.003','0.01','0.03','0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000',))
       

ss_period=(0.39,0.723,1,1.52,5.2,9.5,19.19,30.1)
ss_radius=(0.055,0.81,1,0.1,317.8,95,14.37,17.14)

ssa2=(0.45,0.8,1.1,1.7,5.5,10,15,35,)
ssa1=(0.05,0.4,0.7,0.11,320,100,6.5,18,)

plt.scatter(ss_period,ss_radius,c='c',edgecolor='k',linewidth=1.5,alpha=1,label='Solar system planets',s=150)

name=('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', )

for label, x, y in zip(name, ssa2, ssa1):
    plt.annotate(label, xy=(x, y), xytext=(x, y), fontsize=20)

def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)
    

plt.savefig('2005.png')


#%%


df= pd.read_csv("PSCompPars_2023.08.14_02.08.36.csv", )

m=df.disc_year<=1995

stlr=df[m]
plt.figure()

m1=(stlr.discoverymethod=='Radial Velocity')
m2=(stlr.discoverymethod=='Transit')
m3=(stlr.discoverymethod=='Imaging')
m4=(stlr.discoverymethod=='Pulsar Timing')  
m5=(stlr.discoverymethod=='Microlensing')
#m6=(stlr.disc_facility=='Kepler')
#m5=(stlr.disc_facility=='Transiting Exoplanet Survey Satellite (TESS)')

semi=np.array(stlr.pl_orbsmax)
mass=np.array(stlr.pl_bmasse)



plt.figure(figsize=[16,9])





ax = plt.subplot(111)
#ax.hist(semi, bins = 10 ** np.linspace(np.log10(a), np.log10(b), 20),edgecolor='black', linewidth=1.2)
plt.scatter(stlr.pl_orbsmax,stlr.pl_bmasse,color='r',edgecolor='k',linewidth=1.5, s =70,label=None)

plt.scatter(stlr.pl_orbsmax[m1],stlr.pl_bmasse[m1],color='b',edgecolor='k',linewidth=1.5, s =70,label='Radial Velocity',zorder=10)
#plt.scatter(stlr.pl_orbsmax[m2],stlr.pl_bmasse[m2],color='y',edgecolor='k',linewidth=1.5, s =70,label='Transit',zorder=10)
#plt.scatter(stlr.pl_orbsmax[m3],stlr.pl_bmasse[m3],color='g',edgecolor='k',linewidth=1.5, s =70,label='Directly Imaged',zorder=11)
plt.scatter(stlr.pl_orbsmax[m4],stlr.pl_bmasse[m4],color='m',edgecolor='k',linewidth=1.5, s =70,label='Pulsar Timing',zorder=20)
#plt.scatter(stlr.pl_orbsmax[m5],stlr.pl_bmasse[m5],color='C1',edgecolor='k',linewidth=1.5, s =70,label='Micro lensing',zorder=30)
plt.legend(title="Method of Discovery",loc=4)

plt.gca().set_xscale("log")
plt.gca().set_yscale("log")
#plt.hist(period,bins=50,edgecolor='black', linewidth=1.2)
plt.ylabel('Planet Mass (in units of Earth mass)')
#plt.xlabel('Planet Radius $(R_\oplus)$')
plt.xlabel('Orbital Distance (in units of Earth-Sun distance)')
plt.text(0.0025,100000, "Total number of Exoplanets: "+str(len(stlr)) ,  )
plt.text(300,57000, str(1995) ,size=40  )
         
plt.xlim(0.002,3500)  
plt.ylim(0.01,30000) 
ax.set_yticks((0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,10000,))
ax.set_yticklabels(('0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000','10000',))

ax.set_xticks((0.003,0.01,0.03,0.1,0.3,1,3,10 ,30, 100,300 ,1000,3000,))
ax.set_xticklabels(('0.003','0.01','0.03','0.1','0.3','1','3','10' ,'30', '100','300' ,'1000','3000',))
       

ss_period=(0.39,0.723,1,1.52,5.2,9.5,19.19,30.1)
ss_radius=(0.055,0.81,1,0.1,317.8,95,14.37,17.14)

ssa2=(0.45,0.8,1.1,1.7,5.5,10,15,35,)
ssa1=(0.05,0.4,0.7,0.11,320,100,6.5,18,)

plt.scatter(ss_period,ss_radius,c='c',edgecolor='k',linewidth=1.5,alpha=1,label='Solar system planets',s=150)

name=('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', )

for label, x, y in zip(name, ssa2, ssa1):
    plt.annotate(label, xy=(x, y), xytext=(x, y), fontsize=20)

def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)
    

plt.savefig('1995.png')
