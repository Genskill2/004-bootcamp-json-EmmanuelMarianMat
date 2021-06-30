# Add the functions in this file
from math import sqrt
import json
def load_journal(filename):
    f = open(filename)
    return json.load(f)

def compute_phi(filename,event):
    list_dict = load_journal(filename)
    n00,n01,n10,n11,n1p,n0p,np1,np0 = 0,0,0,0,0,0,0,0
    for dict in list_dict:
        event_present = event in dict['events']
        if event_present and dict['squirrel']:
            n11+=1
        elif event_present:
            n10+=1
        elif dict['squirrel']:
            n01+=1
        else:
            n00+=1

        if event_present:
            n1p+=1
        else:
            n0p+=1

        if dict['squirrel']:
            np1+=1
        else:
            np0+=1

    return (n11*n00 - n01*n10)/sqrt(n1p*n0p*np1*np0)

def compute_correlations(filename):
    list_dict = load_journal(filename)
    corr_dict = dict()
    for dic in list_dict:
        for event in dic['events']:
            if event not in corr_dict:
                corr_dict[event] = compute_phi(filename,event)
        
    return corr_dict

def diagnose(filename):
    corr_dict = compute_correlations(filename)
    sorted_dict = sorted(corr_dict, key= lambda item: corr_dict[item])
    return (sorted_dict[-1],sorted_dict[0])

diagnose('journal.json')