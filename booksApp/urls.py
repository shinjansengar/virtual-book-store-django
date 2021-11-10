from django.urls import path
from . import views

urlpatterns = [
    path('allbooks/',views.allBooks),
    path('activebooks/',views.activeBooks),
    path('addbook/',views.addBook),
    path('editbook/<int:id>',views.editBook),
    path('delistedbooks/',views.delistedBooks),
    path('getbook/<int:id>',views.getBook),
    path('deletebook/<int:id>',views.deleteBook),
    path('allcategories/',views.allCategories),
    path('allsubcategories/',views.allSubCategories),
    path('addcategory/',views.addCategory),
    path('addsubcategory/',views.addSubCategory),
    path('delistbook/<int:id>',views.delistBook),
]