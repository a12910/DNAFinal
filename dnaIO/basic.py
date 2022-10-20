import time

class LOG:
    @staticmethod
    def Basic(key, value):
        print("[%s] [%s] %s" % (time.strftime("%H:%M:%S", time.localtime()), key.ljust(10), value))
