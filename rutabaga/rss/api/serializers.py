from rest_framework import serializers

from rss.models import Feed
import feedparser


class FeedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    contents = serializers.SerializerMethodField()

    class Meta:
        model = Feed
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_contents(self, instance):
        rss = feedparser.parse(instance.url)
        items = []

        items.extend(rss["items"])

        items = list(reversed(sorted(items, key=lambda item: item["published_parsed"])))
        return items[0:3]
