from django.shortcuts import render
from django.views.generic import TemplateView
from .models import WtpBook, WtpEmo


class Index(TemplateView):
    template_name = 'wtp/index.html'


class Gender(TemplateView):
    template_name = 'wtp/gender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emotion_index'] = self.kwargs['emotion_index']
        return context


class Age(TemplateView):
    template_name = 'wtp/age.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emotion_index'] = self.kwargs['emotion_index']
        context['gender_index'] = self.kwargs['gender_index']
        return context


class Book(TemplateView):
    template_name = 'wtp/book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        emotion_index = self.kwargs['emotion_index']
        gender_index = self.kwargs['gender_index']
        age_index = self.kwargs['age_index']
        book_nums = WtpEmo.objects.filter(emo_emotion=emotion_index, emo_gender=gender_index, emo_age=age_index)
        books = WtpBook.objects.filter(
            book_num__in=[book_num.book_num.book_num for book_num in book_nums]
        )  # 수정한 부분입니다.

        context['books'] = books
        return context
