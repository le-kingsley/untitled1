"""
Title:刷弹幕
Author:kingsley
Version:0.1
Question:在各大直播平台刷弹幕
"""
import danmu

def get_keyword():
    keyword = input()
    return keyword

if __name__ == '__main__':
    
    doc = docx.Document('D:\\预案.doc')
    pars = doc.paragraphs
    key = get_keyword()
    for par in pars:
        str = par.text
        if key in str:
            print('a')

