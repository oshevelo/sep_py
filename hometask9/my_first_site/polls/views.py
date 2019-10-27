from django.http import HttpResponse
# from django.http import Http404


# Create your views here.
from django.shortcuts import get_object_or_404
from polls.models import Question, Choice
from rest_framework import generics
from polls.serializers import QuestionSerializer, ChoiceSerializer



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



# def index(request):
#     question_list = Question.objects.all()
#     return HttpResponse(', '.join([q.question_text for q in  question_list]))


class Question_List(generics.ListAPIView): # ми просто виведимо список  всіх питань
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class Question_List_Create(generics.ListCreateAPIView):  # ми зможемо бачити і одночасно додавати питання навідміну від просто CreateAPIView
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class Question_Create(generics.CreateAPIView): # Ми просто створюємо питання по наших параметрах, але не бачимо списа питань якій ми вже створили
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class Question_Retrieve(generics.RetrieveAPIView):  # тут ми переглядаємо тільки по одному елементу, по якому ми звертаємося pk
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        return obj


class Question_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj



class Choice_List_Create(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class Choice_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


    def get_object(self):
        obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
        return obj
