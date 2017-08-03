import json, random, sys

d = dict(name='caren', salary=18000)
print(json.dumps(d), type(d))
print('\n')

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)
print(parsed_json['first_name'], type(parsed_json))

d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}
f = json.dumps(d)
print(f, type(f))
print(d, type(d))
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
            # print(p)
            return p


if __name__ == '__main__':
    main()
    # print(random.choice(main()),type(random.choice(main())))
    print(random.choice(main()))

print('\n')


def readip():
    pool = []
    pool2 = []
    with open('ip3.txt', 'r') as f:
        for i in f.readlines():
            lines = json.loads(i)
            line = lines['RESULT']
            for l in line:
                ip = ':'.join((l.get('ip'), l.get('port')))
                # print(l, type(l), l.get('ip'), l.get('port'))
                pool.append(l.get('ip'))
                pool2.append(ip)
            return pool2


if __name__ == '__main__':
    # readip()
    print(readip())
    print(random.choice(readip()), type(random.choice(readip())))

print('\n')

pool3 = []

# class MiddleWares(object):
# @classmethod
with open('ip3.txt', 'r') as f:
    for i in f.readlines():
        lines = json.loads(i)
        line = lines['RESULT']
        for l in line:
            ip = ':'.join((l.get('ip'), l.get('port')))
            # print(l, type(l), l.get('ip'), l.get('port'))
            # pool.append(l.get('ip'))
            pool3.append(ip)
print(random.choice(pool3))

print('\n')
with open('ip6.txt', 'r') as f:
    # for line in f.readlines():
    #     print(line.strip())
    lines = ['http://' + l.strip() for l in f.readlines()]
    print(lines)
print(random.choice(lines))