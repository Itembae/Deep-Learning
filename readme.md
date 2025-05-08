inaturalist.py pulls images from the inaturalist group created for this project

    for all users except crono_sequencia_4, the tag is the last (sixth image)
        for crono_sequencia_4 and 5, it is the first

        need to remove the corresponding image for all of them


        mismatches: 480219389.jpg isnt a tag
                    480235270.jpg



Order: 

    1. Run inaturalist.py to download the photos

    2. Run merged_csv.py to add species labeling to the photos from the csv tracking specimen ids
            a. check that every entry is populated, correct spelling errors (incorrect sapling label (PEQ0333 instead of PEA0333))

    3. Run dataset.py to organize the images into csv files usable for model training

    4. using dataset.csv from step 3, run set_creation.py and then folder_creation to generate a usable dataset
    
    
