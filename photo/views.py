from django.shortcuts import render, get_object_or_404, redirect

from .models import Photo
from .forms import PhotoForm
from django.urls import reverse
from django.contrib import messages





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
    context = {
        'photo':photo
    }
    return render(request, 'photo/detail.html', context)


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




def photoUpdate(request, photo_id):
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

def photoDelete(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user != photo.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('photo:detail', photo_id=photo.id)

    photo.delete()
    return redirect('photo:index')