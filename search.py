import os
import argparse
from constants import MASTER_FOLDER, DB_NAME
from utils import create_folder, delete_old_files, generate_dataframe, save_db_of_papers, search_papers

def parse_arguments():
    """
    Parses command-line arguments for the script.
    """
    parser = argparse.ArgumentParser(description="Process papers based on query and filters.")
    parser.add_argument("--folder", type=str, required=True,
                        help="Folder name to save results.")
    parser.add_argument("--query", type=str, required=True,
                        help="Search query for papers.")
    parser.add_argument("--amount", type=int, default=30,
                        help="Number of papers to retrieve.")
    parser.add_argument("--start_year", type=int, default=2022,
                        help="Start year for filtering papers.")
    parser.add_argument("--end_year", type=int, default=2025,
                        help="End year for filtering papers.")
    return parser.parse_args()

def perform_search(query, amount, folder):
    """
    Performs the search for papers and saves the results in a folder.
    """
    create_folder(MASTER_FOLDER)
    file_to_save = os.path.join(MASTER_FOLDER, folder)
    papers = search_papers(query, limit=amount, pdir=file_to_save)
    print(f"Found {len(papers)} papers")
    return papers, file_to_save

def filter_papers(papers, start_year, end_year):
    """
    Filters papers by removing those outside the specified year range.
    """
    amount_deleted, list_of_papers_to_delete = delete_old_files(
        papers,
        range=(start_year, end_year)
    )
    print(f"Deleted {amount_deleted} papers outside the range {start_year}-{end_year}")
    return {key: value for key, value in papers.items() if key not in list_of_papers_to_delete}

def generate_and_save_db(papers, folder, db_name):
    """
    Generates a DataFrame from the papers and saves it to a file.
    """
    file_of_db = os.path.join(folder, db_name)
    df, amount_deleted = generate_dataframe(papers, db=file_of_db)
    print(f"Deleted {amount_deleted} papers already in the database")
    save_db_of_papers(df, file_of_db)
    print(f"Database saved at {file_of_db}")

def main():
    args = parse_arguments()

    # Perform the paper search
    papers, file_to_save = perform_search(args.query, args.amount, args.folder)
    
    # Filter papers by year range
    papers = filter_papers(papers, args.start_year, args.end_year)
    
    # Generate and save the database
    generate_and_save_db(papers, file_to_save, DB_NAME)

if __name__ == '__main__':
    main()


