"""
国调语料处理

"""
import docx
import codecs
import string

doc = docx.Document('D:\\预案.docx')
i = 1
s = ''
# 去XX
for par in doc.paragraphs:
    if 'XX' not in par.text:
        if par.text not in '':
            tmp = par.text + ';'
            s = '%s%s' % (s, tmp)
        if par.text in '':
            if s != '':
                path = 'D:\\sent%d.txt' % i
                file = codecs.open(path, 'w', encoding='UTF-8')
                s = s[:-1]
                print(s)
                file.write(''+s)
                s = ''
                i = i + 1
                file.close()


