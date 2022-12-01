import time


class TreeStore:
    def __init__(self, items_in):
        self.items = {}
        for item in items_in:  # Перегоняем список словарей в словарь, где ключ - ИД объекта, а значение - сам объект, для прямого доступа к элементам дерева
            self.items[item['id']] = item

    def getAll(self):  # Получение всех элементов
        return list(self.items.values())

    def getItem(self, id: int):  # Получение элемента
        if id in self.items.keys():
            response = self.items[id]
        else:  # если элемента нет - возвращается None
            response = None
        return response

    def getChildren(self, id: int):  # Получение потомков элемента
        return list(filter(lambda item: item['parent'] == id, self.items.values()))

    def getAllParents(self, id: int):  # Получение всех предков элемента
        if id not in self.items.keys():  # Если нет такого ИД - возвращается пустой массив
            return []
        response = []
        child = self.items[id]
        response.append(child)
        while True:
            if child['parent'] == 'root':
                break
            parent = self.getItem(child['parent'])
            response.append(parent)
            child = parent
        return response


if __name__ == '__main__':
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
    start_time = time.time()
    ts = TreeStore(items)
    print(f'getAll(): {ts.getAll()}')
    print(f'getItem(): {ts.getItem(5)}')
    print(f'getChildren(): {ts.getChildren(2)}')
    print(f'getAllParents(): {ts.getAllParents(7)}')
    task_time = time.time() - start_time
    print(f'Total time: {task_time}')
