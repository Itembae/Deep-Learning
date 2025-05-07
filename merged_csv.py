
import pandas as pd


#adds species information to tagged plant photos



notes_photos_path = 'tagged_photos.csv'
yps_seedlings_path = 'data_YPS_seedlings_2025_03_18.csv'

notes_df = pd.read_csv(notes_photos_path)
seedlings_df = pd.read_csv(yps_seedlings_path)

# Ensure correct column names
id_yps_col = "ID_YPS"
description_col = "description"


notes_df[description_col] = notes_df[description_col].str.upper()
seedlings_df[id_yps_col] = seedlings_df[id_yps_col].str.upper() 

# Select relevant columns from seedlings data
seedlings_df = seedlings_df[[id_yps_col, "Genus", "Family", "Species"]]

# Merge based on description matching id_yps
notes_df = notes_df.merge(seedlings_df, left_on=description_col, right_on=id_yps_col, how="left")

# Drop the redundant id_yps column from the merge
notes_df.drop(columns=[id_yps_col], inplace=True)

# Save the updated file
output_path = "/Users/itembematiku/Desktop/Senior Project/Model/photo_labels.csv"
notes_df.to_csv(output_path, index=False)

print(f"Updated file saved as: {output_path}")
