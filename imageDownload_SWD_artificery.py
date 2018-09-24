import os
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#url= 'https://artificery.com/product-category/sw-destiny/singles/'
#html = urlopen(url)
path="C:\Workspace\Python\Webtools"
i = 0
for x in range(2,36):
    page = x
    directory= path + "/%i" % page
#    if not os.path.exists(directory):
#        os.makedirs(directory)
#    os.chdir(directory)
    url= 'https://artificery.com/product-category/sw-destiny/singles/page/'
    html = urlopen(url+"%i" % page)
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.png')})
    for image in images:
        imageString=image['src']
        #print("Image String: {}".format(imageString))
        imageURL=imageString[:-12]+".png"
        #print("Image URL: {}".format(imageURL))
        imageName=imageURL.split('/')[-1]
        #print("Image Filename: {}".format(imageName))
        if imageName == "Ar.png":
            #print("Skipping file {}".format(imageName)+'\n')
            i = i + 1
        elif imageName == "Across-the-Galaxy-Booster-Box.png":
            #print("Skipping file {}".format(imageName)+'\n')
            i = i + 1
        elif imageName == "transformers-tcg-booster-display.png":
            #print("Skipping file {}".format(imageName)+'\n')
            i = i + 1
        elif imageName == "Destiny-Subscription.png":
            #print("Skipping file {}".format(imageName)+'\n')
            i = i + 1
        elif imageName == "transformers-tcg-subscription.png":
            #print("Skipping file {}".format(imageName)+'\n')
            i = i + 1
        else:
            print(imageName)
#            try:
#                # Download image
#                #urllib.request.urlretrieve("https:" + imageURL, imageName)
#                urllib.request.urlretrieve(imageURL, imageName)
#                print("Successfully download {}".format(imageName)+'\n')
#            except:
#                print('failed %s'%imageURL+'\n')