from socket import *
import threading
lock = threading.Lock() # 加锁避免多个线程对一个变量同时进行操作，产生错误
Num = 0
threads = []  # 定义线程列表
def portscanner(host,port):
    global Num
    try:
        s = socket(AF_INET,SOCK_STREAM) # 创建套接字
        s.connect((host,port)) # 初始化TCP连接
        lock.acquire() # 获取锁
        Num += 1 # 修改变量
        print('[+] %d 端口开启' % port)
        lock.release() # 释放锁
        s.close()
    except:
        print('[-] %d 端口关闭' % port)

def main():
    setdefaulttimeout(1)
    '''
    ports = [25，40，496，886，1024，65535]  #定义要扫描的端口
    for i in ports:
        t = threading.Thread(target=portScanner, args=('192.168.0.100, i))
        threads.append(t)
        t.start()
    '''
    for i in range(1,1000):
        t = threading.Thread(target=portscanner,args=('220.181.38.148',i))  # 创建线程
        threads.append(t)  # 开始
        t.start()

    for t in threads:  # 等待线程列表中的所有线程执行完毕
        t.join()
    print('------End------')
    print('[*] 总共有 %d 个开启的端口' % (Num))

main()