import requests
r = requests.get("https://rtas.wdfiles.com/local--code_/gas%3Ataglisten/1")
print(r.text)
f = open('./scp-wiki/tags/tags.md', 'w', encoding="utf-8_sig")
f.write(r.text)
f.close()

