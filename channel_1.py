#channelId="2036768"


# import requests
# import xml.etree.ElementTree as ET

# url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

# print("Fetching the XML data from the URL...")
# response = requests.get(url, stream=True)
# response.raw.decode_content = True  # Ensure correct decoding
# print("XML data received. Starting parsing process...\n")

# # Define the TitanTV namespace
# ns = {"ttv": "http://www.titantv.com/"}

# # Target channel ID
# target_channel_id = "2036768"

# # Parse the XML efficiently
# context = ET.iterparse(response.raw, events=("start", "end"))

# # Track whether we are inside the correct <Channel>
# current_channel = None

# print(f"Looking for shows under channel ID: {target_channel_id}\n")

# # Iterate through the XML
# for event, elem in context:
#     if event == "start" and elem.tag.endswith("Channel"):  
#         current_channel = elem.attrib.get("channelId")

#     if event == "end" and elem.tag.endswith("Show") and current_channel == target_channel_id:
#         # Extract show details
#         start_time = elem.attrib.get("startTimeUtc", "N/A")
#         end_time = elem.attrib.get("endTimeUtc", "N/A")
#         duration = elem.attrib.get("duration", "N/A")
#         program_id = elem.attrib.get("programId", "N/A")
#         is_hd = elem.attrib.get("isHd", "false")
#         new_repeat = elem.attrib.get("newRepeat", "N/A")
#         year = elem.attrib.get("year", "N/A")
#         original_air_date = elem.attrib.get("originalAirDate", "N/A")

#         title_elem = elem.find("ttv:Title", ns)
#         title = title_elem.text if title_elem is not None else "N/A"

#         desc_elems = elem.findall("ttv:Description", ns)
#         descriptions = [desc.text for desc in desc_elems if desc.text]  # Handle multiple descriptions

#         genre_elem = elem.find("ttv:DisplayGenre", ns)
#         genre = genre_elem.text if genre_elem is not None else "N/A"

#         cast_elems = elem.findall("ttv:Cast", ns)
#         cast_members = [f"{cast_elem.attrib.get('role', 'N/A')}: {cast_elem.text}" for cast_elem in cast_elems]

#         category_elems = elem.findall("ttv:Category", ns)
#         categories = [f"{cat_elem.attrib.get('lang', 'N/A')}: {cat_elem.text}" for cat_elem in category_elems]

#         rating_elem = elem.find("ttv:Rating", ns)
#         rating = rating_elem.attrib.get("tv", "N/A") if rating_elem is not None else "N/A"

#         cc_elem = elem.find("ttv:ClosedCaption", ns)
#         closed_caption = "Yes" if cc_elem is not None and cc_elem.attrib.get("isDigital", "false") == "true" else "No"

#         print(f"📺 Title: {title}")
#         print(f"📖 Descriptions: {' | '.join(descriptions)}")
#         print(f"📅 Start Time: {start_time}")
#         print(f"⌛ Duration: {duration}")
#         print(f"🎭 Genre: {genre}")
#         print(f"📆 Year: {year}, Original Air Date: {original_air_date}")
#         print(f"🔍 HD: {is_hd}, New/Repeat: {new_repeat}")
#         print(f"🎭 Cast: {', '.join(cast_members)}")
#         print(f"📂 Categories: {', '.join(categories)}")
#         print(f"⭐ Rating: {rating}")
#         print(f"📝 Closed Captions Available: {closed_caption}")
#         print(f"🎬 Program ID: {program_id}")
#         print("-" * 80)

#         elem.clear()  # Free memory after processing each <Show> element

# del context  # Cleanup

# print("\nExtraction completed! ✅")


# import requests
# import xml.etree.ElementTree as ET

# url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"

# print("Fetching the XML data from the URL...")
# response = requests.get(url, stream=True)
# response.raw.decode_content = True  # Ensure correct decoding
# print("XML data received. Starting parsing process...\n")

# # Define the TitanTV namespace
# ns = {"ttv": "http://www.titantv.com/"}

# # Target channel ID
# target_channel_id = "2036768"

# # Parse the XML efficiently
# context = ET.iterparse(response.raw, events=("start", "end"))

# # Track whether we are inside the correct <Channel>
# current_channel = None

# print(f"Looking for shows under channel ID: {target_channel_id}\n")

# for event, elem in context:
#     tag_name = elem.tag.split("}")[-1]  # Extract tag name without namespace

#     if event == "start" and tag_name == "Channel":
#         current_channel = elem.attrib.get("channelId")
    
#     elif event == "end" and tag_name == "Channel":
#         current_channel = None  # Reset when exiting a Channel

#     elif event == "end" and tag_name == "Show" and current_channel == target_channel_id:
#         # Extract show details
#         start_time = elem.attrib.get("startTimeUtc", "N/A")
#         end_time = elem.attrib.get("endTimeUtc", "N/A")
#         duration = elem.attrib.get("duration", "N/A")
#         program_id = elem.attrib.get("programId", "N/A")
#         is_hd = elem.attrib.get("isHd", "false")
#         new_repeat = elem.attrib.get("newRepeat", "N/A")
#         year = elem.attrib.get("year", "N/A")
#         original_air_date = elem.attrib.get("originalAirDate", "N/A")

#         title_elem = elem.find("ttv:Title", ns)
#         title = title_elem.text if title_elem is not None else "N/A"

#         episode_title_elem = elem.find("ttv:EpisodeTitle", ns)
#         episode_title = episode_title_elem.text if episode_title_elem is not None else "N/A"

#         desc_elems = elem.findall("ttv:Description", ns)
#         descriptions = [desc.text for desc in desc_elems if desc.text]  # Handle multiple descriptions

#         genre_elem = elem.find("ttv:DisplayGenre", ns)
#         genre = genre_elem.text if genre_elem is not None else "N/A"

#         cast_elems = elem.findall("ttv:Cast", ns)
#         cast_members = [f"{cast_elem.attrib.get('role', 'N/A')}: {cast_elem.text}" for cast_elem in cast_elems]

#         category_elems = elem.findall("ttv:Category", ns)
#         categories = [f"{cat_elem.attrib.get('lang', 'N/A')}: {cat_elem.text}" for cat_elem in category_elems]

#         rating_elem = elem.find("ttv:Rating", ns)
#         rating = rating_elem.attrib.get("tv", "N/A") if rating_elem is not None else "N/A"

#         cc_elem = elem.find("ttv:ClosedCaption", ns)
#         closed_caption = "Yes" if cc_elem is not None and cc_elem.attrib.get("isDigital", "false") == "true" else "No"

#         network_elem = elem.find("ttv:Network", ns)
#         network = network_elem.text if network_elem is not None else "N/A"

#         series_id_elem = elem.find("ttv:SeriesId", ns)
#         series_id = series_id_elem.text if series_id_elem is not None else "N/A"

#         season_elem = elem.find("ttv:SeasonNumber", ns)
#         season = season_elem.text if season_elem is not None else "N/A"

#         episode_elem = elem.find("ttv:EpisodeNumber", ns)
#         episode = episode_elem.text if episode_elem is not None else "N/A"

#         print(f"📺 Title: {title}")
#         print(f"🎭 Episode Title: {episode_title}")
#         print(f"📖 Descriptions: {' | '.join(descriptions)}")
#         print(f"📅 Start Time: {start_time}")
#         print(f"⌛ Duration: {duration}")
#         print(f"🎭 Genre: {genre}")
#         print(f"📆 Year: {year}, Original Air Date: {original_air_date}")
#         print(f"🔍 HD: {is_hd}, New/Repeat: {new_repeat}")
#         print(f"🎭 Cast: {', '.join(cast_members)}")
#         print(f"📂 Categories: {', '.join(categories)}")
#         print(f"⭐ Rating: {rating}")
#         print(f"📝 Closed Captions Available: {closed_caption}")
#         print(f"📡 Network: {network}")
#         print(f"📀 Series ID: {series_id}")
#         print(f"📅 Season: {season}, Episode: {episode}")
#         print(f"🎬 Program ID: {program_id}")
#         print("-" * 80)

#         elem.clear()  # Free memory after processing each <Show> element

# del context  # Cleanup

# print("\nExtraction completed! ✅")


##in excel : ABC!

import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Define the file path
file_path = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\media_star_shows1.xlsx"

# Fetch XML data
url = "https://data.titantvguide.com/api/schedule/1e6db3bcf5e743f883a4814f5d960fba"
print("Fetching the XML data from the URL...")
response = requests.get(url, stream=True)
response.raw.decode_content = True
print("XML data received. Starting parsing process...\n")

# Define the TitanTV namespace
ns = {"ttv": "http://www.titantv.com/"}
target_channel_id = "2036768"  # Example channel ID to filter

# Parse the XML efficiently
context = ET.iterparse(response.raw, events=("start", "end"))

# Track whether we are inside the correct <Channel>
current_channel = None

# Prepare a list to store the extracted data
show_data = []

for event, elem in context:
    tag_name = elem.tag.split("}")[-1]  # Extract tag name without namespace

    if event == "start" and tag_name == "Channel":
        current_channel = elem.attrib.get("channelId")

    elif event == "end" and tag_name == "Channel":
        current_channel = None  # Reset when exiting a Channel

    elif event == "end" and tag_name == "Show" and current_channel == target_channel_id:
        # Extract show details
        show_info = {
            "Event ID": elem.attrib.get("eventId", "N/A"),
            "Title": elem.find("ttv:Title", ns).text if elem.find("ttv:Title", ns) is not None else "N/A",
            "Episode Title": elem.find("ttv:EpisodeTitle", ns).text if elem.find("ttv:EpisodeTitle", ns) is not None else "N/A",
            "Start Time": elem.attrib.get("startTimeUtc", "N/A"),
            "Duration": elem.attrib.get("duration", "N/A"),
            "Genre": elem.find("ttv:DisplayGenre", ns).text if elem.find("ttv:DisplayGenre", ns) is not None else "N/A",
            "Year": elem.attrib.get("year", "N/A"),
            "Original Air Date": elem.attrib.get("originalAirDate", "N/A"),
            "HD": elem.attrib.get("isHd", "false"),
            "New/Repeat": elem.attrib.get("newRepeat", "N/A"),
            "Rating": elem.find("ttv:Rating", ns).attrib.get("tv", "N/A") if elem.find("ttv:Rating", ns) is not None else "N/A",
            "Closed Caption": "Yes" if elem.find("ttv:ClosedCaption", ns) is not None and elem.find("ttv:ClosedCaption", ns).attrib.get("isDigital", "false") == "true" else "No",
            "Network": elem.find("ttv:Network", ns).text if elem.find("ttv:Network", ns) is not None else "N/A",
            "Cast": ", ".join([f"{cast_elem.attrib.get('role', 'N/A')}: {cast_elem.text}" for cast_elem in elem.findall("ttv:Cast", ns)]),
            "Categories": ", ".join([f"{cat_elem.attrib.get('lang', 'N/A')}: {cat_elem.text}" for cat_elem in elem.findall("ttv:Category", ns)]),
            "Program ID": elem.attrib.get("programId", "N/A"),
        }

        show_data.append(show_info)
        elem.clear()  # Free memory after processing each <Show> element

del context  # Cleanup

# Save data to Excel using pandas
df = pd.DataFrame(show_data)
df.to_excel(file_path, index=False, engine='openpyxl')

print(f"\nExtraction completed! ✅ Data saved to {file_path}")
