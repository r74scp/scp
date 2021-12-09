# coding: UTF-8
import re
#
html = '''

* ,,,,**[[[/system:page-tags/tag/scp|scp]]]** //(scp)// - [/scp-series メインブロック]、[/scp-001 001提言]、[/joke-scps Joke(-J)]、[/scp-ex Explained(-EX)]、[/scp-d Decommissioned(-D)]のいずれかに属する[[footnote]]何らかの理由でアーカイブされ、これらの分類から外れた場合も含みます。[[/footnote]]SCP報告書の記事に付与されるタグです。//scp//タグが使用される場合、オブジェクトクラスカテゴリのタグのいずれかと併用されねばなりません。作成に関しては[[[how-to-write:post-scp|]]]を参照してください。
 * **[[[/system:page-tags/tag/explained|explained]]]** //(explained)// - //scp//タグの特殊なサブクラスであり、Explained(-EX)の報告書に付与されるタグです。必ず//scp//タグ及びいずれかのオブジェクトクラスタグと併用されねばなりません。[#faq 一般的なFAQ]及び[#faq 翻訳に関するFAQ]も参照してください。
 * ,,︁,,,,,,**[[[/system:page-tags/tag/decommissioned|decommissioned]]]** //(decommissioned)// - //scp//タグの特殊なサブクラスであり、Decommissioned(-D)の報告書に付与されるタグです。必ず//scp//タグ及びいずれかのオブジェクトクラスタグと併用されねばなりません。新規作成は認められておらず、該当ページはアーカイブされています。
 * **[[[/system:page-tags/tag/白|白]]]** //(blanc)// / **[[[/system:page-tags/tag/青|青]]]** //(bleu)// / **[[[/system:page-tags/tag/緑|緑]]]** //(vert)// / **[[[/system:page-tags/tag/黄|黄]]]** //(jaune)// / **[[[/system:page-tags/tag/橙|橙]]]** //(orange)// / **[[[/system:page-tags/tag/赤|赤]]]** //(rouge)// / **[[[/system:page-tags/tag/黒|黒]]]** //(noir)// / **[[[/system:page-tags/tag/未定|未定]]]** //(indéterminé)// - [[[niveaux-de-menace-des-objets-scp|脅威レベル]]]が付与されていることを表すタグです。必ず//scp//タグ及びいずれかのオブジェクトクラスタグと併用されねばなりません。
'''
pattern_ultag = '\* \*\*.*?(?=\* \*\*|$)'
pattern_ultag_list = '( \* (.*?)$)'
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
          # print(result_tagnest[1], result_tagnest[3], result_tag[5], list(filter(lambda a: a != '', re.split(' \* |\n', results_ultag_list[0][0]))))
      else:
        if not (results_ultag_list[0][0].startswith(" * ,,")):
          print(results_ultag_list[0][0])
        # print(result_tag[1], result_tag[3], result_tag[5], list(filter(lambda a: a != '', re.split(' \* |\n', results_ultag_list[0][0]))))
  else:
    results_tag = re.findall(pattern_tag, result_ultag, re.S)
    for result_tag in results_tag:
      if(result_tag[4] !=""):
        results_tagnest = re.findall(pattern_tag_nest, result_tag[4], re.S)
        for result_tagnest in results_tagnest:
          print(result_tagnest[1], result_tagnest[3], result_tag[5])
      else:
        print(result_tag[1], result_tag[3], result_tag[5])
