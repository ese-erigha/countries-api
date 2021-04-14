from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, Index

index = Index('todo')

@index.document
class TodoESModel(Document):
    todo = Text()


def init():
  
  if index.exists() is True:
    index.delete()

  index.settings(number_of_shards=1)
  index.create()



def index_todo(data):
    TodoESModel(meta={'id':data.get('id')}, todo = data.get('todo')).save()
    
    # refresh index manually to make changes live
    index.refresh()
