# coding: UTF-8
import re
#
html = '''
* **[[[/system:page-tags/tag/蘇生|蘇生]]]** //(reanimation)// - 臨床死状態から、他者または自身の一部または全てを蘇生させるSCPの記事に付与されるタグです。
 * 適切ならば//死体//タグと併用してください。
 * 適切ならば//死d体//タグと併用してください。
 * 適切ならば//死s体//タグと併用してください。
[[>]]
[#attribute-toc 目次へ]
[[/>]]

++ た行[[# attribute-t]]

* **[[[/system:page-tags/tag/蘇生|蘇生]]]** //(reanimation)// - 臨床死状態から、他者または自身の一部または全てを蘇生させるSCPの記事に付与されるタグです。
 * ss適切ならば//死体//タグと併用してください。
 * sas適切ならば//死d体//タグと併用してください。
 * 適assasa切ならば//死s体//タグと併用してください。
[[>]]
[#attribute-toc 目次へ]
[[/>]]

++ as行[[# attribute-t]]
'''
pattern_ultag = '\* \*\*.*?(?=\* \*\*|$)'
pattern_ultag_list = '( \* (.*?)$)'
pattern_ultag_list_li = '( \* (.*?))\\n'
pattern_tag = '(\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*)( \/\/\((.*?)\)\/\/|)(.*?) - (.*?)\n'
pattern_tag_nest = '(\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*( \/\/\((.*?)\)\/\/|))'


results_ultag = re.findall(pattern_ultag, html, re.S)

# Type:list
# print((results_ultag))

# 抽出
for result_ultag in results_ultag:
  results_ultag_list = re.findall(pattern_ultag_list, result_ultag, re.S)
  if results_ultag_list !=[]:
    results_tag = re.findall(pattern_tag, result_ultag, re.S)
    for result_tag in results_tag:
      if(result_tag[4] !=""):
        results_tagnest = re.findall(pattern_tag_nest, result_tag[4], re.S)
        for result_tagnest in results_tagnest:
          print(results_ultag_list[0][0])
          print(result_tagnest[1], result_tagnest[3], result_tag[5], results_ultag_list[0][0])
      else:
        if not (results_ultag_list[0][0].startswith(" * ,,")):
          results_ultag_list_li = re.findall(pattern_ultag_list_li, results_ultag_list[0][0], re.S)
          results_ultag_list_list =[]
          for result_ultag_list_li in results_ultag_list_li:
            results_ultag_list_list.append(result_ultag_list_li[1])
        # print(result_tag[1], result_tag[3], result_tag[5], list(filter(lambda a: a != '', re.split(' \* |\n', results_ultag_list[0][0]))))
          print(result_tag[1], result_tag[3], result_tag[5], results_ultag_list_list)
  else:
    results_tag = re.findall(pattern_tag, result_ultag, re.S)
    for result_tag in results_tag:
      if(result_tag[4] !=""):
        results_tagnest = re.findall(pattern_tag_nest, result_tag[4], re.S)
        for result_tagnest in results_tagnest:
          print(result_tagnest[1], result_tagnest[3], result_tag[5])
      else:
        print(result_tag[1], result_tag[3], result_tag[5])
