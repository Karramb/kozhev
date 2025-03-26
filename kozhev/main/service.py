from django.db.models import Count


def filter_products(post_obj):
    return post_obj.filter(
        is_published=True, category__is_published=True
    )
