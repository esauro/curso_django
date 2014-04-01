from models import Visits, Post


class Statistics():

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__module__ == "blog.views" and view_func.__name__ == "PostDetail":
            visits_obj = Visits.objects.get_or_create(post=Post.objects.get(pk=view_kwargs['pk']))[0]
            visits_obj.visitas += 1
            visits_obj.save()
        return None

    def process_template_response(self, request, response):
        if response.template_name[0] == u"blog/post_detail.html":
            response.context_data['visits'] = Visits.objects.get(post = response.context_data['post'])
        return response
