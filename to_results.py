from collections import defaultdict
from json import dumps
from re import compile as recompile
from os import walk
from os.path import join

base_dir = '/tmp/xxx'

SPLIT_PATTERN = recompile( r'{0}/(?P<uid>.*)/(?P<source>(?P<exercise>.*)\.java)'.format( base_dir ) )

res = defaultdict( lambda : defaultdict( lambda : defaultdict( lambda : defaultdict( lambda : defaultdict( lambda : dict ) ) ) ) )
for root, dirs, files in walk( base_dir ):
	for name in files:
		path = join( root, name )
		match = SPLIT_PATTERN.match( path )
		if match:
			s = match.groupdict()
			with open( path, 'r' ) as f:
				res[ s[ 'uid' ] ][ 'exercises' ][ s[ 'exercise' ] ][ 'sources' ][ s[ 'source' ] ] = f.read()
				res[ s[ 'uid' ] ][ 'exercises' ][ s[ 'exercise' ] ][ 'cases' ] = [ {
					'name': '',
					'stdout': '',
					'stderr': '',
					'failure': '',
					'error': '',
					'type': '	'
				} ]


for uid, rest in res.items():
	res[ uid ][ 'signature' ] = [ uid, uid, '' ]

print 'results = {0};'.format( dumps( res ) )
