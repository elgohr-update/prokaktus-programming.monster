# Generated by Django 2.2 on 2020-01-15 00:13

import apps.base.wagtail.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articleindexpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('markdown', apps.base.wagtail.blocks.MarkDownBlock()), ('sourcecode', apps.base.wagtail.blocks.CodeBlock())], blank=True),
        ),
    ]