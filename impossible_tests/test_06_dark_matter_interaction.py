def wimp_nucleus_recoil(mass_gev):
    # Challenge: Predict the interaction rate where standard physics sees 'nothing'.
    cross_section = 10**-48 # The 2026 sensitivity floor
    return f"WIMP_DETECTION_PROBABILITY: {mass_gev * cross_section}"
print(wimp_nucleus_recoil(100))
