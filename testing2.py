import requests
import xml.etree.ElementTree as ET

# Target setup
ns = {"ttv": "http://www.titantv.com/"}
target_channel_id = "2036768"
url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

# Fetch the XML
response = requests.get(url, stream=True)
response.raw.decode_content = True

context = ET.iterparse(response.raw, events=("start", "end"))
_, root = next(context)

# Set to store unique field names
field_names = set()

def collect_field_names(elem, parent_prefix=""):
    # Add attribute names
    for attr in elem.attrib:
        field_names.add(f"{parent_prefix}@{attr}")
    # Add element tag
    tag = elem.tag.split("}")[-1]
    full_path = f"{parent_prefix}{tag}"
    field_names.add(full_path)
    # Recurse
    for child in elem:
        collect_field_names(child, f"{full_path}:")  # add path depth

# Parse the XML
for event, elem in context:
    if event == "end" and elem.tag.endswith("Channel") and elem.attrib.get("channelId") == target_channel_id:
        for show in elem.findall("ttv:Show", ns):
            collect_field_names(show)
        root.clear()

# Save to Notepad file
notepad_path = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\show_field_names.txt"
with open(notepad_path, "w") as f:
    for name in sorted(field_names):
        f.write(name + "\n")

print(f"✔ Field names extracted and saved to {notepad_path}")
