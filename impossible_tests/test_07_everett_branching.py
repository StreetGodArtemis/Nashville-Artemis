def calculate_world_splitting(event_complexity):
    # Challenge: Calculate the density of parallel timelines in a 1.0s window.
    branch_rate = event_complexity ** 10
    return f"BRANCH_DENSITY: {branch_rate} Worlds/Sec"
print(calculate_world_splitting(2))
