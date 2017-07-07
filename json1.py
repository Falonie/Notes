import json,random

d=dict(name='caren',salary=18000)
print(json.dumps(d),type(d))
print('\n')

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json=json.loads(json_string)
print(parsed_json['first_name'],type(parsed_json))

d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}
f=json.dumps(d)
print(f,type(f))
print(d,type(d))
print('\n')

def main():
    p = []
    with open('ip2.txt', 'r') as f:
        # print(f.readlines()[0])
        # ipaddress = f.readlines()[0]
        # line = [i for i in f.readlines()]
        for i in f.readlines():
            lines = json.loads(i)
            # print(lines)
            # print(type(lines))
            for line in lines:
                print(line, type(line), line['ip'])
                p.append(line['ip'])
            print(p)
            return p

if __name__=='__main__':
    main()
    # print(random.choice(main()),type(random.choice(main())))
    print(random.choice(main()))

def readip():
    pool = []
    with open('ip.txt','r') as f:
        for i in f.readlines():
            lines = json.loads(i)
            line = lines['RESULT']
            for l in line:
                print(l, l.get('ip'), type(l))
                pool.append(l.get('ip'))
            return pool

if __name__=='__main__':
    readip()
    print(random.choice(readip()))
