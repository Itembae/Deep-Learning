import requests
import os
import csv


# downloads inaturalist images


# List of selected user IDs with usernames
user_ids = {
    9000660: "crono_secuencia_2",
    9000828: "crono_secuencia_3",
    9010243: "crono_secuencia5",
    #run 4 separately as they are inconsistent
    # 9010247: "crono_secuencia_4"  # This user will omit the first image instead
}

# Directory to save photos
save_dir = os.path.expanduser('inaturalist_photos_filtered')
os.makedirs(save_dir, exist_ok=True)

# CSV file to save notes and photo details
csv_file = os.path.join(save_dir, 'notes_and_photos.csv')

def save_notes_and_photos_to_csv(data):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, 'a', newline='') as csvfile:
        fieldnames = ['user_id', 'username', 'observation_id', 'photo_id', 'photo_url', 'photo_path', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for entry in data:
            writer.writerow(entry)

def download_photos_and_notes(user_id, username):
    page = 1
    data = []

    while True:
        url = f'https://api.inaturalist.org/v1/observations?user_id={user_id}&per_page=100&page={page}'
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f'Failed to fetch observations for {username} ({user_id}) on page {page}')
            break

        observations = response.json().get('results', [])
        if not observations:
            break  # No more data

        for obs in observations:
            observation_id = obs['id']
            note = obs.get('description', '')
            photos = obs.get('photos', [])
            
            # Optionally omit first or last photo
            # Uncomment and customize this block if needed
            if username == "crono_secuencia_4" or username == "crono_secuencia5":
                photos = photos[1:]
            else:
                photos = photos[:-1]

            for photo in photos:
                photo_url = photo.get('url', '').replace('square', 'original')
                photo_id = photo.get('id')

                if photo_url:
                    photo_response = requests.get(photo_url)
                    if photo_response.status_code == 200:
                        photo_path = os.path.join(save_dir, f'{user_id}_{observation_id}_{photo_id}.jpg')
                        with open(photo_path, 'wb') as f:
                            f.write(photo_response.content)
                        print(f'Downloaded photo {photo_id} for {username} ({user_id})')
                        data.append({
                            'user_id': user_id,
                            'username': username,
                            'observation_id': observation_id,
                            'photo_id': photo_id,
                            'photo_url': photo_url,
                            'photo_path': photo_path,
                            'description': note
                        })
                    else:
                        print(f'Failed to download photo {photo_id} for {username} ({user_id})')

        page += 1  # Move to the next page
    save_notes_and_photos_to_csv(data)

# Loop through selected users
for user_id, username in user_ids.items():
    download_photos_and_notes(user_id, username)
