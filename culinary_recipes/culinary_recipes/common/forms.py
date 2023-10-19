from django import forms

from culinary_recipes.common.models import RecipeComment


class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                 attrs={
                    'cols': 40,  
                    'rows': 4,  
                    'placeholder': 'Въведи коментар...',
                     'style':'resize:none;'
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


class ContactForm(forms.Form):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    SUBJECT_MAX_LENGTH = 100
    MESSAGE_MAX_LENGTH = 2000

    first_name = forms.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        label='First Name',
        widget=forms.TextInput(
            attrs={
                # 'placeholder': 'Въведи името си'
            }),

    )
    last_name = forms.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                # 'placeholder': 'Въведи фамилията си'
            }),

    )
    subject = forms.CharField(
        max_length=SUBJECT_MAX_LENGTH,
        label='Title',
        widget=forms.TextInput(
            attrs={
                # 'placeholder': 'Въведи заглавие'
            }),

    )
    email_address = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                # 'placeholder': 'example@example.com'
            }),

    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(
            attrs={
                # 'placeholder': 'Въведи съобщението си тук ...'
            }),
        max_length=MESSAGE_MAX_LENGTH,
    )
