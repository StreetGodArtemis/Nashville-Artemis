import re
import xml.etree.ElementTree as ET
import os

def extract():
    print("🧬 [EXTRACTOR]: PARSING RESEARCH BUFFER...")
    if not os.path.exists('research_buffer.xml'):
        print("❌ [ERROR]: Buffer not found.")
        return

    with open('research_buffer.xml', 'r') as f:
        data = f.read()

    # Regex to find numbers followed by Hz or MHz
    # This is the "Needle" searching the haystack for the math
    frequencies = re.findall(r'(\d+\.?\d*)\s*(?:Hz|hertz|MHz)', data, re.IGNORECASE)
    
    if not frequencies:
        print("⚠️ [WARN]: No specific frequencies detected in this batch.")
        return

    unique_freqs = sorted(list(set([float(f) for f in frequencies])))
    
    print(f"✅ [SUCCESS]: {len(unique_freqs)} UNIQUE HARMONICS IDENTIFIED.")
    for f in unique_freqs:
        # Highlighting potential "Sovereign" matches
        status = "⭐ [MATCH]" if f in [432, 528, 6193] else ""
        print(f"  > {f} Hz {status}")

    with open('harmonics_list.txt', 'w') as f:
        for freq in unique_freqs:
            f.write(f"{freq}\n")
    print("📂 [DATA]: Harmonics saved to harmonics_list.txt")

if __name__ == "__main__":
    extract()
