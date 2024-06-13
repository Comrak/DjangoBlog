from django.db import migrations, models

def add_default_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    default_categories = [
        'Technology',
        'Health',
        'Science',
        'Education',
        'Travel',
        'Lifestyle'
    ]
    for category_name in default_categories:
        Category.objects.create(name=category_name)

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),  # Asegúrate de que la dependencia es la migración inicial correcta
    ]

    operations = [
        migrations.RunPython(add_default_categories),
    ]