import time
import numpy as np

import astropy.units as u
import matplotlib.pyplot as plt
import warnings
import pandas as pd
warnings.filterwarnings("ignore", category=FutureWarning)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 30
plt.rcParams['axes.labelsize'] = 30
plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] =30
plt.rcParams['legend.fontsize'] = 30
plt.rcParams['figure.titlesize'] = 12
plt.rcParams['axes.labelweight']='bold'
plt.rcParams['axes.linewidth'] = 3
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.minor.size'] = 3
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.minor.size'] = 3
plt.rcParams['xtick.major.width'] = 5
plt.rcParams['ytick.major.width'] = 3
plt.rcParams['xtick.minor.width'] = 5
plt.rcParams['ytick.minor.width'] = 3

def orbital_distance(stellar_mass_solar_units, orbital_period_days):
    # Convert stellar mass to solar mass units (1 solar mass = 1.989 x 10^30 kg)
    stellar_mass_kg = stellar_mass_solar_units * 1.989e30

    # Convert orbital period to seconds (1 day = 86400 seconds)
    orbital_period_seconds = orbital_period_days * 86400

    # Universal gravitational constant in m^3 kg^-1 s^-2
    G = 6.67430e-11

    # Compute the semi-major axis (orbital distance) in meters
    orbital_distance_meters = ((G * stellar_mass_kg * orbital_period_seconds**2) / (4 * (3.14159**2)))**(1/3)

    # Convert orbital distance to astronomical units (1 AU = 1.496 x 10^11 meters)
    orbital_distance_au = orbital_distance_meters / 1.496e11

    return orbital_distance_au



def bolometric_luminosity(temperature_kelvin, stellar_radius_solar_units):
    # Convert stellar radius to meters (1 solar radius = 6.957 x 10^8 meters)
    stellar_radius_meters = stellar_radius_solar_units * 6.957e8

    # Stefan-Boltzmann constant in W m^-2 K^-4
    stefan_boltzmann_constant = 5.67e-8

    # Calculate luminosity in watts
    luminosity_watts = 4 * 3.14159 * stellar_radius_meters**2 * stefan_boltzmann_constant * temperature_kelvin**4

    # Convert luminosity to solar luminosity (1 solar luminosity = 3.828 x 10^26 W)
    solar_luminosity = luminosity_watts / 3.828e26

    return solar_luminosity


def insolation_flux(semi_major_axis_au, stellar_luminosity_solar_units):
    # Convert semi-major axis to meters (1 AU = 1.496 x 10^11 meters)
    semi_major_axis_meters = semi_major_axis_au * 1.496e11

    # Convert stellar luminosity to watts (1 solar luminosity = 3.828 x 10^26 W)
    stellar_luminosity_watts = stellar_luminosity_solar_units * 3.828e26

    # Calculate insolation flux in watts per square meter
    insolation_flux_w_m2 = stellar_luminosity_watts / (4 * 3.14159 * semi_major_axis_meters**2)

    return insolation_flux_w_m2/1361



df=pd.read_csv('PS_2023.07.31_07.23.30.csv')

RP=df['pl_rade']
per=df['pl_orbper']

mstar=df['st_mass']
rstar=df['st_rad']
teff=df['st_teff']

semi=orbital_distance(mstar,per)

Lbol =  bolometric_luminosity(teff,rstar)
Sbol =insolation_flux(semi,Lbol)

plt.scatter(Sbol,RP)

plt.xlabel('S$_{bol}$  (S$_{\oplus}$)')
plt.ylabel('Planet Radius (R$_\oplus$)')

plt.xscale('log')
plt.yscale('log')

plt.axvline(x=150, lw=3,c='k',ls='--')

plt.xlim(0.1,1e5)


