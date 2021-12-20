from typing import List


class Cave:
    def __init__(self, name: str, connection: List[str]):
        self.name = name
        self.connection = connection
        self.type = None
        self._connect_to_ends()
        self.connection_repr = []

    def __str__(self):
        return f'Cave name: {self.name}, Type: {self.type}, Connection: {self.connection}'

    # def __repr__(self):
    #     return f'Cave name: {self.name}, Type: {self.type}, Connection: {self.connection_repr},' \
    #            f' S/E: {self.start_connection}/{self.end_connection}'

    def add_connection(self, connection) -> None:
        self.connection_repr.append(connection)

    def _connect_to_ends(self) -> None:
        if "start" in self.connection:
            self.start_connection = True
        else:
            self.start_connection = False
        if "end" in self.connection:
            self.end_connection = True
        else:
            self.end_connection = False


class BigCave(Cave):
    def __init__(self, name: str, connection: List[str]):
        super().__init__(name, connection)
        self.type = "Big"

    def create_connections(self, starting):
        for conn in self.connection_repr:
            temp = starting
            print(1)
            print(temp + "-" + self.name + '-' + conn.name)
            temp += "-" + self.name + '-' + conn.name
            conn.create_temp_connections(temp)

    def create_temp_connections(self, starting):
        for conn in self.connection_repr:
            temp = starting
            print(temp + '-' + conn.name)
            temp += '-' + conn.name
            conn.create_temp_connections(temp)

class SmallCave(Cave):
    def __init__(self, name: str, connection: List[str]):
        super().__init__(name, connection)
        self.type = "small"
        self.visited = False

    def create_connections(self, starting):
        for conn in self.connection_repr:
            if self.visited:
                return None
            temp = starting
            print(temp + "-" + self.name + '-' + conn.name)
        self.visited = True

    def create_temp_connections(self, starting):
        for conn in self.connection_repr:
            if self.visited:
                return None
            temp = starting
            print(temp + '-' + conn.name)
        self.visited = True
        conn.create_temp_connections(temp)

def load_data() -> List[str]:
    with open('test_input.txt', 'r') as file:
        data = [line.strip() for line in file]
    return data


def create_cave_system(data: List[str]) -> List[Cave]:
    caves = set()
    list_of_caves = []
    connections_dict = {}
    for connection in data:
        connection = connection.split("-")
        if connection[0] != "start" and connection[0] != "end":
            caves.add(connection[0])
        if connection[1] != "start" and connection[1] != "end":
            caves.add(connection[1])
    for connection in data:
        conn = connection.split("-")
        if conn[0] not in connections_dict:
            connections_dict[conn[0]] = [conn[1]]
        else:
            connections_dict[conn[0]].append(conn[1])
        if conn[1] not in connections_dict:
            connections_dict[conn[1]] = [conn[0]]
        else:
            connections_dict[conn[1]].append(conn[0])
    # print(connections_dict)
    for name in caves:
        if name.isupper():
            list_of_caves.append(BigCave(name, connections_dict[name]))
        else:
            list_of_caves.append(SmallCave(name, connections_dict[name]))
    # [print(cave) for cave in list_of_caves]
    print("")
    for cave in list_of_caves:
        for conn in list_of_caves:
            if conn.name in cave.connection:
                cave.add_connection(conn)
            else:
                continue
    [print(cave) for cave in list_of_caves]

    return list_of_caves


def main() -> None:
    data = load_data()
    system = create_cave_system(data)
    for obj in system:
        if obj.type == "Big":
            obj.create_connections("start")
    pass


if __name__ == '__main__':
    main()
