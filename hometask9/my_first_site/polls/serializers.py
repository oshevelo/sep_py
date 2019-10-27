from rest_framework import serializers
from polls.models import Question,Choice



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk','question_text', 'pub_date']




class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['pk','question', 'choice_text','votes']


