# Generated by Django 4.0.4 on 2022-12-28 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=50)),
                ('channel_image', models.ImageField(blank=True, default='https://dummyimage.com/1600x900', null=True, upload_to='channel_images/')),
                ('subscribers', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(default='SplitUnity', max_length=20)),
                ('navbar_logo', models.ImageField(blank=True, default='https://dummyimage.com/99x24', null=True, upload_to='page_contents/')),
                ('footer_logo', models.ImageField(blank=True, default='https://dummyimage.com/99x24', null=True, upload_to='page_contents/')),
                ('footer_description', models.CharField(blank=True, default='Lorem ipsum dolor sit amet consectetur adipiscing elit platea convallis tortor, et laoreet posuere nisi suspendisse mollis gravida facilisi fusce cras, augue dictumst tempor imperdiet lacus risus neque elementum nisl.', max_length=500, null=True)),
                ('footer_address', models.CharField(blank=True, default='Lorem ipsum dolor sit amet consectetur, adipiscing elit platea nec.', max_length=100, null=True)),
                ('footer_phone', models.CharField(blank=True, default='+123456789', max_length=20, null=True)),
                ('footer_email', models.CharField(blank=True, default='lorem@lorem.com', max_length=50, null=True)),
                ('social_icon_1', models.CharField(blank=True, default='twitter', max_length=30, null=True)),
                ('social_icon_url_1', models.URLField(default='https://google.com')),
                ('social_icon_2', models.CharField(blank=True, default='facebook', max_length=30, null=True)),
                ('social_icon_url_2', models.URLField(default='https://google.com')),
                ('social_icon_3', models.CharField(blank=True, default='youtube', max_length=30, null=True)),
                ('social_icon_url_3', models.URLField(default='https://google.com')),
                ('social_icon_4', models.CharField(blank=True, default='instagram', max_length=30, null=True)),
                ('social_icon_url_4', models.URLField(default='https://google.com')),
                ('footer_social_icon_1', models.CharField(blank=True, default='facebook-f', max_length=30, null=True)),
                ('footer_social_icon_url_1', models.URLField(default='https://google.com')),
                ('footer_social_icon_2', models.CharField(blank=True, default='twitter', max_length=30, null=True)),
                ('footer_social_icon_url_2', models.URLField(default='https://google.com')),
                ('footer_social_icon_3', models.CharField(blank=True, default='instagram', max_length=30, null=True)),
                ('footer_social_icon_url_3', models.URLField(default='https://google.com')),
                ('footer_social_icon_4', models.CharField(blank=True, default='youtube', max_length=30, null=True)),
                ('footer_social_icon_url_4', models.URLField(default='https://google.com')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('banner', models.ImageField(default='/static/1600x900.png', upload_to='video_banner')),
                ('path', models.FileField(upload_to='videos/')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('number_of_views', models.IntegerField(blank=True, default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Video_View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.video')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.video')),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.video')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.video')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Channel_Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
