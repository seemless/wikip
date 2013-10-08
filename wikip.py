import sys
import wikipedia

def suggest_entry(entry):
    '''return a suggested entry in {'data':entry}.
If page not found, {'err': error} is populated.'''   
    ret = {}
    try:
        ret['data'] = {'summary': wikipedia.summary(entry)}
    except wikipedia.PageError as e:
        ret['err'] = 'keyword not found. Try another.'

    return ret

if __name__=="__main__":
    args = sys.argv[1:]
    print suggest_entry(args[0])
