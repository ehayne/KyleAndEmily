from kyleandemily import settings


def wedding_default(request):
    return {
        'css_file': ['base/css/main.css',
                     'base/css/normalize.css',
                     'wedding/css/wedding.css',],
        'js_file': ['base/js/vendor/jquery-1.11.0.min.js',],
        'page_title': 'Kyle & Emily',
        'window_title': 'Kyle Rockman and Emily Buschang''s Wedding Site',  #use full names for search engine optimization
    }