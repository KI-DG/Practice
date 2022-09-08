from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATION_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATION_CHOICES)
    # nation = forms.ChoiceField(choices=NATION_CHOICES, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm):
                        #상속
    title = forms.CharField(
        label='제목' ,
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            }
        )
    )
    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder': 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages ={
            'required': 'Please enter your content'
        }
    )
    # 딕셔너리 형태로 넣어준다  

    class Meta:
        model = Article
        # 어떤 모델을 기반으로 할지 (호출하지 않는다) 등록을 하지 않는다 참조값으로 활용
        fields = '__all__'
        # 어떤 모델필드 중 어떤 것을 출력할지 결정
        # 리스트 혹은 튜플로 진행
        # ['title', 'content']
        # exclude = ('title',) 제외 시키고 싶을때 사용
        # widget ={
        #     'title': forms.TextInput(attrs={
        #         'class': 'title',
        #         'placeholder' : 'Enter the title',
        #         'maxlength': 10,
        #         }
        #     )
        # }