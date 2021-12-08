import requests
r = requests.get("https://rtas.wdfiles.com/local--code_/gas%3Ataglistjp/1")
print(r.text)
f = open('./tags/tags.md', 'w')
f.write(r.text)
f.close()
