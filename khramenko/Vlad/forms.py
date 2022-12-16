from django import forms
class ArticlesForms(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"name":'title'}))
    URL = forms.URLField( widget=forms.URLInput(attrs={"name":'link'}))
    content = forms.CharField(widget=forms.Textarea(attrs={"name":'content'}))
    is_published = forms.BooleanField(initial=True,widget=forms.CheckboxInput(attrs={"name":'is_published'}))
    category = forms.ChoiceField(choices=(('Старое','Старое'),('Новое','Новое')),widget=forms.Select(attrs={"name":'category'}))