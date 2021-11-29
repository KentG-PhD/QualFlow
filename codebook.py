from tag import Tag
from highlightColor import Color

class CodeBook: 
    def __init__(self):
        self.codebook = {}
        self.codebook['tag_colors_list'] = []
    
    def addGroup(self, group_name):
        self.codebook[group_name] = []
        dict_list = list(self.codebook)
        print(dict_list)
        for i, v in enumerate(self.codebook):
            print(i, v)

    def addTag(self, tag_data, group_name):
        self.codebook[group_name].append(Tag(tag_data))

    def getGroupInfo(self, group_name):
        return self.codebook[group_name]
    
    def getPlainTextGroupInfo(self, group_name):
        string_value = f"Group: {group_name}\n\nTags:\n"
        
        for index, tag in enumerate(self.codebook[group_name]):
            string_value += f"{index + 1}: {tag.data}\n"
        
        return string_value

    def getGroupNameIndex(self, group_name):
        string_value = self.codebook['group_name'].index(group_name)
        return string_value
    
    # def addTagColor(self, tag_color_list):
    #     self.codebook[tag_color_list] = []
        
    def setTagColor(self, tag_color):
        self.codebook['tag_colors_list'].append(Color(tag_color))
        print(self.codebook['tag_colors_list'])
        
        
    def getTagColors(self):
        return self.codebook['tag_colors_list']
        #print(self.codebook['tag_colors_list'])
        # for index, highlightColor in self.codebook['tag_colors_list']:
        #     color = {highlightColor.color}
        #     print(color)
        #     return(color)
