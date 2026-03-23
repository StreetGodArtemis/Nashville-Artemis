import re
import os

def deep_scan():
    print("🧬 [DEEP SCAN]: PIERCING RESEARCH BUFFER...")
    if not os.path.exists('research_buffer.xml'):
        print("❌ [ERROR]: Buffer not found.")
        return

    with open('research_buffer.xml', 'r') as f:
        data = f.read()

    # Regex patterns for Hz, MHz, kHz, and decimal contexts
    patterns = [
        r'(\d+\.?\d*)\s*(?:Hz|hertz|MHz|kHz)',
        r'(?:frequency|rate|pulse)\s*(?:of|at)?\s*(\d+\.?\d*)',
        r'(\d+\.?\d*)\s*(?:nm|nanometers)'
    ]
    
    found_values = []
    for pattern in patterns:
        matches = re.findall(pattern, data, re.IGNORECASE)
        found_values.extend([float(m) for m in matches])

    # If the specific search fails, grab all floating point metrics
    if not found_values:
        print('⚠️ [WARN]: Data is still too "noisy". Expanding search to raw metrics...')
        found_values = [float(f) for f in re.findall(r'\b\d+\.\d+\b', data)]

    unique_vals = sorted(list(set(found_values)))
    
    print(f"✅ [SUCCESS]: {len(unique_vals)} METRIC POINTS IDENTIFIED.")
    for v in unique_vals:
        # Check for specific "Sovereign" markers in the data
        marker = "⭐" if v in [528.0, 432.0, 1.618] else ""
        print(f"  > Value: {v} {marker}")

    with open('harmonics_list.txt', 'w') as f:
        for v in unique_vals:
            f.write(f"{v}\n")
    print("📂 [DATA]: Metrics saved to harmonics_list.txt")

if __name__ == "__main__":
    deep_scan()
