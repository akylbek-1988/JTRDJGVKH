from django.conf import settings
from django.http import FileResponse, Http404


def homepage(request):
    """Serve the existing public landing page at the site's root URL."""
    page = settings.BASE_DIR / "index.html"
    if not page.is_file():
        raise Http404("Homepage not found.")
    return FileResponse(page.open("rb"), content_type="text/html; charset=utf-8")
