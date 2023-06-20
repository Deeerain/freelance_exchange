from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


from tasks import models


@registry.register_document
class CategoryDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'categories'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = models.Category
        fields = [
            'name'
        ]


@registry.register_document
class TaskDocument(Document):
    employer = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })

    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })

    class Index:
        name = 'tasks'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = models.Task
        fields = [
            'id',
            'title',
            'description',
            'visible',
            'created',
            'updated'
        ]
