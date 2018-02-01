from string import Template

s=Template("There are ${howmany} ${lang} Quotation Symbols")
print(s.safe_substitute(lang="Python"))