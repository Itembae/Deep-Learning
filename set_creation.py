import os
import shutil
from sklearn.model_selection import train_test_split
from collections import defaultdict
from tqdm import tqdm

# Set your paths
source_dir = "grouped_images"  # e.g., "data/plant_images"
output_dir = "split_data"        # e.g., "data/split"
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6, "Splits must sum to 1.0"

# Step 1: Gather filepaths and labels
filepaths = []
labels = []

for label in os.listdir(source_dir):
    class_dir = os.path.join(source_dir, label)
    if not os.path.isdir(class_dir):
        continue
    for filename in os.listdir(class_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            filepaths.append(os.path.join(class_dir, filename))
            labels.append(label)

# Step 2: Stratified split
X_train, X_temp, y_train, y_temp = train_test_split(
    filepaths, labels, stratify=labels, test_size=(1 - train_ratio), random_state=42
)

val_relative = val_ratio / (val_ratio + test_ratio)  # e.g., 0.15 / (0.15 + 0.15) = 0.5
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, stratify=y_temp, test_size=(1 - val_relative), random_state=42
)

splits = {
    "train": (X_train, y_train),
    "val": (X_val, y_val),
    "test": (X_test, y_test),
}

# Step 3: Copy files into new structure
for split_name, (split_paths, split_labels) in splits.items():
    print(f"Copying {split_name} data...")
    for src, label in tqdm(zip(split_paths, split_labels), total=len(split_paths)):
        dst_dir = os.path.join(output_dir, split_name, label)
        os.makedirs(dst_dir, exist_ok=True)
        shutil.copy2(src, os.path.join(dst_dir, os.path.basename(src)))
