"""
Text wrapping using Python (HackerRank)
"""
'''method 1'''

# import textwrap
# def wrap(string, max_width):
#     wrapped = textwrap.wrap(string, width=max_width)
#     return "\n".join(wrapped)
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

'''method 2'''

# import textwrap
# def wrap(string, max_width):
#     wrapped=textwrap.TextWrapper(width=max_width)
#     return "\n".join(wrapped.wrap(string))
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

'''method 3'''

# import textwrap
# def wrap(string, max_width):
#     w = textwrap.fill(string,max_width)
#     return w
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)