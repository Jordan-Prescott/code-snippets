# Replacing complex if statements with dictionaries
# if staten=ment
if format == 'text':
    formatter == TextFormatter()
elif format == 'csv':
    formatter == CSVFormatter()
elif format == 'html':
    formatter == HTMLFormatter()
else:
    raise ValueError('Unknown format')

# dictionary
_formats = {
    'text': TextFormatter,
    'csv': CSVFormatter,
    'html': HTMLFormatter
}

if format in _formats:
    formatter = _formats[format]()
else:
    raise ValueError('Unknown format')