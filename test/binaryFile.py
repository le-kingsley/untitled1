"""
binary file
"""

def main():
    try:
        with open('D:\\1.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('D:\\企鹅.jpg', 'wb')as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('文件未找到！')
    except IOError as e:
        print('读写文件错误！')
    print('文件复制成功')

if __name__ == '__main__':
    main()