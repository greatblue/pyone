import urllib.request
import json


class FunWithOs(object):
    """zezanje sa operativnim sistemom"""

    def __init__(self, text):
        self.text = text

    def writefile(self):
        print('creating new file ')
        file = open('test.txt', 'a')
        file.write(str(self.text))
        file.close()


urlData = ""
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
print(data)
encoding = webURL.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))

writeToFile = FunWithOs(JSON_object)
writeToFile.writefile()
"""from windows"""
