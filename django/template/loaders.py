# -*- coding: utf-8 -*-
from django.template import loader, Context

# templates/home.html

<html>
    <body>
        Hello, {{ name }}
    </body>
</html>

t = loader.get_template('home.html')
c = Context({'name': 'John'})
rendered = t.render(c)


# Buscando até encontrar um template usando select_template

t = loader.select_template('index.html', 'home.html')
c = Context({'name': 'John'})
rendered = t.render(c)
