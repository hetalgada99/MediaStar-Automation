import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Target setup
ns = {"ttv": "http://www.titantv.com/"}
target_channel_id = "2036768"
url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

# Fetch the data
response = requests.get(url, stream=True)
response.raw.decode_content = True

# Initialize parsing
context = ET.iterparse(response.raw, events=("start", "end"))
_, root = next(context)

# Recursive function to extract attributes and text from a Show element
def flatten_element(elem, parent_prefix=""):
    data = {}
    # Include attributes
    for key, val in elem.attrib.items():
        data[f"{parent_prefix}@{key}"] = val
    # Include text if it's meaningful
    if elem.text and elem.text.strip():
        data[parent_prefix.strip(":")] = elem.text.strip()

    # Recurse into children
    for child in elem:
        tag = child.tag.split("}")[-1]  # Remove namespace
        new_prefix = f"{parent_prefix}{tag}:"
        child_data = flatten_element(child, new_prefix)
        data.update(child_data)
    return data

# Parse and collect
all_shows = []

for event, elem in context:
    if event == "end" and elem.tag.endswith("Channel") and elem.attrib.get("channelId") == target_channel_id:
        for show in elem.findall("ttv:Show", ns):
            show_dict = flatten_element(show)
            # Add channel info
            show_dict["channelId"] = elem.attrib.get("channelId")
            show_dict["callsign"] = elem.attrib.get("callsign")
            show_dict["channelNumber"] = elem.attrib.get("channelNumber")
            all_shows.append(show_dict)
        root.clear()

# Convert to DataFrame
df = pd.DataFrame(all_shows)

# Save to Excel
file_path = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\media_star_shows1.xlsx"
df.to_excel(file_path, index=False)

print("✔ All fields and subfields scraped and saved to Excel.")
