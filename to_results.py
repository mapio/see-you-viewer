#!/usr/bin/env python

from collections import defaultdict
from json import dumps
from re import compile as recompile
from os import walk
from os.path import join
from sys import argv

base_dir = argv[ 1 ]

SPLIT_PATTERN = recompile( join( base_dir, r'(?P<uid>.*)/(?P<source>(?P<exercise>.*)\.java)' ) )

res = defaultdict( lambda : defaultdict( lambda : defaultdict( lambda : defaultdict( lambda : defaultdict( lambda : dict ) ) ) ) )
for root, dirs, files in walk( base_dir ):
	for name in files:
		path = join( root, name )
		match = SPLIT_PATTERN.match( path )
		if match:
			s = match.groupdict()
			with open( path, 'r' ) as f:
				res[ s[ 'uid' ] ][ 'exercises' ][ s[ 'exercise' ] ][ 'sources' ][ s[ 'source' ] ] = f.read()
				res[ s[ 'uid' ] ][ 'exercises' ][ s[ 'exercise' ] ][ 'cases' ] = []


for uid, rest in res.items():
	res[ uid ][ 'signature' ] = [ uid, uid, '' ]

print 'results = {0};'.format( dumps( res ) )
