#!/usr/bin/env python
# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()



search_queries = ['achaemid architecture', 'american craftsman architecture',  'American Foursquare architecture', 'Ancient Egyptian architecture', 'austin architecture', 'oslo architecture', 'berlin architecture', 'tokyo architecture', 'sydney architecture', 'oslo architecture at night', 'tokyo architecture at night', 'berlin architecture at night','boston architecture', 'tennessee architecture', 'Art Deco architecture', 'Art Nouveau architecture', 'Baroque architecture', 'Bauhaus architecture', 'Beaux-Arts architecture',
   'Byzantine architecture' ,'Chicago school architecture', 'Colonial architecture', 'Deconstructivism', 'Edwardian architecture', 'Georgian architecture', 'Gothic architecture', 'Gothic architecture at night', 'Greek Revival architecture', 'International style', 'Novelty architecture', 'Palladian architecture', 'Postmodern architecture', 'Queen Anne architecture(Victorian)', 'Romanesque architecture','Russian Revival architecture', 'Tudor Revival architecture', 'new york architecture', 'miami architecture' 'chichago architecture', 'chichago architecture at night',
                  'Frank Lloyd Wright architecture', 'san fransisco architecture', 'la architecture']


def downloadimages(query):
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit":100,
                 "print_urls":True,
                 "size": "medium"}
    try:
        response.download(arguments)


    # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit":100,
                     "print_urls":True,
                     "size": "medium"}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass

# Driver Code
# Driver Code
for query in search_queries:
    downloadimages(query)
    print()



