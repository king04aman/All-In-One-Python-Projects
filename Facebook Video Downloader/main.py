import os, re, requests, wget

root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, "Downloads")
if not os.path.exists(path):
    os.mkdir(path)

link = input("Enter video link: ")
try:
    r = requests.get(link)
    if r.status_code == requests.codes.ok:
        try:
            sd_url = re.search('sd_src:"(.+?)"', r.text)[1]
            url = (
                re.search('hd_src:"(.+?)"', r.text)[1] if "hd_src" in r.text else sd_url
            )
            print("Downloading... Please wait...")
            wget.download(url, path)
        except Exception as e:
            print(e)
    else:
        print("Invalid Link!")

except Exception as e:
    print(e)
