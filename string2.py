#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    if len(s) >= 3 and s.endswith('ing'):
        s = s + 'ly'
    elif len(s) >= 3:
        s = s + 'ing'
    else:
        s = s
    return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    result_string = s
    s = s.split()
    if 'bad' in s:
        bad_index = s.index('bad')
        not_index = s.index('not')
        if bad_index > not_index:
            s_start = s[0:not_index]
            s_end = s[bad_index + 1:]
            s_start.append('good')
            s_start = ' '.join(s_start)
            s_end = ' '.join(s_end)
            result_string = s_start + s_end
            return result_string
        else:
            return result_string
    elif 'bad!' in s:
        bad_bang_index = s.index('bad!')
        not_index = s.index('not')
        if bad_bang_index > not_index:
            s_start = s[0:not_index]
            s_end = s[bad_bang_index + 1:]
            s_start.append('good!')
            s_start = ' '.join(s_start)
            s_end = ' '.join(s_end)
            result_string = s_start + s_end
            return result_string
        else:
            return result_string
    else:
        return result_string
        

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back


def front_back(a, b):
    result_string = ''
    if len(a) % 2 == 0 and len(b) % 2 == 0:
        a_front = a[0:(len(a)/2)]
        a_back = a[(len(a)/2):]
        b_front = b[0:(len(b)/2)]
        b_back = b[(len(b)/2):]
        result_string = a_front + b_front + a_back + b_back
        return result_string
    elif len(a) % 2 == 1 and len(b) % 2 == 1:
        a_front = a[0:(len(a)/2 + 1)]
        a_back = a[(len(a)/2 + 1):]
        b_front = b[0:(len(b)/2 + 1)]
        b_back = b[(len(b)/2 + 1):]
        result_string = a_front + b_front + a_back + b_back
        return result_string
    elif len(a) % 2 == 0 and len(b) % 2 == 1:
        a_front = a[0:(len(a)/2)]
        a_back = a[(len(a)/2):]
        b_front = b[0:(len(b)/2 + 1)]
        b_back = b[(len(b)/2 + 1):]
        result_string = a_front + b_front + a_back + b_back
        return result_string
    elif len(a) % 2 == 1 and len(b) % 2 == 0:
        a_front = a[0:(len(a)/2 + 1)]
        a_back = a[(len(a)/2 + 1):]
        b_front = b[0:(len(b)/2)]
        b_back = b[(len(b)/2):]
        result_string = a_front + b_front + a_back + b_back
        return result_string


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.


def test(got, expected):
    """Your code goes here.  Edit this docstring."""
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    """Your code goes here.  Edit this docstring."""
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
