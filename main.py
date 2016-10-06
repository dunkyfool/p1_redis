import redis
import pprint as pp
import sys

def insert(r,key,value):
    '''
    insert (key,value) as string into redis
    input:
        r: redis connection
        key, value: input parameter
    '''
    r.set(key,value)

def transform(r):
    '''
    transform all string(s) into set(UNION, (key,value))
    input:
        r:redis connction
    '''
    value, _type = None, None
    key_list = r.keys()

    for key in key_list:
        _type = r.type(key)
        if _type=='string':
            value = r.get(key)
            r.sadd('UNION',(key,value))

def print_str_set(r):
    '''
    output all key(s), its type & value
    input:
        r:redis connction
    '''
    value, _type = None, None
    _sep = ';'
    key_list = r.keys()

    for key in key_list:
        _type = r.type(key)
        if _type=='string': value = r.get(key)
        elif _type=='set': value = r.smembers(key)
        print 'KEY:',key,_sep,'TYPE',_type,_sep,'VALUE',value

def mod_config(r):
    '''
    change config on the fly & rewrite redis.conf
    input:
        r:redis connction
    '''
    # LOG
    print r.config_get('loglevel')
    print r.config_get('logfile')
    print r.config_get('slowlog-log-slower-than')
    print r.config_get('slowlog-max-len')

    # RDB
    print r.config_get('save')
    print r.config_get('stop-writes-on-bgsave-error')
    print r.config_get('rdbcompression')
    print r.config_get('dbfilename')
    print r.config_get('dir')

    # AOF
    print r.config_get('appendonly')
    print r.config_get('appendfilename')
    print r.config_get('appendfsync')
    print r.config_get('no-appendfsync-on-rewrite')
    print r.config_get('auto-aof-rewrite-percentage')
    print r.config_get('auto-aof-rewrite-min-size')

    # LIMITATION
    #maxclients 128
    print r.config_get('maxmemory')

    # EXPIRATION
    print r.config_get('maxmemory-policy')
    print r.config_get('maxmemory-samples')

    # SECURITY
    #requirepass foobared

    # TRIVAL
    print r.config_get('vm.overcommit_memory')

    #r.config_set('appendonly','no')
    #print r.config_get('appendonly')

def show_info(r):
    '''
    output redis current status
    input:
        r:redis connction
    '''
    pp.pprint(r.info())

if __name__ == '__main__' :
    pass
    arg_list = sys.argv
    r = redis.StrictRedis(host='localhost', port=30001)

    if len(arg_list)==1:
            print 'python main.py MODE [Key] [Value]'
            print 'MODE:1 Insert Key & Value'
            print 'MODE:2 Transform all String into Set'
            print 'MODE:3 Output all Keys\' value'
            print 'MODE:4 Change config'
            print 'MODE:5 Output INFO'
    else:
        if arg_list[1]=='1': insert(r,arg_list[2],arg_list[3])
        elif arg_list[1]=='2': transform(r)
        elif arg_list[1]=='3': print_str_set(r)
        elif arg_list[1]=='4': mod_config(r)
        elif arg_list[1]=='5': show_info(r)
