import os

def install():
    package = 'BeautifulSo'
    try:
        if __import__(package):
            print "[*] Installation Finish"
    except ImportError:
        print "[*] Installing required module . . "
        return os.system('python -m pip install %s' % package)
install()