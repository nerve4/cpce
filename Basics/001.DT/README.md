# Python Data Types


## Summary

Data type is an important concept. Variables can store data of different types, and different types can do different things.


## Data Types

|:--------------- |:---------------------------- |
| Text Type:      | str                          |
| Numeric Types:  | int, float, complex          |
| Sequence Types: | list, tuples, range          |
| Mapping Type:   | dict                         |
| Set Types:      | set, frozenset               |
| Boolean Type:   | bool                         |
| Binary Types:   | bytes, bytearray, memoryview |
| None Type:      | NoneType                     |


## Print the Data Type

Use `type()` function to get the data type:
```
x = "test1"
print( type( x ) )

y = 10
print( type( y ) )
```


## Python 3 - str

A string is a sequence of one or more characters (letters, numbers, symbols) that can be either a constant or a variable. Made up of Unicode, strings are immutable sequences, meaning they are unchanging.
```
example1 = "What is this?"

print( example1 )
print( type( example1 ) )
```


## Python 3 - int (signed integers)

They are often called just integers or ints. They are positive or negative whole numbers with no decimal point. Integers in Python 3 are of unlimited size. Python 2 has two integer types - int and long. There is no 'long integer' in Python 3 anymore.
```
example2 = 10

print( example2 )
print( type( example2 ) )
```


## Python 3 - float

Float represent real numbers and are written with a decimal point dividing the integer and the fractional parts.
```
example3 = 10.55

print( example3 )
print( type( example3 ) )
```


## Python 3 - complex

The complex() method returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number.
```
example4 = complex( 5, -3 )

print( example4 )
print( type( example4 ) )
```


## Python 3 - lists

The list is the most versatile datatype available in Python, which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that the items in a list need not be of the same type.
```
list1 = [ 'test1', 'test2', 'test3' ]
list2 = [ 1, 2, 3, 4 ]
list3 = [ "1", "2", "3", "4" ]

print( list1 )
print( type( list1 ) )
print( "===========" )
print( list2 )
print( type( list2 ) )
print( "===========" )
print( list3 )
print( type( list3 ) )
```


## Python 3 - tuples

Tuples are used to store multiple items in a single variable. Tuples are sequences, just like lists. The main difference between the tuples and the lists is that the tuples cannot be changed unlike lists.
```
tup1 = ( 1, 2, 3, 'this is awesome' ) 
tup2 =  "mouse", "cat", "dog"

print( "tup1[ 0 ]: ", tup1[ 0 ] )
print( type( tup1 ) )

print( "tup1[ 2:3 ]: ", tup1[ 2:3 ] )
print( type( tup2 ) )
```

Tuples are **immutable**, which means you cannot update or change the values of tuple elements. Removing individual tuple elements is not possible.


## Python 3 - range

Python 3 range method returns the sequence of numbers within a given range, range is a Python built-in function.
```
example7 = range( 6 )

for n in example7:
  print( n )

print( type( example7 ) )
```


## Python 3 - dict

Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
**Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.**
```
example8 =	{
  "First Name": "John",
  "Last Name": "Wick",
  "Job": "Retired Freelancer"
}

print( example8 )
print( "------------" )
print( type( example8 ) )
```


## Python 3 - set

A set is a collection of unique data. That is, elements of a set cannot be duplicate and Set items are unchangeable, but you can remove items and add new items.
```
example9 = { "test1", "test2", "test3" }

print( example9 )
print( "------------" )
print( type( example9 ) )
```


## Python 3 - frozenset

The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.
```
example10 = { "test1", "test2", "test3" }

fs = frozenset( example10 )
print( "The frozenset looks like: ", fs )
print( "------------" )
print( type( example10 ) )
```


## Python 3 - bool

Booleans represent one of two values: True or False.
```
example11 = True

print( example11 )
print( "------------" )
print( type( example11 ) )
```


## Python 3 - bytes

The `bytes()` method returns an immutable bytes object initialized with the given size and data.
```
example12 = "This is Python3 Data type BYTES"

convert_to_byte = bytes( example12, 'utf-8' )

print( convert_to_byte )
print( "------------" )
print( type( convert_to_byte ) )
```


## Python 3 - bytearray

With a `bytearray` you can do everything you can with other mutables like push, pop, insert, append, delete, and sort.
```
prime_numbers = [ 2, 3, 5, 7 ]

example13 = bytearray( prime_numbers )

print( example13 )
print( "------------" )
print( type( example13 ) )
```


## Python 3 - memoryview

The `memoryview()` function returns a memory view object of the given argument.
```
random_byte_array = bytearray( 'ABC', 'utf-8' )

example14 = memoryview( random_byte_array )

print( example14[ 0 ] )
print( "------------" )
print( type( example14 ) )
```