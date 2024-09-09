from django.db import models
import uuid
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    gender = models.CharField(choices=(('Male','MALE'),('Female','FEMALE')),max_length=6)


class BaseModel(models.Model):
    uid = models.CharField(primary_key=True, default=uuid.uuid4,editable=False,max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Question(BaseModel):
    question = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category_type')
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

class Answer(BaseModel):
    question = models.ForeignKey(Question,related_name='quetion_name',on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


