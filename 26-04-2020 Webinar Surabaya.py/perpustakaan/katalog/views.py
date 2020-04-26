from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Buku

# Create your views here.
def index(request):
    data_buku = Buku.objects.all()
    return render(request, 'katalog/index.html', {'data_buku': data_buku})

def create(request):
    if request.method == 'POST':
        try:
            Buku(
                judul = request.POST['judul'],
                pengarang = request.POST['pengarang'],
                penerbit = request.POST['penerbit'],
                tahun = request.POST['tahun'] 
            ).save()
            messages.add_message(request, messages.SUCCESS, 'berhasil menambahkan buku')
            return redirect('katalog:index')        
        except:
            messages.add_message(request, messages.ERROR, 'terjadi kesalahan, pastikan form sudah terisi semua')
            return redirect('katalog:create')        
    else:
        return render(request, 'katalog/create.html')

def update(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    if request.method == 'POST':
        try:
            buku.judul = request.POST['judul']
            buku.penerbit = request.POST['penerbit']
            buku.pengarang = request.POST['pengarang']
            buku.tahun = request.POST['tahun']
            buku.save()
            messages.add_message(request, messages.SUCCESS, 'berhasil megubah buku')
            return redirect('katalog:update', pk=pk)
        except:
            messages.add_message(request, messages.ERROR, 'gagal megubah buku')
            return redirect('katalog:update', pk=pk)
    else:
        return render(request, 'katalog/update.html', {'buku': buku})

def delete(request, pk):
    buku = get_object_or_404(Buku, pk=pk)
    buku.delete()
    messages.add_message(request, messages.SUCCESS, 'berhasil menghapus buku')
    return redirect('katalog:index')