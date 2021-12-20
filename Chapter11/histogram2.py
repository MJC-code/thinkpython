Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {}
>>> a
{}
>>> a = dict()
>>> a
{}
>>> a[1] = 'apple'
>>> a
{1: 'apple'}
>>> a[4] = 'banana'
>>> a
{1: 'apple', 4: 'banana'}
>>> a
{1: 'apple', 4: 'banana'}
>>> a
{1: 'apple', 4: 'banana'}
>>> a['dfd'] = 6
>>> a
{1: 'apple', 4: 'banana', 'dfd': 6}
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[3]
KeyError: 3
>>> a[2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[2]
KeyError: 2
>>> a[1]
'apple'
>>> a[4]
'banana'
>>> 1 in a
True
>>> 2 in a
False
>>> a.values()
dict_values(['apple', 'banana', 6])
>>> 
============ RESTART: /home/mark/thinkpython/Chapter11/histogram.py ============
>>> 
============ RESTART: /home/mark/thinkpython/Chapter11/histogram.py ============
{'h': 1, 'i': 1, 'p': 3, 'o': 2, 't': 1, 'a': 1, 'm': 1, 'u': 1, 's': 1}
>>> 