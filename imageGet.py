#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anthony.Lim
#
# Created:     17/09/2013
# Copyright:   (c) Anthony.Lim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib,re,ntpath,os

base_path = "c:/localdrive/"
image_extensions = ['jpg','png']

def main():
    download_from_url('http://thoughtcatalog.com/2013/22-things-you-need-to-do-while-you-have-the-chance/')

def download_from_url(url):
    htmllines = get_request(url)
    for line in htmllines:
        imgs = get_img(line)
        if len(imgs)>0:
            #print ''.join(imgs)
            for img in imgs:
                url = ''.join( get_src(img) )
                if url:
                    base_name = ntpath.basename(url)
                    local_path = os.path.join(base_path,base_name)
                    urllib.urlretrieve(url,local_path)

def get_request(url):
    return urllib.urlopen(url).readlines()

def get_img(line):
    pattern = re.compile('<img[^>]+>',re.IGNORECASE)
    return pattern.findall(line)

def get_src(img):
    results = []
    for val in self.image_extensions:
        pattern = re.compile('http.+\.'+val,re.IGNORECASE)
        results += pattern.findall(img)
    ##pattern = re.compile('http\:\/\/4\.bp\.blogspot\.com\/\-XhZnSeF81Lc/UGEna2b7HaI\/AAAAAAAAA6Y\/WBodpDoVUmc\/s72\-c\/1\.jpg',re.IGNORECASE)
    return results

if __name__ == '__main__':
    main()
