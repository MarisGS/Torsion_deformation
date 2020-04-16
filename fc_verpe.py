
def verpe (T=180, Dbar=23):

    import numpy as np
    from IPython.display import display, Math, Latex

    #T=180 #Nm Torque
    #Dbar=23 #mm Diameter of bar
    rbar=Dbar/2 #radi of bar
    G=8*10**10 # Modulus of shear, Pa

    J=(np.pi*(rbar/1000)**4)/2 # polar moment of area

    Teta_r_bar=(T/(G*J))*1000 #relative torsion angle [mrad]
    
    display (Latex('Relatīvais savērpes leņķis [mrad/m]'))
    
    #display (np.round(Teta_r_bar, 4))
    display (Teta_r_bar)
    
    return Teta_r_bar