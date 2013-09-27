#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anthony.Lim
#
# Created:     13/09/2013
# Copyright:   (c) Anthony.Lim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib,re

def main():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    num = "12345"
    _continue = True
    tries = 0
    while _continue:
        e = url+"?nothing="+num
        print(e)
        try:
            num = get(e)
        except NoMatchException:
            print 'No Match!'
            if tries >= 1:
                _continue = False
            else:
                tries += 1
                num = ""

def get(url):
    result = urllib.urlopen(url)
    line = ''.join( result.readlines() )
    nothing_pattern = re.compile('\d{1,5}')
    match = nothing_pattern.findall(line)
    print line
    if match:
        return ''.join( match )
    else:
        raise NoMatchException()

if __name__ == '__main__':
    main()

class NoMatchException(Exception):
    pass