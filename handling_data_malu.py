#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Data Reduction and Adjustments

    @author:  Maria Luiza Linhares Dantas
    @date:    2015.10.14
    @version: 0.0.1

    This program is an overall example of data analysis using Python.

"""
# =====================================================================================================================

import matplotlib.pyplot as plt
import numpy as np

# =====================================================================================================================

def flux(magnitude, wavelength):
    flux = (2.997E18/(wavelength ** 2.)) * 10.**(-0.4 * (magnitude + 48.60)) # In erg s^-1 cm^-2 Angstrom^-1
    return flux
    
# =====================================================================================================================

# Main thread
if __name__ == '__main__':

    # Configuring the inputs ------------------------------------------------------------------------------------------
    mydata = np.loadtxt('mydata.txt')
    
    objectid = mydata[:, 0].astype(long)
    mag_ab_g = mydata[:, 1].astype(float)
    mag_ab_r = mydata[:, 2].astype(float)
    mag_abs_r= mydata[:, 3].astype(float)
    redshift = mydata[:, 4].astype(float)
    
    ## ALTERNATIVELY --------------------------------------------------------------------------------------------------
    # mydata_path = '/home/fulano_de_tal/folder1/folder2/mydata.txt'
    # objectid = np.loadtxt(mydata_path, usecols=[0], dtype=long)
    # mag_ab_g = np.loadtxt(mydata_path, usecols=[1])
    
    # A few calculations -----------------------------------------------------------------------------------------------
    average_redshift = np.average(redshift)  # Calculates the average redshift of the sample
    print average_redshift                   # Printing the results
    
    mag_abs_r_std = np.std(mag_abs_r)        # Calculates the standard deviation of absolute magnitude
    print '%.4f' % mag_abs_r_std             # Prints it with 4 decimal characters
    
    # Using my function -----------------------------------------------------------------------------------------------
    wavelength_g = 4770.                     # Effective wavelength in Angstroms for the SDSS u band
    flux_u = flux(mag_ab_g, wavelength_g)
    print flux_u[1:10]

    # Plots -----------------------------------------------------------------------------------------------------------
    ## Plot01
    plt.plot(mag_abs_r, mag_ab_g - mag_ab_r, 'o', markersize=15, alpha=0.5, color='#FF0066')
    plt.title('Diagrama cor-magnitude', fontsize=15)
    #plt.legend(r"Diagrama cor-magnitude", loc='best', numpoints=1)
    plt.ylabel(r"g-r", fontsize=20)
    plt.xlabel(r"$\rm{M_{r}}$", fontsize=20)
    plt.tick_params('both', labelsize='20')
    plt.grid(alpha = 0.5)
    plt.show()
    
    # Or... ----------------------------------------------------------------------------------------------------------
    color = mag_ab_g - mag_ab_r
    
    index_red   = np.where(color > 0.75)
    index_green = np.where((color <= 0.75) * (color > 0.5))
    index_blue  = np.where(color < 0.5)
    
    ## Plot02
    plot01, = plt.plot(mag_abs_r[index_red], color[index_red], 'o', markersize=15, alpha=0.5, color='#FF0000')
    plot02, = plt.plot(mag_abs_r[index_green], color[index_green], 'o', markersize=15, alpha=0.5, color='#00CC00')
    plot03, = plt.plot(mag_abs_r[index_blue], color[index_blue], 'o', markersize=15, alpha=0.5, color='#0033CC')
    plt.legend([plot01, plot02, plot03], [r"Red Sequence", r"Green Valley", r"Blue Cloud"], loc='best', numpoints=1)
    plt.title('Diagrama cor-magnitude', fontsize=15)
    plt.ylabel(r"g-r", fontsize=20)
    plt.xlabel(r"$\rm{M_{r}}$", fontsize=20)
    plt.tick_params('both', labelsize='20')
    plt.grid(alpha = 0.5)
    plt.show()
    
    ## Plot03
    plt.hist(mag_ab_g - mag_ab_r, bins=40, color='red', alpha=0.8)
    plt.xlabel(r"g-r", fontsize=20)
    plt.ylabel(r"Frequência".decode('utf8'), fontsize=20)
    plt.tick_params('both', labelsize='20')
    plt.grid(alpha = 0.5)
    plt.show()
    
    # Or... ----------------------------------------------------------------------------------------------------------
    
    ## Plot04
    fig, axes = plt.subplots(nrows=2, ncols=1)
    fig.tight_layout()           # The above lines are used only to make the plots better adjusted.
    
    plt.subplot(2, 1, 1)
    plot01, = plt.plot(mag_abs_r[index_red], color[index_red], 'o', markersize=15, alpha=0.5, color='#FF0000')
    plot02, = plt.plot(mag_abs_r[index_green], color[index_green], 'o', markersize=15, alpha=0.5, color='#00CC00')
    plot03, = plt.plot(mag_abs_r[index_blue], color[index_blue], 'o', markersize=15, alpha=0.5, color='#0033CC')
    plt.legend([plot01, plot02, plot03], [r"Red Sequence", r"Green Valley", r"Blue Cloud"], loc='best', numpoints=1)
    plt.title('Diagrama cor-magnitude', fontsize=15)
    plt.ylabel(r"g-r", fontsize=10)
    plt.xlabel(r"$\rm{M_{r}}$", fontsize=10)
    plt.tick_params('both', labelsize='10')
    plt.grid(alpha = 0.5)

    plt.subplot(2, 1, 2)
    plt.hist(mag_ab_g - mag_ab_r, bins=40, color='red', alpha=0.8)
    plt.xlabel(r"g-r", fontsize=10)
    plt.ylabel(r"Frequência".decode('utf8'), fontsize=10)
    plt.tick_params('both', labelsize='10')
    plt.grid(alpha = 0.5)
    
    plt.show()
    
__author__ = 'mldantas'

