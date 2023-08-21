from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
# Create your views here.

def create_post(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            caption = request.POST.get('caption')
            print(username)
            print(caption)
            post = Post.objects.create(username=username, caption= caption)
            return JsonResponse({'Message': 'Post created Successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
    
def get_post(request):
    if request.method == 'GET':
        try:
            posts = Post.objects.all()
            post_list = [{'id': post.id, 'username': post.username, 'caption': post.caption} for post in posts]
            return JsonResponse({'posts': post_list}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
        
def delete_post(request):
    if request.method == 'DELETE':
        try:
            id = request.GET.get('id')
            post = Post.objects.get(id=id)
            post.delete()
            return JsonResponse({'Message': 'Post deleted Successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)