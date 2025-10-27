from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def post_list(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 10))

    posts = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts, page_size)
    page_obj = paginator.get_page(page)

    serializer = PostSerializer(page_obj, many=True)
    return Response({
        'posts': serializer.data,
        'page': page,
        'total_pages': paginator.num_pages,
        'total_posts': paginator.count
    })
