from django.core.management.base import BaseCommand
from blog.models import Post, Visits

class Command(BaseCommand):
    help = 'Elimina los posts sin contador de visitas'

    def handle(self, *args, **options):
        for post in Post.objects.all():
            if not post.visits_set.all():
                post.delete()