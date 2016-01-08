from sys import stdin

if __name__ == '__main__':
    trie = {}
    leaf = "leaf"

    def insert(string):
        root = trie
        for ch in list(string):
            root = root.setdefault(ch, {})

        root[leaf] = True


    def query(string):
        root = trie
        b = False
        for ch in list(string):
            if ch in root:
                root = root[ch]
            else:
                b = True
                break
        return (b, root)

    n = int(stdin.readline())

    ans, record = True, ""

    for _ in range(n):
        ss = stdin.readline().strip()
        b, rr = query(ss)
        if "leaf" in rr or b == False:
            if ans: record = ss
            ans = False
            break   # failure earlier to avoid segment fault(memory usage)
        insert(ss)

    if ans:
        print("GOOD SET")
    else:
        print("BAD SET")
        print(record)


