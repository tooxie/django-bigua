from settings import CSS_PATH, JS_PATH, MEDIA_URL
# from flash.models import Flash

def urls(request):
    return {'CSS_PATH': CSS_PATH, 'JS_PATH': JS_PATH, 'MEDIA_URL': MEDIA_URL}
