from textwrap import TextWrapper
from string import split, join

def comment(text, wrap=80, escape='% ', escape_first='', escape_last=''):
    '''comment filter
    Takes a string in text, and wraps it to wrap characters in length with
    preceding comment escape sequence on each line. escape_first and 
    escape_last can be used for languages which define block comments.
    Examples:
        C++ inline comment    comment(80, '// ')
        C block comment:      comment(80, ' * ', '/*', ' */')
        Matlab comment:       comment(80, '% ')
        Matlab block comment: comment(80, '', '%{', '%}')
        Python docstrings:    comment(80, '', '\'\'\'', '\'\'\'')
    '''

    tw = TextWrapper(width=wrap-len(escape))
    if escape_first:
        escape_first = escape_first+'\n'
    if escape_last:
        escape_last = '\n'+escape_last
    escapn = '\n'+escape
    lines  = text.split('\n')
    wlines = (tw.wrap(line) for line in lines)
    return escape_first+escape+join((join(line, escapn) for line in wlines), escapn)+escape_last
