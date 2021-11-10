from django.db import models

# Create your models here.

class Book(models.Model):
    bookName = models.CharField(max_length=50)
    authorName = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    isActive = models.BooleanField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    pages = models.IntegerField()
    addedOn = models.DateTimeField(auto_now_add=True,blank=True)
    addedBy = models.CharField(max_length=30, null=True,blank=True)
    lastModifiedOn = models.DateTimeField(auto_now_add=True,blank=True)
    lastModifiedBy = models.CharField(max_length=30, null=True,blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True )
    subCategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.bookName


class Category(models.Model):
    categoryName = models.CharField(max_length=30)
    addedOn = models.DateTimeField(auto_now_add=True)
    addedBy = models.CharField(max_length=30, null=True,blank=True)

    def __str__(self):
        return self.categoryName

class SubCategory(models.Model):
    subCategoryName = models.CharField(max_length=30)
    addedOn = models.DateTimeField(auto_now_add=True)
    addedBy = models.CharField(max_length=30, null=True,blank=True)

    def __str__(self):
        return self.subCategoryName