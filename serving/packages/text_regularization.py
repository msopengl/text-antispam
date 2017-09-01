#! /usr/bin/env python3

import re
# import opencc


def strtr(text, replace):
    for s, r in replace.items():
        text = text.replace(s, r)
    return text


# def simplify(text):
#     return opencc.convert(text)


# def traditionalize(text):
#     """ https://pypi.python.org/pypi/OpenCC
#     """
#     return opencc.convert(text, config='s2t.json')


def sbcCase(text):
    """转换全角字符为半角字符
    SBC case to DBC case
    """
    return strtr(text, {
        "０" : "0", "１" : "1", "２" : "2", "３" : "3", "４" : "4",
        "５" : "5", "６" : "6", "７" : "7", "８" : "8", "９" : "9",
        'Ａ' : 'A', 'Ｂ' : 'B', 'Ｃ' : 'C', 'Ｄ' : 'D', 'Ｅ' : 'E',
        'Ｆ' : 'F', 'Ｇ' : 'G', 'Ｈ' : 'H', 'Ｉ' : 'I', 'Ｊ' : 'J',
        'Ｋ' : 'K', 'Ｌ' : 'L', 'Ｍ' : 'M', 'Ｎ' : 'N', 'Ｏ' : 'O',
        'Ｐ' : 'P', 'Ｑ' : 'Q', 'Ｒ' : 'R', 'Ｓ' : 'S', 'Ｔ' : 'T',
        'Ｕ' : 'U', 'Ｖ' : 'V', 'Ｗ' : 'W', 'Ｘ' : 'X', 'Ｙ' : 'Y',
        'Ｚ' : 'Z', 'ａ' : 'a', 'ｂ' : 'b', 'ｃ' : 'c', 'ｄ' : 'd',
        'ｅ' : 'e', 'ｆ' : 'f', 'ｇ' : 'g', 'ｈ' : 'h', 'ｉ' : 'i',
        'ｊ' : 'j', 'ｋ' : 'k', 'ｌ' : 'l', 'ｍ' : 'm', 'ｎ' : 'n',
        'ｏ' : 'o', 'ｐ' : 'p', 'ｑ' : 'q', 'ｒ' : 'r', 'ｓ' : 's',
        'ｔ' : 't', 'ｕ' : 'u', 'ｖ' : 'v', 'ｗ' : 'w', 'ｘ' : 'x',
        'ｙ' : 'y', 'ｚ' : 'z',
    })


def circleCase(text):
    """转换①数字为半角数字
    ①②③④⑤⑥⑦⑧⑨⑩ case 全角
    ❹❸❽❼❽❼❾❽❼
    ➀➁➂➃➄➅➆➇➈
    """
    return strtr(text, {
        "➀" : "1", "➁" : "2", "➂" : "3", "➃" : "4", "➄" : "5",
        "➅" : "6", "➆" : "7", "➇" : "8", "➈" : "9", "①" : "1",
        "②" : "2", "③" : "3", "④" : "4", "⑤" : "5", "⑥" : "6",
        "⑦" : "7", "⑧" : "8", "⑨" : "9", "❶" : "1", "❷" : "2",
        "❸" : "3", "❹" : "4", "❺" : "5", "❻" : "6", "❼" : "7",
        "❽" : "8", "❾" : "9", "➊" : "1", "➋" : "2", "➌" : "3",
        "➍" : "4", "➎" : "5", "➏" : "6", "➐" : "7", "➑" : "8",
        "➒" : "9", 'Ⓐ' : 'A', 'Ⓑ' : 'B', 'Ⓒ' : 'C', 'Ⓓ' : 'D',
        'Ⓔ' : 'E', 'Ⓕ' : 'F', 'Ⓖ' : 'G', 'Ⓗ' : 'H', 'Ⓘ' : 'I',
        'Ⓙ' : 'J', 'Ⓚ' : 'K', 'Ⓛ' : 'L', 'Ⓜ' : 'M', 'Ⓝ' : 'N',
        'Ⓞ' : 'O', 'Ⓟ' : 'P', 'Ⓠ' : 'Q', 'Ⓡ' : 'R', 'Ⓢ' : 'S',
        'Ⓣ' : 'T', 'Ⓤ' : 'U', 'Ⓥ' : 'V', 'Ⓦ' : 'W', 'Ⓧ' : 'X',
        'Ⓨ' : 'Y', 'Ⓩ' : 'Z', 'ⓐ' : 'a', 'ⓑ' : 'b', 'ⓒ' : 'c',
        'ⓓ' : 'd', 'ⓔ' : 'e', 'ⓕ' : 'f', 'ⓖ' : 'g', 'ⓗ' : 'h',
        'ⓘ' : 'i', 'ⓙ' : 'j', 'ⓚ' : 'k', 'ⓛ' : 'l', 'ⓜ' : 'm',
        'ⓝ' : 'n', 'ⓞ' : 'o', 'ⓟ' : 'p', 'ⓠ' : 'q', 'ⓡ' : 'r',
        'ⓢ' : 's', 'ⓣ' : 't', 'ⓤ' : 'u', 'ⓥ' : 'v', 'ⓦ' : 'w',
        'ⓧ' : 'x', 'ⓨ' : 'y', 'ⓩ' : 'z',
        "㊀" : "一", "㊁" : "二", "㊂" : "三", "㊃" : "四",
        "㊄" : "五", "㊅" : "六", "㊆" : "七", "㊇" : "八",
        "㊈" : "九",
    })


def bracketCase(text):
    """转换⑴数字为半角数字
    ⑴ ⑵ ⑶ ⑷ ⑸ ⑹ ⑺ ⑻ ⑼case 全角
    """
    return strtr(text, {
        "⑴" : "1", "⑵" : "2", "⑶" : "3", "⑷" : "4", "⑸" : "5",
        "⑹" : "6", "⑺" : "7", "⑻" : "8", "⑼" : "9",
        '🄐' : 'A', '🄑' : 'B', '🄒' : 'C', '🄓' : 'D', '🄔' : 'E',
        '🄕' : 'F', '🄖' : 'G', '🄗' : 'H', '🄘' : 'I', '🄙' : 'J',
        '🄚' : 'K', '🄛' : 'L', '🄜' : 'M', '🄝' : 'N', '🄞' : 'O',
        '🄟' : 'P', '🄠' : 'Q', '🄡' : 'R', '🄢' : 'S', '🄣' : 'T',
        '🄤' : 'U', '🄥' : 'V', '🄦' : 'W', '🄧' : 'X', '🄨' : 'Y',
        '🄩' : 'Z', '⒜' : 'a', '⒝' : 'b', '⒞' : 'c', '⒟' : 'd',
        '⒠' : 'e', '⒡' : 'f', '⒢' : 'g', '⒣' : 'h', '⒤' : 'i',
        '⒥' : 'j', '⒦' : 'k', '⒧' : 'l', '⒨' : 'm', '⒩' : 'n',
        '⒪' : 'o', '⒫' : 'p', '⒬' : 'q', '⒭' : 'r', '⒮' : 's',
        '⒯' : 't', '⒰' : 'u', '⒱' : 'v', '⒲' : 'w', '⒳' : 'x',
        '⒴' : 'y', '⒵' : 'z',
        "㈠" : "一", "㈡" : "二", "㈢" : "三", "㈣" : "四",
        "㈤" : "五", "㈥" : "六", "㈦" : "七", "㈧" : "八",
        "㈨" : "九",
    })


def dotCase(text):
    """转换⑴数字为半角数字
    ⒈⒉⒊⒋⒌⒍⒎⒏⒐case 全角
    """
    return strtr(text, {
        "⒈" : "1",
        "⒉" : "2",
        "⒊" : "3",
        "⒋" : "4",
        "⒌" : "5",
        "⒍" : "6",
        "⒎" : "7",
        "⒏" : "8",
        "⒐" : "9",
    })


def specialCase(text):
    """特殊字符比如希腊字符，西里尔字母
    """
    return strtr(text, {
        # 希腊字母
        "Α" : "A", "Β" : "B", "Ε" : "E", "Ζ" : "Z", "Η" : "H",
        "Ι" : "I", "Κ" : "K", "Μ" : "M", "Ν" : "N", "Ο" : "O",
        "Ρ" : "P", "Τ" : "T", "Χ" : "X", "α" : "a", "β" : "b",
        "γ" : "y", "ι" : "l", "κ" : "k", "μ" : "u", "ν" : "v",
        "ο" : "o", "ρ" : "p", "τ" : "t", "χ" : "x",

        # 西里尔字母 (U+0400 - U+04FF)
        "Ѐ" : "E", "Ё" : "E", "Ѕ" : "S", "І" : "I", "Ї" : "I",
        "Ј" : "J", "Ќ" : "K", "А" : "A", "В" : "B", "Е" : "E",
        "З" : "3", "Ζ" : "Z", "И" : "N", "М" : "M", "Н" : "H",
        "О" : "O", "Р" : "P", "С" : "C", "Т" : "T", "У" : "y",
        "Х" : "X", "Ь" : "b", "Ъ" : "b", "а" : "a", "в" : "B",
        "е" : "e", "к" : "K", "м" : "M", "н" : "H", "о" : "O",
        "п" : "n", "р" : "P", "с" : "c", "т" : "T", "у" : "y",
        "х" : "x", "ш" : "w", "ь" : "b", "ѕ" : "s", "і" : "i",
        "ј" : "j",

        "À" : "A", "Á" : "A", "Â" : "A", "Ã" : "A", "Ä" : "A", "Å" : "A", "Ā" : "A", "Ă" : "A", "Ă" : "A",
        "Ç" : "C", "Ć" : "C", "Ĉ" : "C", "Ċ" : "C",
        "Ð" : "D", "Ď" : "D", "Đ" : "D",
        "È" : "E", "É" : "E", "Ê" : "E", "Ë" : "E", "Ē" : "E", "Ė" : "E", "Ę" : "E", "Ě" : "E",
        "Ĝ" : "G", "Ġ" : "G", "Ģ" : "G",
        "Ĥ" : "H", "Ħ" : "H",
        "Ì" : "I", "Í" : "I", "î" : "I", "ï" : "I", "į" : "I",
        "Ĵ" : "J",
        "Ķ" : "K",
        "Ļ" : "L", "Ł" : "L",
        "Ñ" : "N", "Ń" : "N", "Ņ" : "N", "Ň" : "N",
        "Ò" : "O", "Ó" : "O", "Ô" : "O", "Õ" : "O", "Ö" : "O", "Ő" : "O",
        "Ŕ" : "R", "Ř" : "R",
        "Ś" : "S", "Ŝ" : "S", "Ş" : "S", "Š" : "S", "Ș" : "S",
        "Ţ" : "T", "Ť" : "T", "Ț" : "T",
        "Ù" : "U", "Ú" : "U", "Û" : "U", "Ü" : "U", "Ū" : "U", "Ŭ" : "U", "Ů" : "U", "Ű" : "U", "Ų" : "U",
        "Ŵ" : "W",
        "Ý" : "Y", "Ŷ" : "Y", "Ÿ" : "Y",
        "Ź" : "Z", "Ż" : "Z", "Ž" : "Z",

        "à" : "a", "á" : "a", "â" : "a", "ã" : "a", "ä" : "a", "å" : "a", "ā" : "a", "ă" : "a", "ą" : "a",
        "ç" : "c", "ć" : "c", "ĉ" : "c", "ċ" : "c",
        "ď" : "d", "đ" : "d",
        "è" : "e", "é" : "e", "ê" : "e", "ë" : "e", "ē" : "e", "ė" : "e", "ę" : "e", "ě" : "e", "ə" : "e",
        "ĝ" : "g", "ġ" : "g", "ģ" : "g",
        "ĥ" : "h", "ħ" : "h",
        "ì" : "i", "í" : "i", "î" : "i", "ï" : "i", "ī" : "i", "į" : "i",
        "ĵ" : "j",
        "ķ" : "k",
        "ļ" : "l",
        "ñ" : "n", "ń" : "n", "ņ" : "n", "ň" : "n",
        "ò" : "o", "ó" : "o", "ô" : "o", "õ" : "o", "ö" : "o", "ő" : "o", "ŕ" : "r", "ř" : "r",
        "ś" : "s", "ŝ" : "s", "ş" : "s", "š" : "s", "ș" : "s",
        "ţ" : "t", "ť" : "t", "ț" : "t",
        "ù" : "u", "ú" : "u", "û" : "u", "ü" : "u", "ū" : "u", "ŭ" : "u", "ů" : "u", "ű" : "u", "ų" : "u",
        "ŵ" : "w",
        "ý" : "y", "ŷ" : "y", "ÿ" : "y",
        "ź" : "z", "ż" : "z", "ž" : "z",

        # 罗马数字Roman numerals
        "Ⅰ" : "I", "Ⅱ" : "II", "Ⅲ" : "III", "Ⅳ" : "IV", "Ⅴ" : "V", "Ⅵ" : "VI", "Ⅶ" : "VII",
        "Ⅷ" : "VIII", "Ⅸ" : "IX", "Ⅹ" : "X", "Ⅺ" : "XI", "Ⅻ" : "XII", "Ⅼ" : "L", "Ⅽ" : "C",
        "Ⅾ" : "D", "Ⅿ" : "M",
        "ⅰ" : "i", "ⅱ" : "ii", "ⅲ" : "iii", "ⅳ" : "iv", "ⅴ" : "v", "ⅵ" : "vi", "ⅶ" : "vii",
        "ⅷ" : "viii", "ⅸ" : "ix", "ⅹ" : "x", "ⅺ" : "xi", "ⅻ" : "xii", "ⅼ" : "l", "ⅽ" : "c",
        "ⅾ" : "d", "ⅿ" : "m",
    })


def extractWords(text):
    """抽出中文、英文、数字，忽略标点符号和特殊字符（表情）
    一般用与反垃圾
    """
    text = text.lower() # 词向量只计算小写
    # text = simplify(text) # 繁体转简体
    text = sbcCase(text) # 全角转半角
    text = circleCase(text) # 特殊字符
    text = bracketCase(text) # 特殊字符
    text = dotCase(text) # 特殊字符
    text = specialCase(text) # 特殊字符
    pattern = re.compile(r"[0-9A-Za-z\u4E00-\u9FFF]+")
    match = pattern.findall(text)
    if match:
        text = "".join(match)
    else:
        text = ""

    return text
