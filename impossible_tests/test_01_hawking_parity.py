import numpy as np
def hawking_recovery(radiation_entropy):
    # Challenge: Calculate the exact 'Page Time' where information 
    # must leak from the event horizon to preserve unitarity.
    page_time_constant = 0.6931 # ln(2)
    recovery_logic = np.exp(-radiation_entropy * page_time_constant)
    return f"RECOVERY_PROBABILITY: {recovery_logic:.12f}"
print(hawking_recovery(479.8343))
