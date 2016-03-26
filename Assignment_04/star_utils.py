'''Star utils module
'''

# constants
grav_const = 6.67259e-8
grav_const_unit = 'cm^3 g^-1 s^-2'

# constants for astronomy
rsun_cm = 6.955e10
rsun_cm_s = 'cm'
lsun_erg_s = 3.839e33
lsun_erg_s_unit = 'erg/s'
msun_g = 1.9891e33
msun_unit = 'erg s^-1'
mass_earth_g=5.9742e27

radiation_constant = 7.566e-15
radiation_constant_unit = 'erg cm^-3 K^-4'
speed_light = 2.998e10
speed_light_unit = 'cm s^-1'
grav_const = 6.67259e-8
grav_const_unit = 'cm^3 g^-1 s^-2'

# constants for physics
mass_H_atom=1.674e-24
mass_H_atom_unit='g'
mass_electron=9.10938291E-28
mass_electron_unit='g'
planck_constant_h=6.62606957E-27
planck_constant_h_unit='erg s'
atomic_mass_unit=1.660538921e-24
atomic_mass_unit_unit='g'
boltzmann_constant=1.3806488e-16
boltzmann_constant_unit='erg K^-1'
avogadro_constant=6.02214179e23
avogadro_constant_unit='mol^-1'

def P_ideal_gas(rho,T,mu=1.):
    '''
    ideal gas EOS for astronomy
        
    P = (R/mu) * rho * T
    R: gas constant
    
    parameters
    ----------
    mu : float
        mean molecular weight [in units of the atomic mass unit]
    rho : float
        density [in cgs units]
    T : float
        temperature [K]
    '''

    print("temperature = ", T)
    print("rho = ",rho)
    R = 83144621.4563013 # cgs units [erg K^-1 mol^-1]
    P_ideal = (R/mu) * rho * T
    
    return P_ideal

def Derivative(f,x,x_prec=0.01):
    '''
    Numerical derivative of function f
    '''

    dfdx = (f(x+x_prec)-f(x))/x_prec
    return dfdx

# functions
def linestyle(i,a=5,b=3):
    ''' 
    provide one out of 25 unique combinations of style, color and mark

    use in combination with markevery=a+mod(i,b) to add spaced points,
    here a would be the base spacing that would depend on the data
    density, modulated with the number of lines to be plotted (b)

    Parameters
    ----------
    i : integer
        Number of linestyle combination - there are many....
    a : integer
        Spacing of marks.  The default is 5.
    b : integer
        Modulation in case of plotting many nearby lines.  The default
        is 3.

    Examples
    --------
    
    >>> plot(x,sin(x),linestyle(7)[0], markevery=linestyle(7)[1])


    (c) 2014 FH
    '''
    import scipy as sc

    lines=['-','--','-.',':']
    points=['v','^','<','>','1','2','3','4','s','p','*','h','H','+','x','D','d','o']
    colors=['b','g','r','c','m','k']
    ls_string = colors[sc.mod(i,6)]+lines[sc.mod(i,4)]+points[sc.mod(i,18)]
    mark_i    = a+sc.mod(i,b)
    return ls_string,mark_i
