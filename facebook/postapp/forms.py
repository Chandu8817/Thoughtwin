from  django import  forms
from  .models import UserPost,LikesnComments

# class PostForm(forms.Form):
class PostForm(forms.ModelForm):
    postcontain=forms.CharField(widget=forms.Textarea(
        attrs={

        'class': 'post_catain2',
        'placeholder': ' Whats on your Mind   ! ',
        'rows':"5",
        'max-width':'240',
        'id': 'post_catain'}))

    class Meta:
        model = UserPost

        fields=('postcontain','postimage')
        # exclude = ('user',)

# class LikesnCommentsForm(forms.ModelForm):

#     model= LikesnComments
#     fields=('comments','likes')



   

       
      