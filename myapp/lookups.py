from django.core.exceptions import PermissionDenied
from ajax_select import register, LookupChannel
from .models import Tag

# @register('tags')
# class TagsLookup(LookupChannel):
#     model = Tag
#     forward = ['category','user_id']

#     def check_auth(self, request):
#         return True

#     def get_query(self, q, request):
#         qs = self.model.objects.all()
#         category = request.GET.get('category')
#         user_id  = request.GET.get('user_id')
#         if category:
#             qs = qs.filter(category_id=category)
#         if user_id:
#             qs = qs.filter(created_by_id=user_id)
#         return qs.filter(name__icontains=q).order_by('name')[:50]

#     def format_item_display(self, item):
#         return f"<span class='tag'>{item.name}</span>"

@register('tags')
class TagsLookup(LookupChannel):
    model = Tag

    def check_auth(self, request):
        return True

    def get_query(self, q, request):
        category = request.GET.get('category')
        user_id  = request.GET.get('user_id')
        ad_id    = request.GET.get('ad_id')
        ad_type  = request.GET.get('ad_type')

        print("🚀 term:", q)
        print("📦 all params:", dict(request.GET))

        qs = self.model.objects.all()

        if category:
            qs = qs.filter(category__name=category)
        if user_id:
            qs = qs.filter(created_by_id=user_id)
        if ad_id:
            qs = qs.filter(ad_id=ad_id)
        if ad_type:
            qs = qs.filter(ad_type=ad_type)

        return qs.filter(name__icontains=q).order_by("name")[:20]


    def format_item_display(self, item):
        return item.name