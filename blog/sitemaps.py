from django.contrib.sitemaps import Sitemap
from blog.models import post

class postsitemap(Sitemap):

    changefreq = "weekly"
    priority  = 0.5

    def items(self):
        return post.objects.filter(status=1)
    
    def lastmod(self, items):
        return items.published_date