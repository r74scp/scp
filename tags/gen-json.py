# coding: UTF-8
import re
import json

f = open("./tags/tags_commented.md", "r", encoding="utf-8_sig")
data = f.read()
f.close()

d = []

pattern_tab = '\[\[tab (.*?)\]\]([\s\S]*?)\[\[\/tab\]\]'
pattern_heading3 = '\+{3}.*?(?=\+{3}|$)'
pattern_get_heading3 = '\+{3}\s(.*?)\n'
pattern_tag = '(\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*)( \/\/\((.*?)\)\/\/|)(.*?) - (.*?)\n'
pattern_tag_nest = '(\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*( \/\/\((.*?)\)\/\/|))'


results_tab = re.findall(pattern_tab, data, re.S)
i=0
for result_tab in results_tab:
  # print(str(result_tab[0]))
  results_heading3 = re.findall(pattern_heading3, str(result_tab[1]), re.S)
  if results_heading3 !=[]:
    for result_heading3 in results_heading3:
      result_get_heading3 = re.findall(pattern_get_heading3, str(result_heading3), re.S)
      # if result_get_heading3 != []:
      #   print(str(result_get_heading3[0]))
      results_tag = re.findall(pattern_tag, str(result_heading3), re.S)
      for result_tag in results_tag:
        if(result_tag[4] !=""):
          results_tagnest = re.findall(pattern_tag_nest, result_tag[4], re.S)
          for result_tagnest in results_tagnest:
            # print(result_tagnest[1], result_tagnest[3], result_tag[5], result_get_heading3[0], result_tab[0], i)
            d.append({"id":i, "tag":result_tagnest[1], "trans":result_tagnest[3], "desc":result_tag[5], "type":result_get_heading3[0], "category":result_tab[0]})
            i=i+1
        else:
          # print(result_tag[1], result_tag[3], result_tag[5], result_get_heading3[0], result_tab[0], i)
          d.append({"id":i, "tag":result_tag[1], "trans":result_tag[3], "desc":result_tag[5], "type":result_get_heading3[0], "category":result_tab[0]})
          i=i+1
  else:
    results_tag = re.findall(pattern_tag, result_tab[1], re.S)
    for result_tag in results_tag:
      if(result_tag[4] !=""):
        results_tagnest = re.findall(pattern_tag_nest, result_tag[4], re.S)
        for result_tagnest in results_tagnest:
          # print(result_tagnest[1], result_tagnest[3], result_tag[5], "", result_tab[0], i)
          d.append({"id":i, "tag":result_tagnest[1], "trans":result_tagnest[3], "desc":result_tag[5], "category":result_tab[0]})
          i=i+1
      else:
        # print(result_tag[1], result_tag[3], result_tag[5], "", result_tab[0], i)
        d.append({"id":i, "tag":result_tag[1], "trans":result_tag[3], "desc":result_tag[5], "category":result_tab[0]})
        i=i+1
# print(d)
with open("./tags/tags.json", "w", encoding="utf-8_sig") as f:
  json.dump(d, f, indent=4, ensure_ascii=False)
