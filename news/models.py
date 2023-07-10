from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    authorRating = models.IntegerField(default=0)

    def update_rating(self):

        author_posts_rating = Post.objects.filter(author_id=self.pk).aggregate(posts_rating_sum=Sum('postRating') * 3)['posts_rating_sum']
        
        authorCommentsRating = Comment.objects.filter(userPost_id=self.user).aggregate(comments_rating_sum=Sum('commentRating'))['comments_rating_sum']
        
        postCommentRating = Comment.objects.filter(commentPost_id=self.pk).aggregate(comments_post_rating_sum=Sum('commentRating'))['comments_post_rating_sum']

        self.authorRating = author_posts_rating + authorCommentsRating + postCommentRating
        self.save()
    
    
    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    categoryName = models.CharField(max_length=64, unique=True)
    
    
    def __str__(self):
        return f'{self.categoryName}'


class Post(models.Model):
    
    article = 'AR'
    news = 'NW'
    
    POST_TYPE = [
        (article, 'Статья'),
        (news, 'Новости')
    ]
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    postType = models.CharField(max_length=2, choices=POST_TYPE, default=article)
    timeDateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=255)
    text = models.TextField()
    postRating = models.IntegerField(default=0)


    def like(self):
        self.rating += 1
        self.save()    
    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:128] + '...'
    
    def __str__(self):
        return f'{self.author}, {self.timeDateCreation}, {self.title}'
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    
    

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}, {self.category}'

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    userPost = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    creationData = models.DateTimeField(auto_now_add=True)
    commentRating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    
    def dislike(self):
        self.rating -= 1
        self.save()
