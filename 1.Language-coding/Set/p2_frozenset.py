from frozendict import frozendict

vowels = frozenset({"a", "e", "i", "o", "u"})
# no add / pop api


frozendict = frozendict({"a":1})

# frozendict.update({"b":2}) # NP , AttributeError: 'frozendict' object is read-only
