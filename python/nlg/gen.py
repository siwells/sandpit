from random import choice

grammar = dict(
        S = [['NP','VP']],
        NP = [['Art', 'N']],
        VP = [['V', 'NP']],
        Art = ['the', 'a'],
        N = ['man', 'ball', 'woman', 'table'],
        V = ['hit', 'took', 'saw', 'liked']
        )

def generate(phrase):
    "Generate a random sentence or phrase"
    if isinstance(phrase, list): 
        return mappend(generate, phrase)
    elif phrase in grammar:
        return generate(choice(grammar[phrase]))
    else: return [phrase]
    
def generate_tree(phrase):
    """Generate a random sentence or phrase,
     with a complete parse tree."""
    if isinstance(phrase, list): 
        return map(generate_tree, phrase)
    elif phrase in grammar:
        return [phrase] + generate_tree(choice(grammar[phrase]))
    else: return [phrase]

def mappend(fn, args):
    "Map function over the args; append results." 
    return [item for result in map(fn, args) 
                 for item in result]

if __name__ == "__main__":
    print(' '.join(generate('S')))
#    print(generate_tree('S'))
