def myxml(tag, content='', **kwargs):
    attrs = ''.join([f' {key}="{value}"'
                     for key, value in kwargs.items()])
    print(f'<{tag}{attrs}>{content}</{tag}>')


myxml('foo', a=1, b=33)
