# coding: UTF-8
import re
#
html = '''
+++ 正要注意団体-EN
それぞれの詳細は[[[groups-of-interest|]]]を参照してください。

* **[[[/system:page-tags/tag/alexylva大学|alexylva大学]]]** //(alexylva)// - [[[alexylva-university-hub|Alexylva大学]]]。
* **[[[/system:page-tags/tag/アンブローズ・レストラン|アンブローズ・レストラン]]]** //(ambrose-restaurant)// - [[[ambrose-restaurant-hub|アンブローズ・レストラン]]]。
* **[[[/system:page-tags/tag/アンダーソン|アンダーソン]]]** //(anderson)// - [[[anderson-robotics-hub|アンダーソン・ロボティクス]]]。
* **[[[/system:page-tags/tag/アルカディア|アルカディア]]]** //(arcadia)// - [[[arcadia-hub|アルカディア]]]。
* **[[[/system:page-tags/tag/are-we-cool-yet|are-we-cool-yet]]]** //(are-we-cool-yet)// - [[[are-we-cool-yet-hub|Are We Cool Yet? (AWCY)]]]。
* **[[[/system:page-tags/tag/黒の女王|黒の女王]]]** //(black-queen)// - [[[black-queen-hub|黒の女王]]]。
* **[[[/system:page-tags/tag/カオス・インサージェンシー|カオス・インサージェンシー]]]** //(chaos-insurgency)// - [[[chaos-insurgency-hub|カオス・インサージェンシー (CI)]]]。
* **[[[/system:page-tags/tag/シカゴ・スピリット|シカゴ・スピリット]]]** //(chicago-spirit)// - [[[chicago-spirit|シカゴ・スピリット]]]。
* **[[[/system:page-tags/tag/壊れた神の教会|壊れた神の教会]]]** //(broken-god)// - [[[church-of-the-broken-god-hub|壊れた神の教会 (CotBG)]]]。
* **[[[/system:page-tags/tag/第二ハイトス教会|第二ハイトス教会]]]** //(second-hytoth)// - [[[second-hytoth-hub|第二ハイトス教会]]]。
* **[[[/system:page-tags/tag/ディア大学|ディア大学]]]** //(deer-college)// - [[[deer-college-hub|ディア大学]]]。
* **[[[/system:page-tags/tag/ワンダーテインメント博士|ワンダーテインメント博士]]]** //(dr-wondertainment)// - [[[dr-wondertainment-hub|ワンダーテインメント博士]]]。
* **[[[/system:page-tags/tag/ファクトリー|ファクトリー]]]** //(factory)// - [[[factory-hub|ザ・ファクトリー]]]。
* **[[[/system:page-tags/tag/第五教会|第五教会]]]** //(fifthist)// - [[[fifthist-hub|第五教会]]]。
* **[[[/system:page-tags/tag/ゲーマーズアゲインストウィード|ゲーマーズアゲインストウィード]]]** //(gamers-against-weed)// - [[[gamers-against-weed-hub|ゲーマーズアゲインストウィード]]]。
* **[[[/system:page-tags/tag/世界オカルト連合|世界オカルト連合]]]** //(global-occult-coalition)// - [[[goc-hub-page|世界オカルト連合 (GOC)]]]。
* **[[[/system:page-tags/tag/gru-p-部局|gru-p-部局]]]** //(gru-division-p)// - [[[gru-p-hub|ロシア連邦軍参謀本部情報総局"P"部局]]]。
* **[[[/system:page-tags/tag/ハーマン・フラー|ハーマン・フラー]]]** //(herman-fuller)// - [[[herman-fuller-hub|ハーマン・フラーの不気味サーカス]]]。
* **[[[/system:page-tags/tag/境界線イニシアチブ|境界線イニシアチブ]]]** //(horizon-initiative)// - [[[horizon-initiative-hub|境界線イニシアチブ]]]。
* **[[[/system:page-tags/tag/ijamea|ijamea]]]** //(ijamea)// - [[[ijamea-hub|大日本帝国異常事例調査局 (IJAMEA)]]]。
* **[[[/system:page-tags/tag/マナによる慈善財団|マナによる慈善財団]]]** //(manna-charitable-foundation)// - [[[manna-charitable-foundation-hub|マナによる慈善財団]]]。
* **[[[/system:page-tags/tag/mc&d|mc&d]]]** //(marshall-carter-and-dark)// - [[[marshall-carter-and-dark-hub|マーシャル・カーター＆ダーク株式会社 (MC&D)]]]。
* **[[[/system:page-tags/tag/何者でもない|何者でもない]]]** //(nobody)// - [[[nobody-hub|「何者でもない」]]]。
* **[[[/system:page-tags/tag/oria|oria]]]** //(reclamation)// - [[[oria-hub|イスラム・アーティファクト開発事務局 (ORIA)]]]。
* **[[[/system:page-tags/tag/オネイロイ|オネイロイ]]]** //(oneiroi)// - [[[oneiroi|オネイロイ・コレクティブ]]]。
* **[[[/system:page-tags/tag/パラウォッチ|パラウォッチ]]]** //(parawatch)// - [[[parawatch-hub|パラウォッチWiki]]]。
* **[[[/system:page-tags/tag/プロメテウス|プロメテウス]]]** //(prometheus)// - [[[prometheus-labs-hub|株式会社プロメテウス研究所]]]。
* **[[[/system:page-tags/tag/サーキック|サーキック]]]** //(sarkic)// - [[[sarkicism-hub|サーキック・カルト]]]。
* **[[[/system:page-tags/tag/蛇の手|蛇の手]]]** //(serpents-hand)// - [[[serpent-s-hand-hub|蛇の手]]]。
* **[[[/system:page-tags/tag/サメ殴りセンター|サメ殴りセンター]]]** //(shark-punching-center)// - [[[spc-hub|サメ殴りセンター (SPC)]]]。
* **[[[/system:page-tags/tag/三ツ月イニシアチブ|三ツ月イニシアチブ]]]** //(three-moons-initiative)// - [[[three-moons-initiative-hub|三ツ月イニシアチブ]]]。
* **[[[/system:page-tags/tag/異常事件課|異常事件課]]]** //(unusual-incidents-unit)// - [[[unusual-incidents-unit-hub|連邦捜査局 (FBI) 異常事件課 (UIU)]]]。
* **[[[/system:page-tags/tag/ヴィキャンデル・ニード|ヴィキャンデル・ニード]]]** //(vikander-kneed)// - [[[vikander-kneed-technical-media-hub|ヴィキャンデル=ニード・テクニカル・メディア]]]。
* **[[[/system:page-tags/tag/堂守連盟|堂守連盟]]]** //(wandsmen)// - [[[wandsmen-hub|堂守連盟]]]。
* **[[[/system:page-tags/tag/ウィルソンズ・ワイルドライフ|ウィルソンズ・ワイルドライフ]]]** //(wilsons-wildlife)// - [[[wilson-s-wildlife-solutions-hub|ウィルソンズ・ワイルドライフ・ソリューションズ (WWS)]]]。

+++ 準要注意団体-EN

* **[[[/system:page-tags/tag/accelerate-the-future|accelerate-the-future]]]** //(accelerate-the-future)// - Accelerate the Future。
* **[[[/system:page-tags/tag/asci|asci]]]** //(asci)// - 全米確保収容イニシアチブ (ASCI)。
* **[[[/system:page-tags/tag/アベラール|アベラール]]]** //(avelar)// - アベラール・プロフェッショナル・プロダクツ。
* **[[[/system:page-tags/tag/blackwood|blackwood]]]** //(blackwood)// - blackwood卿の冒険譚。
* **[[[/system:page-tags/tag/british-occult-service|british-occult-service]]]** //(british-occult-service)// - 英国オカルト庁/英国オカルト局 (MI666)。
* **[[[/system:page-tags/tag/brothers-of-death|brothers-of-death]]]** //(brothers-of-death)// - brothers-of-death。
* **[[[/system:page-tags/tag/夜闇の子ら|夜闇の子ら]]]** //(children-of-the-night)// - 夜闇の子ら(参照: [[[scp-1000|]]])。
* **[[[/system:page-tags/tag/松明の子供達|松明の子供達]]]** //(children-of-the-torch)// - 松明の子供達。
* **[[[/system:page-tags/tag/class-of-76|class-of-76]]]** //(class-of-76)// - [[[remembrance|Class of '76]]]。
* **[[[/system:page-tags/tag/daevite|daevite]]]** //(daevite)// - ダエーバイト。
* **[[[/system:page-tags/tag/金帳汗国|金帳汗国]]]** //(golden-horde)// - 金帳汗国。
* **[[[/system:page-tags/tag/hmfscp|hmfscp]]]** //(hmfscp)// - 超常現象の確保収容に関する王立財団 / 珍品と過ぎ往く幻想の研究の為の王立財団 (HMFSCP)。
* **[[[/system:page-tags/tag/icsut|icsut]]]** (//icsut//) - 国際統一奇跡論研究センター (ICSUT)。
* **[[[/system:page-tags/tag/ラ・リュー・マカーブラー|ラ・リュー・マカーブラー]]]** //(la-rue-macabre)// - [[[larue-hub|ラ・リュー・マカーブラー]]]。要注意領域-ENの項目も参照してください。
* **[[[/system:page-tags/tag/名もなきもの|名もなきもの]]]** //(nameless)// - [[[SCP-4000]]]に登場する”名もなきもの”あるいは”妖精”。
* **[[[/system:page-tags/tag/監督真司令部|監督真司令部]]]** //(obearwatch)// - [[span class="ruby"]]監督真司令部[[span class="rt"]]かんと**くま**しれいぶ[[/span]][[/span]]
* **[[[/system:page-tags/tag/オブスクラ|オブスクラ]]]** //(obskura)// - アーネンエルベ・オブスクラ軍団、またはその後継組織であるオブスクラ。
* **[[[/system:page-tags/tag/パングロス|パングロス]]]** //(pangloss)// - パングロス。
* **[[[/system:page-tags/tag/pattern-screamer|pattern-screamer]]]** //(pattern-screamer)// - パターン・スクリーマーズ。
* **[[[/system:page-tags/tag/ペンタグラム|ペンタグラム]]]** //(pentagram)// - ペンタグラム。
* **[[[/system:page-tags/tag/aw教授|aw教授]]]** //(professor-aw)// - aw教授の発明物。
* **[[[/system:page-tags/tag/silicon-nornir|silicon-nornir]]]** //(silicon-nornir)// - 硅/硅素のノルニルの従者達。
* **[[[/system:page-tags/tag/シュガーコム製菓|シュガーコム製菓]]]** //(sugarcomb-confectionery)// - シュガーコム製菓。
* **[[[/system:page-tags/tag/トトレイソフト|トトレイソフト]]]** //(totleighsoft)// - 異常なソフトウェア開発企業、トトレイソフト。
* **[[[/system:page-tags/tag/異常積荷委員会|異常積荷委員会]]]** (//unusual-cargo//) - 異常積荷委員会。
* **[[[/system:page-tags/tag/ウェストヘッド・メディア|ウェストヘッド・メディア]]]** //(westhead-media)// - ウェストヘッド・メディア。
* **[[[/system:page-tags/tag/夏王朝|夏王朝]]]** //(xia-dynasty)// - 夏王朝。

以下のタグについては、特定の他支部の項を参照してください。

* **[[[/system:page-tags/tag/saphir|saphir]]]** //(sapphire)// - 要注意団体-FRの項を参照してください。
* **[[[/system:page-tags/tag/madao|madao]]]** //(medicea-accademia)// - 要注意団体-ITの項を参照してください。
* **[[[/system:page-tags/tag/魔術師学会|魔術師学会]]]** //(mages-academy)// - 要注意団体-DEの項を参照してください。
* **[[[/system:page-tags/tag/陰陽寮|陰陽寮]]]** - JP側で独自に登録されたタグです。準要注意団体-JPの項を参照してください。
* **[[[/system:page-tags/tag/ライト・クーリエ・エンタープライズ|ライト・クーリエ・エンタープライズ]]]** - JP側で独自に登録されたタグです。準要注意団体-JPの項を参照してください。

以下のタグについては、別のカテゴリの項目を参照してください。

* **[[[/system:page-tags/tag/解体部門|解体部門]]]** //(decommissioning-dept)// - 「財団下部組織」の項を参照してください。
* **[[[/system:page-tags/tag/倫理委員会|倫理委員会]]]** //(ethics-committee)// - 「財団下部組織」の項を参照してください。
* **[[[/system:page-tags/tag/誤伝達部門|誤伝達部門]]]** //(miscommunications)// - 「財団下部組織」の項を参照してください。
* **[[[/system:page-tags/tag/戦術神学部門|戦術神学部門]]]** //(tactical-theology)// - 「財団下部組織」の項を参照してください。
'''
pattern = '(\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*)( \/\/\((.*?)\)\/\/|)(.*?) - (.*?)\n'
pattern_4 = '(\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*( \/\/\((.*?)\)\/\/|))'
results = re.findall(pattern, html, re.S)

# Type:list
# print((results))

# 抽出
for result in results:
  if(result[4] !=""):
    results_4 = re.findall(pattern_4, result[4], re.S)
    for res in results_4:
      print(res[1], res[3], result[5])
  print(result[1], result[3], result[5])
