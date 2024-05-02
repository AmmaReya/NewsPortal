from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = self.posts.aggregate(pr=Coalesce(Sum('rating'), 0)).get('pr')
        comments_rating = self.author.comments.aggregate(cr=Coalesce(Sum('rating'), 0)).get('cr')
        post_comment_rating = self.posts.aggregate(pcr=Coalesce(Sum('rating'), 0)).get('pcr')
        print(posts_rating)
        print('------------------')
        print(comments_rating)
        print('------------------')
        print(post_comment_rating)

        self.rating = posts_rating * 3 + comments_rating + post_comment_rating
        self.save()


class Category(models.Model):
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag


article = 'AR'
news = 'NE'

GENRE = [
    (article, 'Статья'),
    (news, 'Новость'),
]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    genre = models.CharField(max_length=2, choices=GENRE, default=news)
    post_time_in = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text_comment = models.TextField()
    comment_time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
