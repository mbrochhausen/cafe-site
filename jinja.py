import jinja2
import os

template_path = 'templates'
output_path = 'static'
templates = jinja2.FileSystemLoader(searchpath=template_path)
env = jinja2.Environment(loader=templates)

for name in env.list_templates():
    if name != 'base.html':
        t = env.get_template(name)
        with open(os.path.join(output_path, name), 'w') as f:
            f.write(t.render())
