from django import forms
from .models import blog
class blogform(forms.ModelForm):
    class Meta : #내가 아래에 있는 필드들 적절히 연결해주겟다~
        model=blog
        fields=['title', 'writer', 'body', 'image']
        #필드에서 내가 원하는 아이들만 pick해서 blogForm으로 해주겟당~