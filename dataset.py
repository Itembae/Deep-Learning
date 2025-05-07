import os
import pandas as pd
from sklearn.model_selection import train_test_split

#structures the dataset into train, val, and test sets


# Load the dataset
file_path = "labeled_photos.csv"  # Update if needed
df = pd.read_csv(file_path)

# Define image directory (assuming images are stored locally)
image_dir = "inaturalist"
os.makedirs(image_dir, exist_ok=True)

image_paths, labels = [], []

for _, row in df.iterrows():
    for item in row:
        if isinstance(item, float):
            print(row["description"])
            print(item)
    species = row["Species"].replace(" ", "_")  # Format species name
    image_path = row["photo_path"]  # Use existing local image path
    
    if os.path.exists(image_path):
        labels.append(species)
        image_paths.append(image_path)
    else:
        
        print(f"Missing image: {image_path}")

# Create DataFrame and split
print(f"Length of image_paths: {len(image_paths)}")
print(f"Length of labels: {len(labels)}")
if len(image_paths) != len(labels):
    print("Mismatch between image paths and labels!")
data = pd.DataFrame({"image_path": image_paths, "label": labels})


label_counts = data["label"].value_counts()
valid_labels = label_counts[label_counts > 1].index
data = data[data["label"].isin(valid_labels)]



train, temp = train_test_split(data, test_size=0.2, stratify=data["label"], random_state=42)

label_counts = temp["label"].value_counts()  # Count occurrences of each label
valid_labels = label_counts[label_counts > 1].index  # Keep only labels with more than 1 sample
temp = temp[temp["label"].isin(valid_labels)]  # Filter temp dataset to include only valid labels

val, test = train_test_split(temp, test_size=0.5, stratify=temp["label"], random_state=42)

# Save CSV files
data.to_csv("dataset.csv", index=False)
train.to_csv("train.csv", index=False)
val.to_csv("val.csv", index=False)
test.to_csv("test.csv", index=False)

print("Dataset structured successfully!")
