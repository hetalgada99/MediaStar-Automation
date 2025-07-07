import requests
import xml.etree.ElementTree as ET

url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

# Stream the XML response
response = requests.get(url, stream=True)
response.raw.decode_content = True  # Ensure correct decoding

# Define the TitanTV namespace
ns = {"ttv": "http://www.titantv.com/"}

# Use a set to store unique channel IDs
unique_channels = set()

# Parse the XML efficiently
context = ET.iterparse(response.raw, events=("start", "end"))

# Iterate through the XML
for event, elem in context:
    if event == "end" and elem.tag.endswith("Channel"):  # Extracting unique channel IDs
        channel_id = elem.attrib.get("channelId")
        if channel_id:
            unique_channels.add(channel_id)
        elem.clear()  # Free memory after processing each <Channel> element

del context  # Cleanup

# Print results
print(f"Total Unique Channels: {len(unique_channels)}")
print("Channel IDs:", unique_channels)
