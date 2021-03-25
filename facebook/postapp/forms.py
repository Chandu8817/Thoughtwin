from  django import  forms
from  .models import Post,Comment

# class PostForm(forms.Form):
class PostForm(forms.ModelForm):
    contain=forms.CharField(widget=forms.Textarea(
        attrs={

        'class': 'form-control',
        'placeholder': ' Whats on your Mind   ! ',
        'rows':"5",
        'max-width':'240',
        'id': 'post_contain',
        'name':'post_contain'}))
    
    image= forms.ImageField(widget=forms.FileInput(attrs=
    {
        'id':'image_file',
        'name':'image_file',
    }))

    class Meta:
        model = Post

        fields=('contain','image')
        # exclude = ('user',)

# class LikesnCommentsForm(forms.ModelForm):

#     model= LikesnComments
#     fields=('comments','likes')



   

       
      