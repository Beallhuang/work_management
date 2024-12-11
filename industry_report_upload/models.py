from django.db import models
from multiselectfield import MultiSelectField
import re
import sys 
from django.utils.html import format_html
sys.path.append("/home/huang.biao/anaconda3/lib/python3.9/site-packages/base_function/industry_report_center") 
import base_api


api = base_api.BaseApi()

report_tag_str = 'class ReportTagEnum(models.TextChoices):\n'
for name, code in api.get_report_tag().items():
    report_tag_str += f"    {code} = '{code}', '{name}'\n"
exec(report_tag_str)

report_type_str = 'class ReportTypeEnum(models.TextChoices):\n'
for name, code in api.get_report_type().items():
    report_type_str += f"    {code} = '{code}', '{name}'\n"
exec(report_type_str)

platform_str = 'class PlatformEnum(models.TextChoices):\n'
for name, code in api.get_platform1().items():
    platform_str += f"    {name} = '{code}', '{name}'\n"
exec(platform_str)

brand_str = 'class BrandEnum(models.TextChoices):\n'
for name, code in api.get_brand().items():
    brand_str += f"    {code} = '{code}', '{name}'\n"
brand_str += f"    all = '~', '全部'\n"
exec(brand_str)

source_app_str = 'class SourceAppEnum(models.TextChoices):\n'
for name, code in api.get_source_app().items():
    source_app_str += f"    {code} = '{code}', '{name}'\n"
exec(source_app_str)

role_str = 'class RoleEnum(models.TextChoices):\n'
for name, code in api.get_role().items():
    name_adj = re.sub(r'[-【】（）\(\)\s\+&]', '_', name)
    role_str += f"""    {name_adj} = '{code}', '{name}'\n"""
exec(role_str)

    
class CoverImageTemplate(models.Model):
    template_page_id = models.CharField(max_length=50, primary_key=True, verbose_name='模板页id')
    image_path = models.ImageField(upload_to='industry_report_upload/image/', verbose_name='封面图模板')

    title_x = models.IntegerField(default=0, verbose_name='标题x坐标')
    title_y = models.IntegerField(default=0, verbose_name='标题y坐标')
    title_font_size = models.IntegerField(default=120, verbose_name='标题字体大小')    
    title_font_color = models.CharField(max_length=20, default='#000000', verbose_name='标题字体颜色')
    date_x = models.IntegerField(default=0, verbose_name='日期x坐标')
    date_y = models.IntegerField(default=0, verbose_name='日期y坐标')
    date_font_size = models.IntegerField(default=60, verbose_name='日期字体大小')
    date_font_color = models.CharField(max_length=20, default='#000000', verbose_name='日期字体颜色')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.template_page_id

    class Meta:
        verbose_name = '报告封面图模板'
        verbose_name_plural = '报告封面图模板'


class UploadFileTemplate(models.Model):
    dir_path = models.CharField(max_length=300, blank=False, null=False, verbose_name='待上传目录')
    template_page = models.ForeignKey(to='CoverImageTemplate', to_field='template_page_id', on_delete=models.SET_DEFAULT, default='page-0001', verbose_name='模板页id')
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='模板标题')
    report_type = models.CharField(max_length=50, choices=ReportTypeEnum.choices, verbose_name='报告类型')
    report_tag = models.CharField(max_length=50, choices=ReportTagEnum.choices, verbose_name='报告标签')
    platform = MultiSelectField(max_length=300, choices=PlatformEnum.choices, verbose_name='平台')
    brand = MultiSelectField(max_length=300, choices=BrandEnum.choices, default=BrandEnum.all , verbose_name='品牌')
    role = MultiSelectField(max_length=50, choices=RoleEnum.choices, verbose_name='角色组id')
    if_to_wps = models.BooleanField(default=False, verbose_name='是否转为wps')
    is_active = models.BooleanField(default=True, verbose_name='是否有效')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '待上传文件配置'
        verbose_name_plural = '待上传文件配置'



