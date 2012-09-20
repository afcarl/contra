#!/usr/bin/env python

'''
Penn TreeBank escaping.

Author:     Pontus Stenetorp    <pontus stenetorp se>
Version:    2011-09-12
'''

#XXX: Won't cut it for quotes!

### Constants
# From: To
PTB_ESCAPES = {
        '(': '-LRB-',
        ')': '-RRB-',
        '[': '-LSB-',
        ']': '-RSB-',
        '{': '-LCB-',
        '}': '-RCB-',
    }
###

def escape(s):
    r = s
    assert '"' not in s, 'quoting not supported'
    for _from, to in PTB_ESCAPES.iteritems():
        r = r.replace(_from, to)
    return r

def unescape(s):
    r = s
    for _from, to in PTB_ESCAPES.iteritems():
        r = r.replace(to, _from)
    # Don't do this here... Can't do it right anyway
    r = r.replace('``', '"').replace("''", '"')
    return r

PTB_SEXP_QUOTE_ESCAPES = {
        '(`` ")':   '(`` ``)',
        "('', \")": "('' '')",
    }

def sexp_quotes_escape(s):
    r = s
    for _from, to in PTB_SEXP_QUOTE_ESCAPES.iteritems():
        r = r.replace(_from, to)
    return r

def sexp_quotes_unescape(s):
    r = s
    for _from, to in PTB_SEXP_QUOTE_ESCAPES.iteritems():
        r = r.replace(to, _from)
    return r

def main(args):
    from argparse import ArgumentParser
    from sys import stdin, stdout

    # TODO: Doc!
    argparser = ArgumentParser()
    argparser.add_argument('-u', '--unescape', action='store_true')
    argp = argparser.parse_args(args[1:])

    for line in (l.rstrip('\n') for l in stdin):
        if argp.unescape:
            r = unescape(line)
        else:
            r = escape(line)
        stdout.write(r)
        stdout.write('\n')

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
