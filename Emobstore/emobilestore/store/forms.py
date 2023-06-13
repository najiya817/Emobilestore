from django import forms
from account.models import products



class AddProductForm(forms.ModelForm):
    class Meta:
        model=products
        fields=["product_name","price","description","image"]
        widget={
                "product_name":forms.TextInput(attrs={"class":"form-control"}),
                "price":forms.IntegerField(),
                "description":forms.Textarea(attrs={"class":"form-control"}),
                "image":forms.FileInput()
        }

class CPassForm(forms.Form):
    old_pass=forms.CharField(max_length=100,label="Old password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter old password"}))    
    new_pass=forms.CharField(max_length=100,label="New Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter new password"}))
    confirm_pass=forms.CharField(max_length=100,label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Re-enter new password"}))