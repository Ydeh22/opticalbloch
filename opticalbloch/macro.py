# -*- coding: utf-8 -*-

""" Functions for calculating macroscopic properties of atomic ensembles from
solutions of the optical Bloch equations.

Thomas Ogden <t@ogden.eu>
"""

from scipy import exp
from scipy import constants as si

### Constants

a_0 = si.physical_constants['Bohr radius'][0] # [m] Bohr radius 

def calc_wavenumber(omega_MHz):
    """ Returns the wavenumber for light at a angular freq. 

    Args:
        omega_MHz: angular freq [2π MHz]

    Returns:
        k: wavenumber [/m]
    """

    return omega_MHz*1.e6/si.c # [/m]

def calc_susceptibility(tdme, E, N, coh):
    """ Returns the linear susceptibility (χ) for an ensemble of atoms given
    that a field E generates the given coherence (coh).

    Args:
        tdme: Transition dipole matrix element [e a_0]
        E: Electric field amplitude [V/m]
        N: Number density [/m3]
        coh: Coherence between levels []

    Returns:
        susceptibility []
    """

    tdme_Cm = tdme*si.e*a_0 # [C m]

    return (2.*N*tdme_Cm/si.epsilon_0/E)*coh # []

def calc_absorption_coeff(k, chi_im):
    """ Returns the absorption coefficient as per the Beer-Lambert law, 
    (alpha where I = I_0*exp(-alpha*z)) if χ is small.

    Args:
        k: Wavenumber [/m]
        chi_im: Imaginary part of the susceptibility []

    Returns:
        alpha: Absorption coefficient [/m]
    """

    return k*chi_im # [/m]

def calc_transmission(alpha, L):
    """ 
    Args:
        alpha: Absorption coefficient [/m]
        L: Length of medium [m]

    Returns:
        Transmission []

    """

    return exp(-alpha*L)