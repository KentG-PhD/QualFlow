from tag import Tag
from highlightColor import Color
from group import Group

COLORS = ['aliceblue', 'antiquewhite','aquamarine','azure','beige','lavender'] 	

class CodeBook: 
    def __init__(self):
        self.codebook = {}
        #self.codebook['tag_colors_list'] = []
    """
    {
        #group_name: array of tags
        group_name: Group Object
    }
    """
    def addGroup(self, group_name):
        #index % length
        group_length = len(self.codebook)
        full_length = len(COLORS)
        index = group_length % full_length
        current_color = COLORS[index]

        self.codebook[group_name] = Group(group_name, current_color)
    
        #dict_list = list(self.codebook)
        #print(dict_list)
        #for i, v in enumerate(self.codebook):
        #    print(i, v)

    def addTag(self, tag_data, group_name):
        self.codebook[group_name].addTag(tag_data)

    def getGroupInfo(self, group_name):
        return self.codebook[group_name].getTags()
    

    def getPlainTextGroupInfo(self, group_name):
        string_value = f"Group: {group_name}\n\nTags:\n"
        
        for index, tag in enumerate(self.codebook[group_name].getTags()):
            string_value += f"{index + 1}: {tag.data}\n"
        
        return string_value
    
    def getColor(self, group_name):
        group_object = self.codebook[group_name]
        color = group_object.getColor()
        return color

    def saveProject(self):
        info = {}
        """
        {
            group_name: {
                color: string
                name: string
                tags: []
            }
        }
        """
        for group_name, group_object in self.codebook.items():
            group_info = {}
            group_info["name"] = group_object.getName()
            group_info["tags"] = group_object.getTags()
            group_info["color"] = group_object.getColor()
            info[group_name] = group_info

        return info
"""
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
"""