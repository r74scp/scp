# coding: UTF-8
import re
import json

pattern_tab = '\[\[tab (.*?)\]\]([\s\S]*?)\[\[\/tab\]\]'
pattern_heading3 = '\+{3}.*?(?=\+{3}|$)'
pattern_get_heading3 = '\+{3}\s(.*?)\n'
pattern_tag = '(\*\*\[https?://scp-wiki\.wikidot\.com/system:page-tags/tag/(.*?) .*?\]\*\*) \-\- (.*?)$'
pattern_tag_nest = '(\*\*\[https?://scp-wiki\.wikidot\.com/system:page-tags/tag/(.*?) .*?\]\*\*( \/\/\((.*?)\)\/\/|))'

pattern_ultag = '\* \*\*.*?(?=\* \*\*|$)'
pattern_ultag_list = '( \* (.*?)$)'
pattern_ultag_list_li = '( \* (.*?))\\n'

def parse(i, d, data):
  results_tab = re.findall(pattern_tab, data, re.S)
  for result_tab in results_tab:
    # print((result_tab[0]))
    results_heading3 = re.findall(pattern_heading3, str(result_tab[1]), re.S)
    if results_heading3 !=[]:
      for result_heading3 in results_heading3:
        result_get_heading3 = re.findall(pattern_get_heading3, str(result_heading3), re.S)
        results_ultag = re.findall(pattern_ultag, result_heading3, re.S)
        for result_ultag in results_ultag:
          results_ultag_list = re.findall(pattern_ultag_list, result_ultag, re.S)
          if results_ultag_list !=[]:
            results_tag = re.findall(pattern_tag, result_ultag, re.S)
            for result_tag in results_tag:
              print(str(result_tag))
              if(result_tag[2] !=""):
                results_tagnest = re.findall(pattern_tag_nest, result_tag[2], re.S)
                for result_tagnest in results_tagnest:
                  # print(result_tagnest[1], result_tagnest[3], result_tag[5], result_get_heading3[0], result_tab[0], i)
                  if not (results_ultag_list[0][0].startswith(" * ,,")):
                    results_ultag_list_li = re.findall(pattern_ultag_list_li, results_ultag_list[0][0], re.S)
                    results_ultag_list_list =[]
                    for result_ultag_list_li in results_ultag_list_li:
                      results_ultag_list_list.append(result_ultag_list_li[1])
                    d.append({"id":i, "tag":result_tagnest[1], "desc":result_tag[2], "type":result_get_heading3[0], "category":result_tab[0],
                              "list":results_ultag_list_list})
                    i=i+1
                  else:
                    d.append({"id":i, "tag":result_tagnest[1], "desc":result_tag[2], "type":result_get_heading3[0], "category":result_tab[0], "list":""})
                    i=i+1
              else:
                # print(result_tag[1], result_tag[3], result_tag[5], result_get_heading3[0], result_tab[0], i)
                if not (results_ultag_list[0][0].startswith(" * ,,")):
                  results_ultag_list_li = re.findall(pattern_ultag_list_li, results_ultag_list[0][0], re.S)
                  results_ultag_list_list =[]
                  for result_ultag_list_li in results_ultag_list_li:
                    results_ultag_list_list.append(result_ultag_list_li[1])
                  d.append({"id":i, "tag":result_tag[1], "desc":result_tag[2], "type":result_get_heading3[0], "category":result_tab[0], "list":results_ultag_list_list})
                  i=i+1
                else:
                  d.append({"id":i, "tag":result_tag[1], "desc":result_tag[2], "type":result_get_heading3[0], "category":result_tab[0], "list":""})
                  i=i+1

        results_tag = re.findall(pattern_tag, str(result_heading3), re.S)
        for result_tag in results_tag:
          if(result_tag[2] !=""):
            results_tagnest = re.findall(pattern_tag_nest, result_tag[2], re.S)
            for result_tagnest in results_tagnest:
              # print(result_tagnest[1], result_tagnest[3], result_tag[5], result_get_heading3[0], result_tab[0], i)
              d.append({"id":i, "tag":result_tagnest[1], "trans":result_tagnest[3], "desc":result_tag[2], "type":result_get_heading3[0], "category":result_tab[0], "list":""})
              i=i+1
          else:
            # print(result_tag[1], result_tag[3], result_tag[5], result_get_heading3[0], result_tab[0], i)
            d.append({"id":i, "tag":result_tag[1], "trans":result_tag[3], "desc":result_tag[2], "type":result_get_heading3[0], "category":result_tab[0], "list":""})
            i=i+1

    else:
      results_ultag = re.findall(pattern_ultag, result_tab[1], re.S)
      for result_ultag in results_ultag:
        results_ultag_list = re.findall(pattern_ultag_list, result_ultag, re.S)
        if results_ultag_list !=[]:
          print(results_ultag_list)
          results_tag = re.findall(pattern_tag, result_ultag, re.S)
          print(results_tag)
          for result_tag in results_tag:
            if(result_tag[2] !=""):
              print(result_tag[2])
              results_tagnest = re.findall(pattern_tag_nest, result_tag[2], re.S)
              for result_tagnest in results_tagnest:
                # print(result_tagnest[1], result_tagnest[3], result_tag[5], result_get_heading3[0], result_tab[0], i)

                if not (results_ultag_list[0][0].startswith(" * ,,")):
                  results_ultag_list_li = re.findall(pattern_ultag_list_li, results_ultag_list[0][0], re.S)
                  results_ultag_list_list =[]
                  for result_ultag_list_li in results_ultag_list_li:
                    results_ultag_list_list.append(result_ultag_list_li[1])
                  d.append({"id":i, "tag":result_tagnest[1], "desc":result_tag[2], "category":result_tab[0], "list":results_ultag_list_list, "type":""})
                  i=i+1
                else:
                  d.append({"id":i, "tag":result_tagnest[1], "desc":result_tag[2], "category":result_tab[0], "list":"", "type":""})
                  i=i+1
            else:
              # print(result_tag[1], result_tag[3], result_tag[5], result_get_heading3[0], result_tab[0], i)
              if not (results_ultag_list[0][0].startswith(" * ,,")):
                results_ultag_list_li = re.findall(pattern_ultag_list_li, results_ultag_list[0][0], re.S)
                results_ultag_list_list =[]
                for result_ultag_list_li in results_ultag_list_li:
                  results_ultag_list_list.append(result_ultag_list_li[1])
                d.append({"id":i, "tag":result_tag[1], "trans":result_tag[3], "desc":result_tag[5], "category":result_tab[0], "list":results_ultag_list_list})
                i=i+1
              else:
                d.append({"id":i, "tag":result_tag[1], "desc":result_tag[2], "category":result_tab[0], "list":"", "type":""})
                i=i+1

      results_tag = re.findall(pattern_tag, result_tab[1], re.S)
      for result_tag in results_tag:
        if(result_tag[2] !=""):
          results_tagnest = re.findall(pattern_tag_nest, result_tag[2], re.S)
          for result_tagnest in results_tagnest:
            # print(result_tagnest[1], result_tagnest[3], result_tag[5], "", result_tab[0], i)
            d.append({"id":i, "tag":result_tagnest[1], "desc":result_tag[2], "category":result_tab[0], "list":"", "type":""})
            i=i+1
        else:
          # print(result_tag[1], result_tag[3], result_tag[5], "", result_tab[0], i)
          d.append({"id":i, "tag":result_tag[1], "desc":result_tag[2], "category":result_tab[0], "list":"", "type":""})
          i=i+1

  # print(d)
  no_lis = [e['tag'] for e in d]
  d = [e for i, e in enumerate(d) if e['tag'] not in no_lis[0:i]]
  return d

# def anchor(text: str) -> str:
#   reg_anchors ='(\[\[a\_{0,1} (.*?)\]\](.*?)\[\[\/a\]\]|\[(.*?) (.*?)\]|\[\[\[(.*?)\|(.*?)\]\]\])'
#   results_anchor = re.findall(reg_anchors, text, re.S)
#   anchor,html_anchor = "",""
#   for res_anchor in results_anchor:
#     if (res_anchor[1]!="")and(res_anchor[2]!=""):
#       anchor="<a "+res_anchor[1] +">" + res_anchor[2] +"</a>"
#       html_anchor = "<a "+res_anchor[1] +">" + res_anchor[2] +"</a>"
#     elif (res_anchor[3]!="")and(res_anchor[4]!=""):
#       anchor =  "<a href='"+res_anchor[3] +"' target='_blank'>" + res_anchor[4] +"</a>"
#       html_anchor = "<a href='"+res_anchor[3] +"' target='_blank'>" + res_anchor[4] +"</a>"
#     elif (res_anchor[5]!="")and(res_anchor[6]!=""):
#       anchor = "<a href='"+res_anchor[5] +"' target='_blank'>" + res_anchor[6] +"</a>"
#       html_anchor = "<a href='"+res_anchor[5] +"' target='_blank'>" + res_anchor[6] +"</a>"
#     else:
#       html_anchor = anchor + text
#   return html_anchor



if __name__ == '__main__':
  f = open("./scp-wiki/tags/tags_commented.md", "r", encoding="utf-8_sig")
  data = f.read()
  f.close()
  d = []
  i=0
  e = parse(i, d, data)
  with open("./scp-wiki/tags/tags.json", "w", encoding="utf-8_sig") as f:
    json.dump(e, f, indent=4, ensure_ascii=False)
