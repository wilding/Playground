uni1 = unicode('abcdefgaa hello')

print uni1
print type(uni1)
print '\n'

# uni2 = unicode('abcdefg' + chr(255))
# print uni2
# >> UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 7: ordinal not in range(128)

# uni3 = unicode('\x80abc', errors='strict')
# print uni3
# >> UnicodeDecodeError: 'ascii' codec can't decode byte 0x80 in position 0: ordinal not in range(128)

uni4 = unicode('\x80abc', errors='replace')
uni5 = unicode('\x80abc', errors='ignore')
print uni4
print uni5
print '\n'

print unichr(255)
print ord('\x80')
print '\n'

print uni1.count('a')
print uni1.find('hello')  # argument can be string or unicode
print uni1.replace('hello', 'goodbye')  # uses ascii encoding
print uni1.upper()
print '\n'

uni6 = unichr(40690) + uni1 + unichr(1972)
print type(uni6)
uni7 = uni6.encode('utf-8')
print uni7
print type(uni7)
# print uni6.encode('ascii', 'strict')     Unicode error
print uni6.encode('ascii', 'replace')
print uni6.encode('ascii', 'ignore')
print uni6.encode('ascii', 'xmlcharrefreplace')
print uni7.decode('utf-8')
print type(uni7.decode('utf-8'))
print '\n'
