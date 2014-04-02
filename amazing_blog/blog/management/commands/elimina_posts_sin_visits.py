from django.core.management.base import BaseCommand
from blog.models import Post, Visits

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for post in Post.objects.all():
            if not post.visits_set.all():
                post.delete()
        pass
