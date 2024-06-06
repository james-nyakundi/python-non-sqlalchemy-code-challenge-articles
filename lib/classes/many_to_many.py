class Article:
  all=[]
def __init__(self, author, magazine, title):
        if type(title) !=str or (len(title)>=5 and len (title)<=50)==False:
               raise ValueError("Title must be a string between 5 and 50 characters long.")
        
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

@property
def title(self):
     return self._title

@title.setter
def title(self,value):
         raise AttributeError("Title name cannot be changed.")
        
        
class Author:
    def __init__(self, name):
        if type(name) !=str or len(name) < 1:
             raise ValueError("Name must be a string with atleast one character.")
        self._name = name
@property
def name(self):
     return self._name
@name.setter
def name(self,value):
         raise AttributeError("Author name cannot be changed.")
def articles(self):  
         x = []
         for article in Article.all:
              if article.author==self:
               x.append(article)  
              return x      
         pass
def magazines(self):
        x = list(set([article.magazine for article in self.articles()]))
        return x
        pass

def add_article(self, magazine, title):
        return(Article(self,magazine,title))
        pass

def topic_areas(self):
        x =list(set([ Magazine.category for magazine in self.magazines()]))
        return x  if x else None
        pass

class Magazine:
    all = []
    def __init__(self, name, category):
        if type(name) !=str or not (len(name)>=2 and len(name)<=16):
             raise ValueError("Name must be a string with  at least 2-16 characters")
        self.name = name
        self.category = category
        Magazine.all.append(self)

        @property
        def name (self):
             return self.name 
        
        @name.setter
        def name (self,value):
             if type(value) !=str or not (len(value)>=2 and len(value)<=16):
              raise ValueError("Name must be a string with  at least 2-16 characters.")
             self._name=value 

        @property
        def category (self):
             return self.category
        
        @category.setter
        def category (self,value):
             if type(value) !=str or not (len(value)>=0 ):
              raise ValueError("Name must be a string with  at least 2-16 characters.")
             self._category=value 


    def articles(self):
        x = []
        for article in Article.all:
             if article.magazine == self:
                  x.append(article)
                  return x
        pass

    def contributors(self):
        x =[]
        for article in self.articles():
             x.append(article.author)
             return list (set(x))
        pass

    def article_titles(self):
        titles = [Article.title for article in self.articles()]
        return titles if titles else None
        pass

    def contributing_authors(self):
        authors=[author for author in self.contributors() if len([article for article in self.articles()if article.author==author])]
        return authors if authors else None
        pass
    