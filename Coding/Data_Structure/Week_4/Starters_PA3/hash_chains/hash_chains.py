# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            #print(c,s)
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        print(self.elems)
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if query.ind in self.elems:
                self.write_chain(cur for cur in reversed(self.elems[query.ind]))
            else:
                self.write_chain(' ')
                        #if self._hash_func(cur) == query.ind)
        else:
            hash_integer = self._hash_func(query.s)
            if hash_integer in self.elems:
                if query.type == 'find':
                    self.write_search_result(query.s in self.elems[hash_integer])
                elif query.type == 'add':
                    if query.s not in self.elems[hash_integer]:
                        self.elems[hash_integer].append(query.s)
                else:
                    if query.s in self.elems[hash_integer]:
                        self.elems[hash_integer].remove(query.s)
            if hash_integer not in self.elems:
                if query.type == 'find':
                    self.write_search_result(0)
                elif query.type == 'add':
                    self.elems[hash_integer] = [query.s]
                
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
    print(proc._hash_func("world"))
