from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from character.models import UserCharacter
from .models import Community, Comment, Like
from .forms import FeedbackForm, CommentForm
from .models import Review
from django.http import JsonResponse


@login_required
def feedback_list(request):
    feedbacks = Review.objects.all()  # 모든 리뷰 가져오기
    first_item = UserCharacter.objects.filter(user=request.user, trash=False).first()
    context = {
        'feedbacks': feedbacks,
        'first_item': first_item
    }
    return render(request, 'feedback/feedback_list.html', context)


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
    first_item = UserCharacter.objects.filter(user=request.user, trash=False).first()
    context = {
        'review': review,
        'first_item': first_item
    }
    return render(request, 'feedback/feedback_detail.html', context)

@login_required
def feedback_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.rate = request.POST.get('rate')
        review.message = request.POST.get('message')
        review.save()
        messages.success(request, '리뷰가 수정되었습니다.')
        return redirect('feedback:feedback_list')  # 리스트 페이지로 리다이렉트
    return render(request, 'feedback/feedback_edit.html', {'review': review})