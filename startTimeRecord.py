# -*- coding: utf-8 -*-
import datetime
import sys
import getpass

def record_current_datatime(path):
    d = datetime.datetime.now()
    f = open(path, 'a+')
    f.write(str(d) + " " + getpass.getuser() + '\n')
    f.close()

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    if argc > 1:
        record_current_datatime(argv[1])
    else:
        print 'No saving path.'
