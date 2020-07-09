from django.shortcuts import render, get_object_or_404, redirect

from .models import Photo, Comment
from .forms import PhotoForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from django.contrib.auth.decorators import login_required



def photoList(request):
    '''
    photo 목록 출력
    '''
    photos = Photo.objects.all()
    context = {
        'photos':photos
    }
    return  render(request, 'photo/list.html', context)


def photoDetail(request, photo_id):
    '''
    photo detail
    댓글 쓸 수 있게 할 예정
    '''
    photo = get_object_or_404(Photo, pk=photo_id)

    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)

    #     if comment_form.is_valid:
    #         comment = comment_form.save(commit=False)
    #         comment.author = request.user
    #         comment.photo = photo
    #         comment.save()
            
    comment_form = CommentForm()
    comments = photo.comment_set.all()

    context = {
        'photo':photo,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, 'photo/detail.html', context)

@login_required(login_url='accounts:login')
def photoUpload(request):
    
    '''
    포토 생성하는 뷰
    '''

    # GET부터 처리

    if request.method == 'GET':
        form = PhotoForm()

    # POST로 요청이 들어왔을 때
    else:
        # file 업로드 : request.FILES, 나머지: request.POST
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('photo:list'))
        
        else:
            form = PhotoForm(request.POST)



    context = {
        'form':form
    }
   
    return render(request, 'photo/upload.html', context)



@login_required(login_url='accounts:login')
def photoUpdate(request, photo_id):
    '''
    글 업데이트
    '''

    photo = Photo.objects.get(pk=photo_id)

    if request.user != photo.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('photo:detail', photo_id=photo.id)

    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES, instance=photo)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.save()
            return redirect('photo:detail', photo_id=photo.id)

    else:
        form = PhotoForm(instance=photo)
        context = {
            'form':form
        }
        return render(request, 'photo/update.html', context)


# 삭제에에에에
@login_required(login_url='accounts:login')
def photoDelete(request, photo_id):
    '''
    글 삭제
    '''
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user != photo.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('photo:detail', photo_id=photo.id)

    photo.delete()
    return redirect('photo:index')


@login_required(login_url='accounts:login')
def commentCreate(request, photo_id):
    '''
    댓글 생성 뷰
    '''

    form = CommentForm(request.POST)
    photo = get_object_or_404(Photo, pk=photo_id)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.photo = photo
        comment.save()
        return redirect(reverse('photo:detail', args=(photo_id,)))
    
    else: #validation 에러
        # form = CommentForm()
        comments = photo.comment_set.all()
        context = {
            'form':form,
            'comments':comments,
        }
        return render(request, 'photo/detail.html', context)


@login_required(login_url='accounts:login')
def commentUpdate(request, comment_id):
    '''
    댓글 수정
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    photo = get_object_or_404(Photo, pk=comment.photo.id)

    if request.user != comment.author:
        messages.warming(request, '권한 없음')
        return redirect('photo:detail', photo_id=photo.id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            form.save()
            return redirect('photo:detail', photo_id=photo.id)
    
    else:
        form = CommentForm(instance=comment)
    
    context = {
        'form':form
    }
    
    return render(request, 'photo/comment/comment_update.html', context)


@login_required(login_url='accounts:login')
def commentDelete(request, comment_id):
    '''
    댓글 삭제
    '''

    comment = get_object_or_404(Comment, pk=comment_id)
    photo = get_object_or_404(Photo, pk=comment.photo.id)

    if request.user != comment.author:
        messages.warning(request, '권한이 없습니다.')
        return redirect('photo:detail', photo_id=photo.id)

    if request.method == 'POST':
        comment.delete()
        return redirect('photo:detail', photo_id=photo.id)
    else:
        return render(request, 'photo/comment/comment_delete.html', {'comment':comment})
