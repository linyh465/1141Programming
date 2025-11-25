MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

import sys

line = sys.stdin.readline()
if not line:
    print('')
    sys.exit(0)

line = line.rstrip('\n')

# 以空白分詞為單字（多個空白視為單字分隔）
words = line.split()
out_words = []
for w in words:
    codes = []
    for ch in w:
        key = ch.upper()
        if key in MORSE_CODE_DICT:
            codes.append(MORSE_CODE_DICT[key])
        # 不在字典中的符號直接忽略
    out_words.append(' '.join(codes))

print(' / '.join(out_words))
