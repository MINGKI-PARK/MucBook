from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Tasty
from .forms import TastyCommentForm


def tastyList(request):
    tasty_list = Tasty.objects.all()
    context = {
        'tasty_list':tasty_list
    }
    return render(request, 'tasty/tasty_list.html', context)


def tastyDetail(request, tasty_id):
    tasty = get_object_or_404(Tasty, pk=tasty_id)

    tasty_comment_form = TastyCommentForm()
    tasty_comments = tasty.tastycomment_set.all()

    context = {
        'tasty':tasty,
        'form':tasty_comment_form,
        'comments':tasty_comments,
    }

    return render(request, 'tasty/tasty_detail.html', context)



# def commentCreate(request, photo_id):
#     '''
#     댓글 생성 뷰
#     '''

#     form = CommentForm(request.POST)
#     photo = get_object_or_404(Photo, pk=photo_id)

#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.author = request.user
#         comment.photo = photo
#         comment.save()
#         return redirect(reverse('photo:detail', args=(photo_id,)))
    
#     else: #validation 에러
#         # form = CommentForm()
#         comments = photo.comment_set.all()
#         context = {
#             'form':form,
#             'comments':comments,
#         }
#         return render(request, 'photo/detail.html', context)



def tastyCommentCreate(request, tasty_id):

    form = TastyCommentForm(request.POST)
    tasty = get_object_or_404(Tasty, pk=tasty_id)

    if form.is_valid():
        # print(request)

        comment = form.save(commit=False)
        comment.writer = request.user
        # comment.score = request.POST.get('score')
        comment.tasty = tasty
        comment.save()

        return redirect(reverse('tasty:tastydetail', args=[tasty.pk]))

    else:
        tasty_comments = tasty.tastycomment_set.all()
        context = {
            'form':form,
            'comments':tasty_comments,
            'tasty':tasty
        }
        return render(request, 'tasty/tasty_detail.html', context)