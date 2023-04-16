#!/usr/bin/python3

## Example of Python 3 - bytearray
random_byte_array = bytearray( 'ABC', 'utf-8' )

example14 = memoryview( random_byte_array )

print( example14[ 0 ] )
print( "------------" )
print( type( example14 ) )

print( "------------" )
print( "Create byte from memory view" )
print( bytes( example14[ 0:2 ] ) )

print( "------------" )
print( "Create list from memory view" )
print( list( example14[ 0:3 ] ) )