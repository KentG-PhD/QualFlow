from tag import Tag

class CodeBook: 
    def __init__(self):
        self.codebook = {}
    
    def addGroup(self, group_name):
        self.codebook[group_name] = []

    def addTag(self, tag_data, group_name):
        self.codebook[group_name].append(Tag(tag_data))

    def getGroupInfo(self, group_name):
        return self.codebook[group_name]
    
    def getPlainTextGroupInfo(self, group_name):
        string_value = f"Group: {group_name}\n\nTags:\n"
        
        for index, tag in enumerate(self.codebook[group_name]):
            string_value += f"{index + 1}: {tag.data}\n"
        
        return string_value