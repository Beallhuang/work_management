# Generated by Django 4.2.13 on 2024-11-25 09:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("industry_report_upload", "0002_alter_uploadfiletemplate_template_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadfiletemplate",
            name="brand",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("BL", "百丽"),
                    ("TT", "他她"),
                    ("BS", "百思图"),
                    ("TM", "天美意"),
                    ("SD", "森达"),
                    ("BT", "拔佳"),
                    ("ST", "思加图"),
                    ("ML", "妙丽"),
                    ("JP", "真美诗"),
                    ("HP", "暇步士"),
                    ("CL", "其乐"),
                    ("SK", "圣伽步"),
                    ("FM", "十五分钟"),
                    ("CM", "冠军（鞋）"),
                    ("XM", "TooManyShoes"),
                    ("QS", "高跟73小时"),
                    ("~", "空"),
                ],
                default="~",
                max_length=300,
                verbose_name="品牌",
            ),
        ),
        migrations.AlterField(
            model_name="uploadfiletemplate",
            name="platform",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("5fdba8f8c2c411e79346b8ee653d98c5", "天猫"),
                    ("956000afc2cb11e79346b8ee653d98c5", "京东"),
                    ("41f0e16416cd11ec8c41506b4b386376", "抖音"),
                    ("e3d68801c2c911e79346b8ee653d98c5", "唯品会"),
                    ("5fdba878c2c411e79346b8ee653d98c5", "其他"),
                ],
                max_length=300,
                verbose_name="平台",
            ),
        ),
    ]
