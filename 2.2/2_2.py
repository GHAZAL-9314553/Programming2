# Good
import xml.etree.ElementTree as ET
from Bio import Entrez
import time
import os
import multiprocessing as mp

def download_reference(reference_id, api_key):
    """
    Download a reference with the specified ID from PubMed.

    Args:
        reference_id (str): The ID of the reference to download.
        api_key (str): The API key for accessing PubMed.

    Prints:
        A message indicating the downloaded reference ID.
    """
    Entrez.email = 'g.s.hosseini.japalagh@st.hanze.nl'  
    handle = Entrez.efetch(db="pubmed", id=reference_id, retmode="xml", api_key=api_key)
    data = handle.read()
    with open(f"{reference_id}.xml", "wb") as f:
        f.write(data)
    print(f"Downloaded reference: {reference_id}")

def main():
    """
    Main entry point of the program.
    """
    # Should not put your api-key in your repo
    api_key = '8fcb0cec66b6442980be82658cb302b39408'
    article_id = '30049270'  # PubMed ID of the article

    try:
        # Obtain the references of the article
        Entrez.email = 'g.s.hosseini.japalagh@st.hanze.nl'
        file = Entrez.elink(dbfrom="pubmed", db="pubmed", LinkName="pubmed_pubmed_refs", id=article_id, api_key=api_key)
        root = ET.parse(file).getroot()
        references = [link.find("Id").text for link in root.iter("Link")]

        # Download the full records of the first ten references using multiprocessing
        with mp.Pool() as pool:
            pool.starmap(download_reference, [(ref_id, api_key) for ref_id in references[:10]])

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    print("Current working directory:", os.getcwd())
