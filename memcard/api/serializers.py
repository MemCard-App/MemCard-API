from memcard.models import Word
from rest_framework import serializers
from .meaning import find_meaning

class WordSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    meaning = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Word
        exclude = ["user"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_meaning(self, instance):
        word = instance.word
        return find_meaning(word)
    
    def get_username(self, instance):
        request = self.context.get("request")
        # if request.user.is_authenticated:
        return instance.user.get_username()
# 