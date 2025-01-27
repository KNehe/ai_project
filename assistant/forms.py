from django import forms

class BlogForm(forms.Form):
    topic = forms.CharField(label="Enter a topic for blog idea", max_length=100, required=False)
    text = forms.CharField(label="Enter text to rewrite", widget=forms.Textarea, required=False)
    tone = forms.ChoiceField(
        label="Select a tone",
        choices=[('professional', "Professional"), ('casual', 'Casual'), ('humorous', 'Humorous')],
        required=False
    )