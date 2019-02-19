from flask_assets import Bundle, Environment, Filter
from flask import Flask


class ConcatFilter(Filter):
    def concat(self, out, hunks, **kw):
        out.write(';'.join([h.data() for h, info in hunks]))


scss_main = Bundle(
    '../assets/sass/index.scss',
    '../assets/sass/main.scss',
    filters=('libsass', 'cssmin'),
    output='css/main.css'
)

js = Bundle(
    '../assets/js/blazy.js',
    '../assets/js/main.js',
    filters=(ConcatFilter, 'jsmin'),
    output='js/packed.js'
)

assets = Environment()
assets.register('scss_main', scss_main)
assets.register('js_all', js)
