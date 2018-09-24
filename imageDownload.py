import os
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# working directory
path="C:\Workspace\Python\Webtools"

for x in range(1,2):
    page = x
    print("Downloading page %i" %page)
    #directory= path + "/%i" %page
    #if not os.path.exists(directory):
    #    os.makedirs(directory)
    #os.chdir(directory)
    # all the other pages (2 through 34)
    #url= 'https://teamcovenant.com/product-category/star-wars-destiny-card-game-ffg/buy-destiny-singles/page/'
    #html = urlopen(url+"%i" % page)
    # page 1
    url= 'https://teamcovenant.com/product-category/star-wars-destiny-card-game-ffg/buy-destiny-singles/'
    html = urlopen(url)


    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.png')})
    for image in images:
        imageString=image['src']
        print("Image String: {}".format(imageString))
        imageURL=imageString[:-12]+".png"
        print("Image URL: {}".format(imageURL))
        imageName=imageURL.split('/')[-1]
        print("Image Filename: {}".format(imageName))
        #Download image
        if imageName == "covenant-log.png":
            print("Skipping file {}".format(imageName)+'\n')
        elif imageName == "i.png":
            print("Skipping file {}".format(imageName)+'\n')
        elif imageName == "coven.png":
            print("Skipping file {}".format(imageName)+'\n')
        else:
            try:
                urllib.request.urlretrieve("https:" + imageURL, imageName)
                print("Successfully download {}".format(imageName)+'\n')
            except:
                print('failed %s'%imageURL+'\n')