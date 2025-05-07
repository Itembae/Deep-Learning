import os
import shutil
import pandas as pd

# Load your dataset
csv_path = "dataset.csv"
df = pd.read_csv(csv_path)

# Define the target directory where folders will be created
output_dir = "grouped_images"
os.makedirs(output_dir, exist_ok=True)

# Iterate through each row
for _, row in df.iterrows():
    image_path = os.path.join(row['image_path'])
    species_name = row['label']
    
    # Create the species folder if it doesn't exist
    species_folder = os.path.join(output_dir, species_name)
    os.makedirs(species_folder, exist_ok=True)
    
    # Define destination path
    dest_path = os.path.join(species_folder, os.path.basename(image_path))
    
    # Copy the image (use shutil.move if you prefer to move instead of copy)
    if os.path.exists(image_path):
        shutil.copy(image_path, dest_path)
    else:
        print(f"Image not found: {image_path}")
