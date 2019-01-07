import os
import urllib.request
import requests

print("downloading with urllib")

url = "https://e4ftl01.cr.usgs.gov/PullDir/030457394991697/ASTGTM2_N04E019.zip"

cookie = 'DATA=W9apAzdvLyZ9gPjKYjzl@wAAANU'

header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Connection':
    'keep-alive',
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cookie': cookie
}
file = url[-19:]
LocalPath = os.path.join('C:/code/files', file)
print('downloading {0}'.format(file))
urllib.request.urlretrieve(url, LocalPath)
