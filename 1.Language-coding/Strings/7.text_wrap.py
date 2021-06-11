import textwrap

s = """This function wraps the input paragraph such that each line
in the paragraph is at most width characters long. The wrap method
returns a list of output lines. The returned list
is empty if the wrapped
output has no content."""

text_wrap = textwrap.TextWrapper(width=80)
result_list = text_wrap.wrap(s)

print(result_list)


#


result_str = "".join(result_list)
print(result_str)



