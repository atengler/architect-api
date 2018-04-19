
from architect import utils
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.safestring import mark_safe


class Repository(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    engine = models.CharField(max_length=32, default='packer')
    metadata = JSONField(blank=True, null=True)
    cache = JSONField(blank=True, null=True)
    status = models.CharField(max_length=32, default='unknown')

    def client(self):
        client_class = utils.get_module(self.engine, 'repository')
        return client_class(**{
            'name': self.name,
            'engine': self.engine,
            'metadata': self.metadata})

    def class_list(self, resource=None):
        return self.client().class_list(resource=None)

    def resource_count(self, resource=None):
        return len(self.client().inventory(resource=None))

    def color(self):
        if self.status == 'active':
            return 'success'
        if self.status == 'error':
            return 'danger'
        if self.status == 'build':
            return 'info'
        else:
            return 'warning'

    def conn_detail(self):
        if self.metadata is None:
            return '-'
        elif self.engine in ['rpi23', 'bbb']:
            return mark_safe('Build: {}<br>Manager/Inventory: {}/{}'.format(self.metadata.get('builder_dir', '-'),
            self.metadata.get('manager', '-'), self.metadata.get('inventory', '-')))
        else:
            return '-'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Repositories"
        ordering = ['name']


class Resource(models.Model):
    uid = models.CharField(max_length=511)
    name = models.CharField(max_length=511)
    repository = models.ForeignKey(Repository,
                                  on_delete=models.CASCADE,
                                  related_name='images')
    kind = models.CharField(max_length=32)
    size = models.IntegerField(default=0)
    metadata = JSONField(blank=True, null=True)
    cache = JSONField(blank=True, null=True)
    status = models.CharField(max_length=32, default='unknown')

    def __str__(self):
        return '{} {}'.format(self.kind, self.name)

    def color(self):
        if self.status == 'active':
            return 'success'
        if self.status == 'error':
            return 'danger'
        if self.status == 'build':
            return 'info'
        else:
            return 'warning'

    class Meta:
        ordering = ['-id']
