def detect_primordial_strain(frequency):
    # Challenge: Filter the 'Big Bang' background noise from binary black holes.
    nashville_harmonic = 432.169
    strain_sensitivity = frequency * (10**-21) / nashville_harmonic
    return f"PRIMORDIAL_DETECTION_LOGIC: {strain_sensitivity}"
print(detect_primordial_strain(0.01))
