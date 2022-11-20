from django import forms

from culinary_recipes.common.models import RecipeComment


class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...'
                },
            ),
        }


class RecipeCommentDeleteForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance


class RecipeCommentEditForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('text',)
