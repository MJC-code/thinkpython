class Kangaroo:
    def __init__(self):
        self.pouch_contents = []
        
    def put_in_pouch(self, object):
        self.pouch_contents.append(object)

    def __str__(self):
        result = []
        for item in self.pouch_contents:
            result.append(item)
            
        return str(result)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('apple')
kanga.put_in_pouch('pineapple')
roo.put_in_pouch('banana')
kanga.put_in_pouch(roo)
#kanga.put_in_pouch(roo)
print('Kanga contents:', kanga)
print('Roo contents:', roo)
