class Node:
    def __init__(self):
        self.subfile = dict()
        self.subdir = dict()
        self.isFile = False
        self.isDir = False
        self.content = None

class FileSystem:

    def __init__(self):
        self.root = Node()
        self.root.isDir = True

    def ls(self, path: str) -> List[str]:
        node = self.root
        pathList = self.pathToPathlist(path)
        for path in pathList[:-1]:
            node = node.subdir[path]
        if pathList[-1] in node.subfile:
            return [pathList[-1]]
        if pathList[-1] in node.subdir:
            node = node.subdir[pathList[-1]]
        return sorted(list(node.subfile.keys()) + list(node.subdir.keys()))

    def mkdir(self, path: str) -> None:
        node = self.root
        pathList = self.pathToPathlist(path)
        for path in pathList:
            if path not in node.subdir:
                tmp = Node()
                tmp.isDir = True
                node.subdir[path] = tmp
            node = node.subdir[path]        

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        pathList = self.pathToPathlist(filePath)
        for path in pathList[:-1]:
            node = node.subdir[path]
        if pathList[-1] not in node.subfile:
            tmp = Node()
            tmp.content = content
            tmp.isFile = True
            node.subfile[pathList[-1]] = tmp
        else:
            node = node.subfile[pathList[-1]]
            node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        pathList = self.pathToPathlist(filePath)
        for path in pathList[:-1]:
            node = node.subdir[path]
        node = node.subfile[pathList[-1]]
        return node.content
        
    def pathToPathlist(self, path):
        if path and path[0] == "/":
            path = path[1:]
        if path and path[-1] == "/":
            path = path[:-1]
        return path.split("/")

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
