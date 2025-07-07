# import requests
# import xml.etree.ElementTree as ET

# url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

# # Stream the XML response
# response = requests.get(url, stream=True)
# response.raw.decode_content = True  # Ensure correct decoding

# # Parse only the first few levels to get an idea of the structure
# try:
#     tree = ET.parse(response.raw)  # Parse the XML
#     root = tree.getroot()  # Get the root element

#     print(f"Root element: {root.tag}")  # Print root element

#     # Print first-level child elements
#     print("\nFirst-level child elements:")
#     for child in root:
#         print(f"- {child.tag}")

#     # Print second-level child elements (if present)
#     print("\nSecond-level child elements:")
#     for child in root:
#         for sub_child in child:
#             print(f"  - {sub_child.tag}")

# except ET.ParseError as e:
#     print(f"Error parsing XML: {e}")


import requests
import xml.etree.ElementTree as ET

url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

# Stream the XML response
response = requests.get(url, stream=True)
response.raw.decode_content = True  # Ensure correct decoding

# Function to extract unique element tags
def get_unique_tags(element, tags=set()):
    tags.add(element.tag)  # Add current element tag
    for child in element:
        get_unique_tags(child, tags)  # Recursively process children
    return tags

# Parse the XML response
try:
    tree = ET.parse(response.raw)  # Parse the XML
    root = tree.getroot()  # Get the root element

    # Get distinct element names
    unique_tags = get_unique_tags(root)

    print("\nDistinct XML elements found:")
    for tag in sorted(unique_tags):
        print(f"- {tag}")

except ET.ParseError as e:
    print(f"Error parsing XML: {e}")
