from flask_assets import Bundle, Environment, Filter
from flask import Flask


class ConcatFilter(Filter):
    def concat(self, out, hunks, **kw):
        out.write(";".join([h.data() for h, info in hunks]))


scss_main = Bundle(
    "../assets/sass/index.scss",
    "../assets/sass/main.scss",
    filters=("libsass", "cssmin"),
    output="css/main.css",
)

scss_materialize = Bundle(
    "../assets/sass/materialize/main.scss",
    filters=("libsass", "cssmin"),
    output="css/materialize.css",
)

js = Bundle(
    "../assets/js/blazy.js",
    filters=(ConcatFilter, "jsmin"),
    output="js/vendor.js",
)

assets = Environment()
assets.register("scss_main", scss_main)
assets.register("scss_materialize", scss_materialize)
assets.register("js_all", js)
