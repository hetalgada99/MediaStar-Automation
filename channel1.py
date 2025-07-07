import requests
import xml.etree.ElementTree as ET

url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

print("Fetching the XML data from the URL...")
response = requests.get(url, stream=True)
response.raw.decode_content = True  # Ensure correct decoding
print("XML data received. Starting parsing process...\n")

# Define the TitanTV namespace
ns = {"ttv": "http://www.titantv.com/"}

# Use a set to store unique channel IDs
unique_channels = set()

# Parse the XML efficiently
context = ET.iterparse(response.raw, events=("start", "end"))

# Iterate through the XML
print("Scanning for <Channel> elements to extract unique channel IDs...\n")
for event, elem in context:
    if event == "end" and elem.tag.endswith("Channel"):  # Looking for <Channel> elements
        channel_id = elem.attrib.get("channelId")
        
        if channel_id:
            if channel_id not in unique_channels:
                print(f"New Channel Found: {channel_id}")  # Print each unique channel ID found
            unique_channels.add(channel_id)
        
        elem.clear()  # Free memory after processing each <Channel> element

del context  # Cleanup

# Print results
print("\n--------------------------------------------")
print(f"Total Unique Channels Found: {len(unique_channels)}")
print("List of Unique Channel IDs:")
print(unique_channels)
print("--------------------------------------------")
