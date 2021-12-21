# Generated by Django 3.2.8 on 2021-12-21 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_price'),
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='author',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='description',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='price',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='title',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='total',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.books'),
            preserve_default=False,
        ),
    ]