from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import FeedSerializer
from rss.models import Feed
from .permissions import IsAuthorOrReadOnly


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all().order_by("-created_at")
    serializer_class = FeedSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # save the current login user as author
        serializer.save(user=self.request.user)
