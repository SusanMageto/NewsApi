class Sources:
  '''
  class that defines Sources
  '''
  def __init__(self,id, name,desc, url, country):
      self.id = id
      self.name = name
      self.desc = desc
      self.url = url
      self.country = country
     
class Headlines:
  '''
  class that defines headlines
  '''
  def __init__(self,author,title,description,url,urlToImage,publishedAt):
     self.author = author
     self.title = title
     self.description = description
     self.url = url
     self.publishedAt = publishedAt
     self.urlToImage = urlToImage