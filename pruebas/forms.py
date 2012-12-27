from django import forms
from auth.models import User, Group
from pruebas.models import Presupuesto

  
class PresuForm(forms.ModelForm):
   # raw_body = forms.CharField(widget=MarkItUpWidget())

    class Meta:
        model = Presupuesto
      
    
        
  #  suma = forms.IntegerField(validators=[validate_even])
    def save(self, commit=True):
        model = super(PresuForm, self).save(commit=False)
 
        # Save the latitude and longitude based on the form fields
        model.total = self.cleaned_data['limpieza_obra'] + self.cleaned_data['tareas'] + self.cleaned_data['suelo']
         
        model.totalHormigon= self.cleaned_data['bases']+self.cleaned_data['vigas_fundacion']+self.cleaned_data['columnas']+self.cleaned_data['vigas_encadenado']+self.cleaned_data['piso']
 
        if commit:
            model.save()
 
        return model 



