from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    args = 'post_id'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        if not len(args) or len(args) > 1:
            return None
        try:
            p = Post.objects.get(pk = args[0])
            v = p.visits_set.all()[0]
            v.visitas = 0
            v.save()
        except Post.DoesNotExist:
            return None
