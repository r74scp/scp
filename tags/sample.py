# coding: UTF-8
import re
#
html = '''
* ,,,,**[[[/system:page-tags/tag/scp|scp]]]** //(scp)// - [/scp-series メインブロック]、[/scp-001 001提言]、[/joke-scps Joke(-J)]、[/scp-ex Explained(-EX)]、[/scp-d Decommissioned(-D)]のいずれかに属する[[footnote]]何らかの理由でアーカイブされ、これらの分類から外れた場合も含みます。[[/footnote]]SCP報告書の記事に付与されるタグです。//scp//タグが使用される場合、オブジェクトクラスカテゴリのタグのいずれかと併用されねばなりません。作成に関しては[[[how-to-write:post-scp|]]]を参照してください。
 * **[[[/system:page-tags/tag/explained|explained]]]** //(explained)// - //scp//タグの特殊なサブクラスであり、Explained(-EX)の報告書に付与されるタグです。必ず//scp//タグ及びいずれかのオブジェクトクラスタグと併用されねばなりません。[#faq 一般的なFAQ]及び[#faq 翻訳に関するFAQ]も参照してください。
 * ,,︁,,,,,,**[[[/system:page-tags/tag/decommissioned|decommissioned]]]** //(decommissioned)// - //scp//タグの特殊なサブクラスであり、Decommissioned(-D)の報告書に付与されるタグです。必ず//scp//タグ及びいずれかのオブジェクトクラスタグと併用されねばなりません。新規作成は認められておらず、該当ページはアーカイブされています。
 * **[[[/system:page-tags/tag/白|白]]]** //(blanc)// / **[[[/system:page-tags/tag/青|青]]]** //(bleu)// / **[[[/system:page-tags/tag/緑|緑]]]** //(vert)// / **[[[/system:page-tags/tag/黄|黄]]]** //(jaune)// / **[[[/system:page-tags/tag/橙|橙]]]** //(orange)// / **[[[/system:page-tags/tag/赤|赤]]]** //(rouge)// / **[[[/system:page-tags/tag/黒|黒]]]** //(noir)// / **[[[/system:page-tags/tag/未定|未定]]]** //(indéterminé)// - [[[niveaux-de-menace-des-objets-scp|脅威レベル]]]が付与されていることを表すタグです。必ず//scp//タグ及びいずれかのオブジェクトクラスタグと併用されねばなりません。

* ,,,,**[[[/system:page-tags/tag/goi-format|goi-format]]]** //(goi-format)// - ある特定の要注意団体(GoI)の視点で記述された独自のフォーマットの記事[[footnote]]SCP-ENの定義では、「GoIハブで用意されているフォーマットに従う」と制限がありますが、JPでは導入されていません。[[/footnote]]に付与されるタグです。必ずGoIフォーマット隠しタグ1つと併用されねばなりません。作成に関しては[[[how-to-write:post-goi-format|]]]を参照してください。

'''
pattern = '(\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*)( \/\/\((.*?)\)\/\/|)(.*?) - (.*?)\n'

results = re.findall(pattern, html, re.S)

# Type:list
print((results))

# 抽出
for result in results:
  print(result[1], result[3], result[4], result[5])
