from django.shortcuts import render
from pieces.models import Piece

def piece_index(request):
    pieces = Piece.objects.all()
    context = {
        'pieces': pieces
    }
    return render(request, 'piece-index.html', context)

def piece_detail(request, pk):
    piece = Piece.objects.get(pk=pk)
    context = {
        'piece': piece
    }
    return render(request, 'piece-detail.html', context)
