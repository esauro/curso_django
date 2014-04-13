
def page(request):
    context = {}
    if request.path==u"/":
        context['page'] = "list"
    if request.path.startswith(u"/post/"):
        context['page'] = "details"
    if request.path.endswith(u"/delete"):
        context['page'] = "delete"
    if request.path.endswith(u"/edit"):
        context['page'] = "form"
    if request.path.endswith(u"/create"):
        context['page'] = "empty"
    return context
