from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter, DateFilter
from .models import Post, Category
from django import forms


class PostFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок',
    )

    tag = ModelMultipleChoiceFilter(
        field_name='post_category',
        queryset=Category.objects.all(),
        label='Теги',
        conjoined=True,
    )

    date_time = DateFilter(
        field_name='post_time_in',
        lookup_expr='date__gte',
        label='Дата публикации после',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = Post
        fields = ['title', 'tag', 'date_time']
