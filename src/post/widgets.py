from django import forms

class DateTimePickerInput(forms.DateInput):
  input_type = 'date'