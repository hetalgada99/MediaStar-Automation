import requests
import xml.etree.ElementTree as ET
from collections import defaultdict

# URL of the XML API
url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

# Dictionary to store parent → set of child tags
parent_child_map = defaultdict(set)

def map_parent_children(parent):
    for child in parent:
        parent_child_map[parent.tag].add(child.tag)
        map_parent_children(child)  # Recursive traversal

try:
    # Get the XML content
    response = requests.get(url)
    response.raise_for_status()

    # Parse the XML
    root = ET.fromstring(response.content)

    # Build parent-child relationships
    map_parent_children(root)

    # Display relationships
    print("Parent → Child Tag Relationships:\n")
    for parent, children in parent_child_map.items():
        print(f"{parent} → {', '.join(sorted(children))}")

except requests.RequestException as e:
    print(f"Request error: {e}")
except ET.ParseError as e:
    print(f"XML parsing error: {e}")


