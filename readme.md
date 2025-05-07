inaturalist.py pulls images from the inaturalist group created for this project

    want to make sure to only use ids from crono_sequncia users

    for all users except crono_sequencia_4, the tag is the last (sixth image)
        for crono_sequencia_4 and 5, it is the first

        need to remove the corresponding image for all of them


        mismatches: 480219389.jpg isnt a tag
                    480235270.jpg



Order: 

    1. Run inaturalist.py to download photos

    2. Run mergede_csv.py to add species labeling to the photos
            a. check that every entry is populated, correct spelling errors (incorrect sapling label (PEQ0333 instead of PEA0333))

    3. Run dataset.py to organize the images into csv files usable for model training
    