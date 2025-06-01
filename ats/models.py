from django.db import models
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


class Candidate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

    @classmethod
    def search_name(self, name_query):
        # build search query with input name keyword terms
        vector = SearchVector("name")
        query = SearchQuery(" | ".join(name_query.split(" ")), search_type="raw")

        # sort by how often terms appear, how close together terms are
        rank = SearchRank(vector, query)
        search_results = (
            Candidate.objects.annotate(search=vector, rank=rank)
            .filter(search=query)
            .order_by("-rank")
        )

        return search_results
