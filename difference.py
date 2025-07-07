# import pandas as pd

# # Paths to the two Excel files
# file_path_1 = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\media_star_shows.xlsx"
# file_path_2 = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\media_star_shows1.xlsx"

# # Load the Excel files into pandas DataFrames
# df1 = pd.read_excel(file_path_1, engine='openpyxl')
# df2 = pd.read_excel(file_path_2, engine='openpyxl')

# # Merge the two DataFrames based on Program ID to find any differences
# merged_df = pd.merge(df1, df2, on='Program ID', how='outer', suffixes=('_old', '_new'))

# # Identify rows where there are differences
# differences = merged_df[merged_df.filter(like='_old').ne(merged_df.filter(like='_new')).any(axis=1)]

# # Display the differences
# if not differences.empty:
#     print("Differences found based on Program ID:")
#     print(differences)
# else:
#     print("No differences found between the two files.")

# # Optionally, save the differences to a new Excel file for review
# differences_file_path = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\differences.xlsx"
# differences.to_excel(differences_file_path, index=False, engine='openpyxl')
# print(f"Differences saved to: {differences_file_path}")


import pandas as pd

# Paths to the two Excel files
file_path_1 = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\media_star_shows.xlsx"
file_path_2 = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\media_star_shows1.xlsx"

# Load the Excel files into pandas DataFrames
df1 = pd.read_excel(file_path_1, engine='openpyxl')
df2 = pd.read_excel(file_path_2, engine='openpyxl')

# Merge the two DataFrames based on Program ID to find any differences
merged_df = pd.merge(df1, df2, on='Program ID', how='outer', suffixes=('_old', '_new'))

# Create an empty list to store the differences
difference_list = []

# Iterate over each row in the merged DataFrame
for index, row in merged_df.iterrows():
    program_id = row['Program ID']
    
    # Check each column for differences
    for column in df1.columns:
        old_value = row[f'{column}_old']
        new_value = row[f'{column}_new']
        
        if old_value != new_value:
            # Add the difference details to the list
            difference_list.append({
                'Program ID': program_id,
                'Column': column,
                'Old Value': old_value,
                'New Value': new_value
            })

# Create a DataFrame from the difference list
differences_df = pd.DataFrame(difference_list)

# Display the differences
if not differences_df.empty:
    print("Differences found based on Program ID:")
    print(differences_df)
else:
    print("No differences found between the two files.")

# Optionally, save the differences to a new Excel file for review
differences_file_path = r"C:\Users\hgada\OneDrive - Hearst\Documents\Media_Star_XML\differences.xlsx"
differences_df.to_excel(differences_file_path, index=False, engine='openpyxl')
print(f"Differences saved to: {differences_file_path}")
