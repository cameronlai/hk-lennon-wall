import json
import pandas as pd

input_filename = 'data.json'
output_filename = '../src/data/Data.json'

with open(input_filename, 'rb') as f:
    data = json.load(f)

df = pd.read_json(json.dumps(data['GraphImages']))
print(df.shape)

df = df.dropna(subset=['location'])
print(df.shape)

output_ary = []
for index, row in df.iterrows():
    output_ary.append({
        'shortcode': row['shortcode'],
        'location':  row['location']['name']
    })
    if index == 3:
        break

final_df = pd.DataFrame(output_ary)
final_df.to_json(output_filename, orient='records')
print(final_df.head())