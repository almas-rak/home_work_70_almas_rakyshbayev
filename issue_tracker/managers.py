from django.db.models import Manager


class CustomManager(Manager):

    def get_or_none(self, pk=None):
        try:
            return self.get_queryset().get(pk=pk, is_deleted=False)
        except self.model.DoesNotExist:
            return None

    def get_deleted(self):
        return self.get_queryset().filter(is_deleted=True)

    def all(self):
        return self.get_queryset().filter(is_deleted=False)


