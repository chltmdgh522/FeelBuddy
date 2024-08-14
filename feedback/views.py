from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Community, Comment, Like
from .forms import FeedbackForm, CommentForm
from .models import Review
from django.http import JsonResponse

@login_required
def feedback_list(request):
    feedbacks = Review.objects.all()  # 모든 리뷰 가져오기
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})

@login_required
def feedback_create(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        rate = request.POST.get('rate')
        if message and rate:
            Review.objects.create(
                user=request.user,
                message=message,
                rate=rate
            )
    return redirect('feedback:feedback_list')

@login_required
def feedback_delete(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    review.delete()
    return redirect('feedback:feedback_list')

@login_required
def feedback_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'feedback/feedback_detail.html', {'review': review})
# def feedback_list(request):
#     feedbacks = Community.objects.all()
#     return render(request, 'feedback/feedback1.html', {'feedbacks': feedbacks})

# def feedback_detail(request, pk):
#     feedback = get_object_or_404(Community, pk=pk)
#     comments = feedback.comment_set.all()
#     is_liked = feedback.like_set.filter(user=request.user).exists()
#     return render(request, 'feedback/feedback_detail.html', {
#         'feedback': feedback,
#         'comments': comments,
#         'is_liked': is_liked,
#         'comment_form': CommentForm()
#     })

# @login_required
# def feedback_create(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         img_url = request.FILES.get('img_url')  

#         if title and content:
#             feedback = Community.objects.create(
#                 title=title,
#                 content=content,
#                 user=request.user,
#                 img_url=img_url  
#             )
#             return redirect('feedback:feedback_list')
#     return render(request, 'feedback/feedback_form.html')

# @login_required
# def feedback_update(request, pk):
#     feedback = get_object_or_404(Community, pk=pk)
#     if request.user != feedback.user:
#         return redirect('feedback:feedback_detail', pk=pk)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feedback)
#         if form.is_valid():
#             form.save()
#             return redirect('feedback:feedback_detail', pk=pk)
#     else:
#         form = FeedbackForm(instance=feedback)
#     return render(request, 'feedback/feedback_form.html', {'form': form})

# @login_required
# def feedback_delete(request, pk):
#     feedback = get_object_or_404(Community, pk=pk)
#     if request.user == feedback.user:
#         feedback.delete()
#     return redirect('feedback:feedback_list')

# @login_required
# def comment_create(request, pk):
#     community = get_object_or_404(Community, pk=pk)  
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         if content:
#             Comment.objects.create(
#                 community=community,  
#                 user=request.user,
#                 content=content
#             )
#     return redirect('feedback:feedback_detail', pk=pk)

# @login_required
# def comment_delete(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     if request.user == comment.user:
#         comment.delete()
#     return redirect('feedback:feedback_detail', pk=comment.community.pk)

# @login_required
# def like_create(request, pk):
#     feedback = get_object_or_404(Community, pk=pk)
#     like, created = Like.objects.get_or_create(user=request.user, community=feedback)
#     if not created:
#         like.delete()
#     return JsonResponse({'likes_count': feedback.like_set.count()})

# @login_required
# def like_delete(request, pk):
#     feedback = get_object_or_404(Community, pk=pk)
#     like = Like.objects.filter(user=request.user, community=feedback).first()
#     if like:
#         like.delete()
#     return JsonResponse({'likes_count': feedback.like_set.count()})

