from elasticsearch_dsl import Document, Text, Index

todoIndex = Index('todo')


@todoIndex.document
class TodoESModel(Document):
    todo = Text()


def init():
    todoIndex.delete(ignore=404)

    todoIndex.settings(number_of_shards=1)
    todoIndex.create()


def index_todo(data):
    TodoESModel(meta={'id': data.get('id')}, todo=data.get('todo')).save()

    # refresh index manually to make changes live
    todoIndex.refresh()
