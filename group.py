from tag import Tag

class Group:
    def __init__(self, name, color):
        self.name = name
        self.tags = []
        self.color = color
    
    def addTag(self, data):
        self.tags.append(Tag(data))

    def changeColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def getTags(self):
        return self.tags
