import os
import time

def checksum(copy_rdb):
    '''
    Check copy_rdb is corrpted or not
    output:
        1: Pass
        0: Fail
    *Condition is not ready
    '''
    #cmd='redis-check-rdb ' + copy.rdb
    #tmp = os.popen(cmd).read()
    #if tmp=='ok': return 1
    #else: return 0

def copy(dump_rdb):
    '''
    Copy dump_rdb as YYMMDDHHMM.bak.rdb
    output:
        <string> copy file's name
    '''
    copy_name = str(time())+'.bak'
    cmd='cp '+dump_rdb+copy_name
    os.system(cmd)
    return copy_name

def delete(copy_name):
    '''
    Delete file
    '''
    cmd='rm '+copy_name
    os.system(cmd)

def find_latest():
    '''
    Find latest copy file
    output:
        copy_name
    '''
    pass

def compare(dump_rdb,latest_rdb):
    '''
    Compare dump_rdb amd latest_rdb
    output
        1: Different
        0: Identical
    '''
    pass

def copy_check_loop(dump_rdb):
    '''
    Copy dump_rdb and check whether it is corrupted
    '''
    while(1):
        copy_name = copy(dump_rdb)
        if checksum(copy_name):
            break
        else:
            delete(copy_name)

def find_latest():
    '''
    Find out last created copy_rdb
    output:
        copy_name
    '''
    from os import listdir
    from os.path import join, getctime
    path=''
    entries=[(getctime(join(path,f)),join(path,f)) for f in listdir(path)]
    return sorted(entris)[-1][1]

def backup():
    ############################################
    # check dump_rdb and copy_rdb exist or not #
    ############################################
    if dump_rdb not exist:
        return 0
    else:
        if .bak not exist:
            copy_check_loop(dump_rdb)

    ###########################################
    # Compare dump_rdb and latest_rdb         #
    ###########################################
    if compare(dump_rdb,find_latest()):
        copy_check_loop(dump_rdb)

    return 0


def test():
    pass
    #checksum('123')

if __name__=='__main__':
    test()
    #while(1):
    #    backup()
    #    sleep(1)

