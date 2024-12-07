import json
import os
from typing import Tuple
import pandas as pd
import re
from tqdm import tqdm

import paperscraper

def get_site(bibtex: str) -> str:
    match = re.search(r"booktitle\s*=\s*\{([^}]*)\}", bibtex)
    if match:
        return match.group(1)
    else:
        return ""
    
def delete_paper(key: str) -> bool:
    try:
        os.remove(key)
        return True
    except FileNotFoundError:
        return False


def delete_old_files(papers, range: tuple = (2023, 2024)) -> Tuple[int, list[str]]:
    aumount_deleted = 0
    id_to_delete = []
    for key, value in tqdm(papers.items(), desc="Deleting old papers"):
        if int(value['year']) < range[0] or int(value['year']) > range[1]:
            if delete_paper(key):
                aumount_deleted += 1
                # delete the paper from the papers dictionary
                id_to_delete.append(key)

    return aumount_deleted, id_to_delete

def generate_dataframe(papers, db: str = None) -> Tuple[pd.DataFrame, int]:

    if db and os.path.exists(db):
        df = pd.read_excel(db)
    else:
        df = pd.DataFrame(
            columns=['doi', 'title', 'citationCount', 'site', 'bibtex', 'year', 'url']
        )

    amount_deleted = 0
    for key, value in tqdm(papers.items(), desc="Generating db"):
        #if doi is already in the db, skip
        list_of_dois = df['doi'].tolist()
        if not value['doi'] in list_of_dois:
            next_row = pd.DataFrame(
                {
                    'doi': value['doi'] if value['doi'] else value['title'], 
                    'title': value['title'], 
                    'citationCount': value['citationCount'], 
                    'site': get_site(value['bibtex']),
                    'bibtex': value['bibtex'],
                    'year': value['year'], 
                    'url': value['url']
                }, index=[0])
            df = pd.concat([df, next_row], ignore_index=True)
        else:
            if delete_paper(key):
                amount_deleted += 1

    df = df.sort_values(by='citationCount', ascending=False)
    return df, amount_deleted 

def search_papers(query, limit=10, pdir='papers'):
    papers = paperscraper.search_papers(query, limit=limit, pdir=pdir)
    return papers

def save_db_of_papers(papers: pd.DataFrame, filename: str):
    papers.to_excel(filename, index=False)

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


