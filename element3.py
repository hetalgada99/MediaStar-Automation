import xml.etree.ElementTree as ET
import pandas as pd
import os
from collections import defaultdict

# === Paths ===
input_dir = r"C:\Users\hgada\OneDrive - Hearst\Documents\Discrepancies XML\Discrepancies Input"
output_dir = r"C:\Users\hgada\OneDrive - Hearst\Documents\Discrepancies XML\Discrepancies Output"
log_file = r"C:\Users\hgada\OneDrive - Hearst\Documents\Discrepancies XML\discrepancies_log.txt"

# === Ensure output directory exists ===
os.makedirs(output_dir, exist_ok=True)

def read_log():
    """Read already processed files from the log file."""
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return set(line.strip() for line in f.readlines())
    return set()

def write_log(filename):
    """Append successfully processed filename to the log."""
    with open(log_file, 'a') as f:
        f.write(f"{filename}\n")

def find_repeating_elements(root):
    """Identify repeating elements under any parent in the XML tree."""
    repeating_elements = defaultdict(list)
    for parent in root.iter():
        child_counts = defaultdict(int)
        for child in parent:
            child_counts[child.tag] += 1
        for tag, count in child_counts.items():
            if count > 1:
                repeating_elements[tag].extend(parent.findall(tag))
    return repeating_elements

def extract_records(elements):
    """Convert XML elements into dictionaries of their children."""
    rows = []
    for elem in elements:
        row = {}
        for child in elem:
            row[child.tag] = child.text.strip() if child.text else ''
        rows.append(row)
    return rows

# === Main processing loop ===
processed_files = read_log()

for filename in os.listdir(input_dir):
    if filename.endswith('.xml') and filename not in processed_files:
        file_path = os.path.join(input_dir, filename)
        output_excel = os.path.join(
            output_dir, os.path.splitext(filename)[0] + '.xlsx'
        )

        print(f"\nProcessing: {filename}")
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            root_tag = root.tag

            repeating_elements = find_repeating_elements(root)

            if not repeating_elements:
                print(f"  No repeating elements in {filename}. Skipping.")
                continue

            with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
                for tag, elements in repeating_elements.items():
                    records = extract_records(elements)
                    if records:
                        df = pd.DataFrame(records)
                        df[root_tag] = tag  # Add new column with root name
                        # Move root column to the end
                        cols = list(df.columns)
                        if cols[-1] != root_tag:
                            cols.append(cols.pop(cols.index(root_tag)))
                            df = df[cols]
                        df.to_excel(writer, sheet_name=tag[:31], index=False)
                    else:
                        print(f"  No data under tag: <{tag}>")

            write_log(filename)
            print(f"  Successfully processed and saved: {output_excel}")

        except ET.ParseError as e:
            print(f"  XML parse error in {filename}: {e}")
        except Exception as ex:
            print(f"  Error processing {filename}: {ex}")
