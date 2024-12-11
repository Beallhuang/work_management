from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sys
sys.path.append('/home/huang.biao/anaconda3/lib/python3.9/site-packages/base_function')
from jdsz import jdsz_gmv_goods_pop, jdsz_gmv_goods_zy
import pandas as pd
import io

from .forms import ExcelForm

def jdsz_index_change_view(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            sheet_name = form.cleaned_data['sheet_name']
            start_row = form.cleaned_data['start_row']
            columns = form.cleaned_data['columns'].strip()
            parameter = form.cleaned_data['parameter']

            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file, sheet_name=sheet_name, skiprows=range(0, start_row-1))
            

            # 遍历参数并将相应列值乘以2并追加为新的列
            if parameter == '2':
                md = jdsz_gmv_goods_zy.fit
            else:
                md = jdsz_gmv_goods_pop.fit
            for i, v in enumerate(df[columns]):
                try:
                    df.loc[i, '还原金额'] = md(int(str(v).replace(',', '').split('.')[0]))
                except Exception as e:
                    print(f'第{i+2}行{columns}列数据格式错误，请检查: {e}')
                    df.loc[i, '还原金额'] = None


            # 使用pandas将DataFrame保存到Excel内存流
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name=sheet_name)

            # 设置指针到流的开始
            output.seek(0)

            # 创建下载响应
            response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={excel_file.name}'
            return response

    else:
        form = ExcelForm()

    return render(request, 'jdsz_index.html', {'form': form})