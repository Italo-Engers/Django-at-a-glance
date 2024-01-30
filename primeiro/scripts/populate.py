from django import setup

from primeiro.news.models import Article, Reporter

setup()

# No reporters ae in the system yet.
Reporter.objects.all()

# Create a new Reporter.
r = Reporter(full_name="Italo Engers")

# # Save the object into the database. You have to call save() explicitly.
# r.save()

# # Now it has an ID.
# r.id

# # Now the new reporter is in the database.
# Reporter.objects.all()

# # Fields are represented as attributes on the Python object.
# r.full_name

# # Django provides a rich database lookup API.
# Reporter.objects.get(id=1)

# Reporter.objects.get(full_name__startswith="Italo")

# Reporter.objects.get(full_name__contains="Engers")

# Reporter.objects.get(id=2)

# # Create an article.
# from datetime import date
# a = Article(
#     pub_date=date.today(), headline="Django is cool", content="Yeah.", reporter=r
# )
# a.save()

# # Now the article is in the database.
# Article.objects.all()

# # Article objects get API access to related Reporter objects.
# r = a.reporter
# r.full_name

# # And vice versa: Reporter objects get API access to Article objects.
# r.article_set.all()

# # The API follows relationships as far as you need, performing efficient
# # JOINs for you behind the scenes.
# # This finds all articles by a reporter whose name starts with "Italo".
# Article.objects.filter(reporter__full_name__startswith="Italo")


# # Change an object by altering its attributes and calling save().
# r.full_name = "Billy Goat"
# r.save()

# # Delete an object with delete().
# r.delete()