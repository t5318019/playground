import os
import urllib.parse


def main():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    md_file = os.path.join(this_dir, '../docs/Big5.md')
    md_file = os.path.normpath(md_file)

    f = open(md_file, 'w', encoding="utf-8")
    print('# Big5\n', file=f)

    write_table(f, '符號', 'a140', 'a3bf', False)
    write_table(f, '常用漢字', 'a440', 'c67e', True)
    write_table(f, '次常用漢字', 'c940', 'f9d5', True)

    f.close()


def write_table(f, title, start, end, moedict):
    print('## %s\n' % title, file=f)

    header = ['\u3000', ]
    for i in range(16):
        header.append(i.to_bytes(1, 'big').hex()[1])
    print('|', '| '.join(header), '|', sep='', file=f)
    print('|--'*17, '| ', sep='', file=f)

    c = int.from_bytes(bytes.fromhex(start), 'big')
    s = []
    while c <= int.from_bytes(bytes.fromhex(end), 'big'):
        try:
            character = c.to_bytes(2, 'big').decode('big5')
            if(moedict):
                character = '[%s](https://www.moedict.tw/%s)' % (
                    character,
                    urllib.parse.quote(character)
                )
        except:
            character = '\u3000'
        s.append(character)
        if (len(s) == 16):
            start = (c-15).to_bytes(2, 'big').hex()
            print('|', start, '|', '|'.join(s), '|', sep='', file=f)
            s = []
        c = c + 1
    start = (c-15).to_bytes(2, 'big').hex()
    if(len(s) < 16):
        padding = ['\u3000']*(16-len(s))
        s.extend(padding)
    print('|', start, '|', '|'.join(s), '|', sep='', file=f)
    print('', sep='', file=f)


if __name__ == "__main__":
    main()
