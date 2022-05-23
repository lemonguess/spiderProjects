from xpinyin import Pinyin
"汉字转拼音"
P = Pinyin()  # 实例化


print(P.get_pinyin("长沙"))  # chang-sha
print(P.get_pinyin("长沙", ""))  # changsha
print(P.get_pinyin("长沙", tone_marks='marks'))  # cháng-shā
print(P.get_pinyin("长沙", " "))  # chang sha

print(P.get_initial("长"))  # C
print(P.get_initial("沙"))  # S
print(P.get_initials("长沙"))  # C-S
print(P.get_initials("长沙", ""))  # CS
