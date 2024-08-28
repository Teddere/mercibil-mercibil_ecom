from django import forms
from articles.models import Category,Article,ArticleImage

GENRE_CHOICES = [
    ('woman','Femme'),
    ('man','Homme'),
    ('kid','Enfant'),
    ('mixed','Mixte')
]

LABEL_CHOICES = [
    ('new','Nouveau'),
    ('sale','Solde'),
    ('without','Sans')
]
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','image']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name','category','genre','price','stock','label','thumbnail','description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Article...'}),
            'category': forms.Select(attrs={'class':'form-control','placeholder':'Type d\'article...'}),
            'price': forms.NumberInput(attrs={'class':'form-control','placeholder':'Prix de l\'article...'}),
            'stock': forms.NumberInput(attrs={'class':'form-control','placeholder':'Nombre d\'articles'}),
            'genre': forms.Select(choices=GENRE_CHOICES,attrs={'class':'form-control','placeholder':'Sélectionner un genre'}),
            'label': forms.Select(choices=LABEL_CHOICES,attrs={'class':'form-control','placeholder':'Choisissez un label '}),
            'thumbnail': forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Sélectionnez une image de l\'article'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description...'}),
        }
        labels = {
            'name': "Nom de l'article",
            'category': "Catégorie",
            'price': "Prix de l'article",
            'stock': "Stock",
            'genre': "Style",
            'label': "Etiquette",
            'thumbnail': 'Image principale',
            'description': "Description de l'article",


        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all().order_by('name')

class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = ['image']