import requests
import xml.etree.ElementTree as ET
import pandas as pd
import os

# URL and namespace
url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"
ns = {"ttv": "http://www.titantv.com/"}

# Output path
output_excel = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\titantv_full_schedule1.xlsx"

def extract_show_data(show):
    """Flatten <Show> attributes and nested tags into a flat dictionary."""
    record = {}

    # Show attributes
    for attr, value in show.attrib.items():
        record[attr] = value

    # Child elements
    for child in show:
        tag = child.tag.split("}")[-1]

        # Handle Cast (repeating with role attribute)
        if tag == "Cast":
            role = child.attrib.get("role", "Unknown")
            record[f"Cast_{role}"] = record.get(f"Cast_{role}", []) + [child.text.strip()] if child.text else []

        # Handle Category (multiple with lang/type)
        elif tag == "Category":
            lang = child.attrib.get("lang", "unk")
            type_ = child.attrib.get("type", "unk")
            key = f"Category_{lang}_{type_}"
            record[key] = record.get(key, []) + [child.text.strip()] if child.text else []

        # Handle ParentalRating (region/dimension)
        elif tag == "ParentalRating":
            dim = child.attrib.get("ratingDimension", "Unknown")
            record[f"Parental_{dim}"] = child.attrib.get("ratingValue", "")

        # Handle simple child elements
        elif len(child) == 0 and child.text:
            record[tag] = child.text.strip()

        # Handle <Audio> and <Rating> attributes
        elif tag in {"Audio", "Rating", "ClosedCaption"}:
            for attr, val in child.attrib.items():
                record[f"{tag}_{attr}"] = val

    # Convert list values to string for Excel export
    for key, value in record.items():
        if isinstance(value, list):
            record[key] = "; ".join(value)

    return record

# Request and parse XML
response = requests.get(url)
response.raise_for_status()
root = ET.fromstring(response.content)

channel_data = {}

# Process each Channel
for channel in root.findall(".//ttv:Channel", ns):
    channel_id = channel.attrib.get("channelId", "Unknown")
    callsign = channel.attrib.get("callsign", "Unknown")
    sheet_name = f"{channel_id}_{callsign}"[:31]  # Excel sheet name limit

    shows = channel.findall("ttv:Show", ns)
    rows = [extract_show_data(show) for show in shows]

    if rows:
        df = pd.DataFrame(rows)
        channel_data[sheet_name] = df

# Write all to Excel
with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
    for sheet_name, df in channel_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"\n✅ Excel saved at:\n{output_excel}")
