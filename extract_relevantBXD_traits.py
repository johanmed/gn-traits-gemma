#!/usr/bin/env python

import re

list_keywords=['immune', 'Immune', 'metabolism', 'Metabolism', 'obesity', 'Obesity', 'Metagenome, microbiota, gastrointestinal system']

def extract_traits(phenotype_filename, list_keywords):
    """
    
    """
    container={}
    fh=open(phenotype_filename, 'r')
    lines=fh.readlines()
    fh.close()
    for (x, i) in enumerate(lines):
        desc_pattern='^    "Description": '
        contain_desc=re.search(desc_pattern, i)
        if contain_desc:
            next_pos_desc=(contain_desc.span())[-1] + 1
            for j in list_keywords:
                if j in i[next_pos_desc:]:
                    extract=(re.search(r'.*$', i[next_pos_desc:])).group()
                    next_line=lines[x+1]
                    id_pattern='^    "Id": '
                    next_pos_id=(re.search(id_pattern, next_line).span())[-1] + 1
                    id_value=next_line[next_pos_id:]
                    if extract in container:
                        container[extract].append([j, id_value])
                    else:
                        container[extract]=[[j, id_value]]
                        
    return container
    

results_extraction=extract_traits('trait_list_BXDPublish.json', list_keywords)


def retrieve_traits_id(traits_container):
    """
    
    """
    traits_id_retrieved=[]
    for value in traits_container.values():
        traits_id_retrieved.append(value[0][-1])
    
    return traits_id_retrieved
    

list_ids=retrieve_traits_id(results_extraction)
print(len(list_ids))
