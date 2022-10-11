class TreeStore:
    def __init__(self, arr):
        self.arr = arr

    # Возвращает изначальный массив элементов
    def getAll(self):
        return (self.arr)

    # Возвращает сам объект элемента
    def getItem(self, id):
        for item in self.arr:
            if item["id"] == id:
                return item

    # Возвращает массив элементов, являющихся дочерними для того элемента
    def getChildren(self, id):
        children = []

        for item in self.arr:
            if item["parent"] == id:
                children.append(item)

        return children

    # Возвращает массив из цепочки родительских элементов
    def getAllParents(self, id):
        parents = []

        def getParents(id, i = False):
            for item in self.arr:
                if item["id"] == id:
                    if i:
                        parents.append(item)
                    i = True
                    getParents(item["parent"], i)

        getParents(id)

        return parents

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)


