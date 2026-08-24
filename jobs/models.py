from django.db import models


class Job(models.Model):
    title = models.CharField(
        max_length=200
    )

    company = models.CharField(
        max_length=200,
        blank=True,
    )

    location = models.CharField(
        max_length=200,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    url = models.URLField(
        max_length=1000,
        unique=True,
    )

    source = models.CharField(
        max_length=100,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    first_seen_at = models.DateTimeField(
        auto_now_add=True,
    )

    last_seen_at = models.DateTimeField(
        auto_now=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"{self.title} - {self.company}"