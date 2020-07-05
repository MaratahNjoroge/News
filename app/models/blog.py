class Blog:
    '''
    Blog class that defines Blog Objects
    '''

    def __init__(self,id,title,name,author,description,publishedAt,content):
        self.id = id       
        self.title = title 
        self.name = name
        self.author = author 
        self.description = description 
        self.publishedAt = publishedAt
        self.content = content
        
        