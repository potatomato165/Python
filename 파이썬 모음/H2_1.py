s = "abcABCdEFaBCDeFAbCdEf"
a=s.lower()
print('"%s 문자열 : %d 인덱스, %d번 존재"' % ('abc',a.find('abc'),a.count('abc')))
print('"%s 문자열 : %d 인덱스, %d번 존재"' % ('def',a.rfind('def'),a.count('def')))
