import redis
import sys

def insert(r,key,value):
    pass
    r.set(key,value)

def transform(r):
    pass
    value, _type = None, None
    key_list = r.keys()

    for key in key_list:
        _type = r.type(key)
        if _type=='string':
            value = r.get(key)
            r.sadd('UNION',(key,value))

def test(r):
    pass
    value, _type = None, None
    _sep = ';'
    key_list = r.keys()

    for key in key_list:
        _type = r.type(key)
        if _type=='string': value = r.get(key)
        elif _type=='set': value = r.smembers(key)
        print 'KEY:',key,_sep,'TYPE',_type,_sep,'VALUE',value


if __name__ == '__main__' :
    pass
    arg_list = sys.argv
    r = redis.StrictRedis(host='localhost', port=30001)

    if len(arg_list)==1:
            print 'python main.py MODE [Key] [Value]'
            print 'MODE:1 Insert Key & Value'
            print 'MODE:2 Transform all String into Set'
            print 'MODE:3 Output all Keys\' value'
    else:
        if arg_list[1]=='1': insert(r,arg_list[2],arg_list[3])
        elif arg_list[1]=='2': transform(r)
        elif arg_list[1]=='3': test(r)
