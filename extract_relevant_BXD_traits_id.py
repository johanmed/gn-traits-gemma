#!/usr/bin/env python

import re

list_keywords=['immune', 'Immune', 'metabolism', 'Metabolism', 'obesity', 'Obesity', 'Microbiome'] # list of keywords related to project

def extract_traits(phenotype_filename, list_keywords):
    """
    Takes phenotype metadata file and list of keywords related to project
    Retrieves trait description and id
    Saves in a dictionary container with an unique key corresponding to full description of trait
    Returns dictionary container
    """
    container={}
    fh=open(phenotype_filename, 'r')
    lines=fh.readlines()
    fh.close()
    for (x, i) in enumerate(lines):
        desc_pattern='^    "Description": '
        contain_desc=re.search(desc_pattern, i)
        if contain_desc:
            next_pos_desc=(contain_desc.span())[-1]
            for j in list_keywords:
                if j in i[next_pos_desc:]:
                    extract=(re.search(r'.*$', i[next_pos_desc:])).group()
                    next_line=lines[x+1]
                    id_pattern='^    "Id": '
                    next_pos_id=(re.search(id_pattern, next_line).span())[-1]
                    id_value=next_line[next_pos_id:]
                    if extract in container:
                        container[extract].append([j, id_value])
                    else:
                        container[extract]=[[j, id_value]]
                        
    return container
    

results_extraction=extract_traits('trait_list_BXDPublish.json', list_keywords)

def save_info(filename, info):
    """
    Takes the filename to save data to and data info
    Open file, if does not exist, creates
    Writes each element of info in a separate line
    """
    fh=open(filename, 'w')
    for element in info:
        val=info[element]
        if val[0][0]=='immune' or val[0][0]=='Immune':
            fh.write(f'{(val[0][-1]).strip()}\tImmune system trait\t{element.strip()}\n')
        elif val[0][0]=='metabolism' or val[0][0]=='Metabolism' or val[0][0]=='obesity' or val[0][0]=='Obesity':
            fh.write(f'{(val[0][-1]).strip()}\tDiabetes trait\t{element.strip()}\n')
        elif val[0][0]=='Microbiome':
            fh.write(f'{(val[0][-1]).strip()}\tGut microbiome trait\t{element.strip()}\n')
    fh.close()
    
save_info('BXD_traits_selected_info.csv', results_extraction)

def retrieve_traits_id(traits_container):
    """
    Takes dictionary containing traits info
    Extracts the trait id
    Adds it to array traits_id_retrieved
    Returns array
    """
    traits_id_retrieved=[]
    for value in traits_container.values():
        traits_id_retrieved.append(value[0][-1])
    
    return traits_id_retrieved
    

list_ids=retrieve_traits_id(results_extraction)
#print(list_ids)
