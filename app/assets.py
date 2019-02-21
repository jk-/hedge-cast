from flask_assets import Bundle, Environment, Filter
from flask import Flask


class ConcatFilter(Filter):
    def concat(self, out, hunks, **kw):
        out.write(";".join([h.data() for h, info in hunks]))


scss_materialize = Bundle(
    "../assets/sass/materialize/main.scss",
    filters=("libsass", "cssmin"),
    output="css/materialize.css",
)

assets = Environment()
assets.register("scss_materialize", scss_materialize)
