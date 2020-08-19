"""
python中文件读写操作
通过内置open函数
"""
import tkinter
import tkinter.messagebox

def main():
    #设置标签
    flag = True
    #修改标签上的文字
    def change_label_text():
        #nonlocal表明当前变量是外部函数定义的变量
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, World!')\
            if flag else ('blue', 'Good, Bye!')
        label.config(text = msg, fg = color)

    #登出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出吗？'):
            top.quit()

    #读取文件，获取文本
    def read_file():
        f= None
        try:
            f = open('D:\\1.txt', 'r', encoding='GBK')
            temp = f.read()
        except FileNotFoundError:
            print('文件未找到！')
        except LookupError:
            print('指定了未知编码！')
        except UnicodeDecodeError:
            print('读取文件时解码错误！')
        f.close()
        return temp

    #gui界面
    top= tkinter.Tk()
    top.title('文本内容')
    top.geometry('400x300')
    label = tkinter.Label(top, text = read_file(), font = 'Arial -10', fg = 'red')
    label.pack(expand = 1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    top.mainloop()
if __name__ == '__main__':
    main()