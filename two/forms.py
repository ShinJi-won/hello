from django.forms import ModelForm
from django import forms
from two.models import Food, Review
from django.utils.translation import gettext_lazy as _

REVIEW_SCORE=(
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4),
    ('5',5),
)
class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['score','comment','food']
        labels={
            'score':'평점',
            'comment':'리뷰'
        }
        widgets={
            'food': forms.HiddenInput(),
            'score':forms.Select(choices=REVIEW_SCORE)
        }


class FoodForm(ModelForm):
    class Meta:
        model=Food
        fields=['name','adr','pw']
        labels={
            'name':'음식명',
            'adr':'식당 주소',
            'pw':'비밀번호',
        }
        widgets={
            'pw':forms.PasswordInput()
        }

class UpdateFoodForm(FoodForm):
    class Meta:
        model=Food
        exclude=['pw']