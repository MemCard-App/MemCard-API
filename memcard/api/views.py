from rest_framework import generics, status, viewsets
from .serializers import WordSerializer
from memcard.models import Word


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WordList(generics.ListAPIView):
    serializer_class = WordSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return Word.objects.filter(user=username)
