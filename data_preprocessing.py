import pandas as pd
import os
import glob
import json

# 1. Define paths for CSV and JSON files
data_path = 'archive'  # Replace with the path to your data folder
csv_files = glob.glob(os.path.join(data_path, "*videos.csv"))
json_files = glob.glob(os.path.join(data_path, "*_category_id.json"))

# 2. Read and merge CSV data
dataframes = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file, encoding='latin1')  # 使用 latin1 编码
    country_code = os.path.basename(csv_file)[:2].upper()  # Extract country code from filename
    df['country'] = country_code  # Add country column
    dataframes.append(df)

# Concatenate all DataFrames
full_data = pd.concat(dataframes, ignore_index=True)
full_data['category_id'] = full_data['category_id'].astype(str)

# 3. Function to load category titles from JSON
def load_category_titles(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    titles = {item['id']: item['snippet']['title'] for item in data['items']}
    return titles

# 4. Merge category titles into DataFrame
for json_file in json_files:
    country_code = os.path.basename(json_file[:json_file.index('_category_id')]).upper()
    category_titles = load_category_titles(json_file)

    # Add category_title column
    full_data.loc[full_data['country'] == country_code, 'category_title'] = \
        full_data.loc[full_data['country'] == country_code, 'category_id'].map(category_titles)

duplicate_rows = full_data[full_data.duplicated()]
print("Duplicates：", duplicate_rows)
full_data_cleaned = full_data.drop_duplicates()
full_data_cleaned.drop(columns=['thumbnail_link', 'description'], inplace=True)

country_counts = full_data_cleaned['country'].value_counts()
print("Count in diff countries：", country_counts)
print(country_counts)
print(full_data_cleaned.info())

# 5. Output the merged dataset into csv/tsv
full_data_cleaned.to_csv('merged_data.csv', index=False)
full_data_cleaned.to_csv('merged_data.tsv', sep='\t', index=False)
full_data.to_csv('raw.tsv', sep='\t', index=False)
print("Output finished!")