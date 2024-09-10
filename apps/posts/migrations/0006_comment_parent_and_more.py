# Generated by Django 5.1 on 2024-09-08 16:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0002_company_average_score"),
        ("posts", "0005_post_dislike_cnt_post_like_cnt_alter_post_user_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="replies",
                to="posts.comment",
            ),
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["deleted_at"], name="posts_comme_deleted_8831e0_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["deleted_at"], name="posts_post_deleted_b51458_idx"
            ),
        ),
    ]