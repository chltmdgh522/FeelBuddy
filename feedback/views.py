from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Community, Comment, Like
from .forms import FeedbackForm, CommentForm

def feedback_list(request):
    feedbacks = Community.objects.all()
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})

def feedback_detail(request, pk):
    feedback = get_object_or_404(Community, pk=pk)
    comments = feedback.comment_set.all()
    is_liked = feedback.like_set.filter(user=request.user).exists()
    return render(request, 'feedback/feedback_detail.html', {
        'feedback': feedback,
        'comments': comments,
        'is_liked': is_liked,
        'comment_form': CommentForm()
    })

@login_required
def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback:feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

@login_required
def feedback_update(request, pk):
    feedback = get_object_or_404(Community, pk=pk)
    if request.user != feedback.user:
        return redirect('feedback:feedback_detail', pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback:feedback_detail', pk=pk)
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'feedback/feedback_form.html', {'form': form})

@login_required
def feedback_delete(request, pk):
    feedback = get_object_or_404(Community, pk=pk)
    if request.user == feedback.user:
        feedback.delete()
    return redirect('feedback:feedback_list')

@login_required
def comment_create(request, pk):
    feedback = get_object_or_404(Community, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.community = feedback
            comment.save()
    return redirect('feedback:feedback_detail', pk=pk)

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('feedback:feedback_detail', pk=comment.community.pk)

@login_required
def like_create(request, pk):
    feedback = get_object_or_404(Community, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, community=feedback)
    if not created:
        like.delete()
    return JsonResponse({'likes_count': feedback.like_set.count()})

@login_required
def like_delete(request, pk):
    feedback = get_object_or_404(Community, pk=pk)
    like = Like.objects.filter(user=request.user, community=feedback).first()
    if like:
        like.delete()
    return JsonResponse({'likes_count': feedback.like_set.count()})

