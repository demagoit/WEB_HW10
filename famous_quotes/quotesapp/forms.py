from django import forms
from .models import Tag, Author, Quote

class TagForm(forms.ModelForm):
    tag = forms.CharField(min_length=3, max_length=50, required=True, widget=forms.TextInput())

    class Meta:
        model = Tag
        fields = ['tag']

class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(min_length=3, max_length=50, required=True, strip=True, widget=forms.TextInput())
    born_date = forms.DateField(required=False, widget=forms.DateInput())
    born_location = forms.CharField(max_length=150, required=False, strip=True, widget=forms.TextInput)
    description = forms.CharField(required=False, widget=forms.TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    quote  = forms.CharField(min_length=3, max_length=50, required=True, strip=True, widget=forms.TextInput())
    # author  = forms.ForeignKey(Author, on_delete=models.CASCADE)
    # tags = forms.ManyToManyField(Tag)

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']