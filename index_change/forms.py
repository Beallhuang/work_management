# read_excel/forms.py
from django import forms

class ExcelForm(forms.Form):
    sheet_name = forms.CharField(max_length=100, label='Sheet名称', initial='Sheet1')
    start_row = forms.IntegerField(label='标题所在行', initial=1)
    columns = forms.CharField(max_length=100, label='待转化列名', initial='指数')
    parameter = forms.ChoiceField(choices=((1, "pop"), (2, "zy")), initial=2, label='指数来源(pop: 京东pop指数, zy: 京东自营指数)')