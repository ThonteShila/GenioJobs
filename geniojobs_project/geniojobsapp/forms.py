from django import forms
class FeedbackForm(forms.Form):
   
    name=forms.CharField(label="Employer's Login",max_length=100)
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'