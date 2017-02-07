import re
def match(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    matches = []
    for word in words:
        if re.search(regex,word):
            matches.append(word)
    print matches
    return matches
match(r'v')
match(r'ss')
match(r'e$')
match(r'b*b')
match(r'b.b')
match(r'b+b')
match(r'a[^e]*e[^i]*i[^o]*o[^u]*u')
match(r'^(?=.*r)(?=.*e)(?=.*g)(?=.*u)(?=.*l)(?=.*a)(?=.*r)(?=.*x)(?=.*p)(?=.*r)(?=.*s)(?=.*i)(?=.*o)(?=.*n)')
match(r"(.)\1")
