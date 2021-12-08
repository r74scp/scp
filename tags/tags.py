import re

f = open("./tags/tags.md", "r", encoding="utf-8_sig")
data = f.read()
f.close()

f = open('./tags/tags_commented.md', 'w', encoding="utf-8_sig")
re_data = re.sub(r'(\n)?\[!\-\-(.*?)\-\-\]', '', data, flags=(re.IGNORECASE | re.DOTALL))
f.write(re_data)
f.close()

# \*\s(|(,,(.{1,2}),,){1,})\*\*\[\[\[\/system:page-tags/tag/(.*)\|(.*)\]\]\]\*\*\s\/\/\((.*)\)\/\/\s-\s
# \*\*\[\[\[/system:page-tags/tag/(.*?)\|(.*?)\]\]\]\*\*( \/\/\((.*?)\)\/\/|) タグと外国名
# (\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*( \/\/\((.*?)\)\/\/|))(.*) - (.*)$ タグ 外国名 説明 多分複数同じ行にある場合はforで回せるはず

# \* ((,,.{1,2},,){1,}|)(\*\*\[\[\[/system:page-tags/tag/(.*?)\|.*?\]\]\]\*\*( \/\/\((.*?)\)\/\/|))(.*) - (.*)$
