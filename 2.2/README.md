# Programming2
The purpose of this assignment is to explore parallelization using Python's multiprocessing module and apply it to the task of harvesting and downloading article references from the National Center for Biotechnology Information (NCBI) using the Biopython package. Here's a summary of each step:

Step 0: Obtaining an API key
- Guide the user through obtaining an API key from the NCBI for automatic article downloading.

Step 1: Install and use the Biopython package
- Install the Biopython package using pip.
- Use the Entrez class from Biopython to query the NCBI databases and retrieve article information.
- Set up the email address used to create the API key.
- Demonstrate how to query the PubMed database and obtain article information and references.

Step 2: Download the referenced articles
- Use the Entrez class to obtain the references of an article using its PubMed ID.
- Download the full record of the first ten references in XML format.
- Save each downloaded record as a separate file with the reference ID as the filename and the ".xml" extension.
- Use the multiprocessing module to parallelize the download process, distributing the task across multiple cores for increased performance.

Extra challenge:
- Optional challenge to perform the same exercise without using the multiprocessing module.
- Measure and compare the execution time of both versions to observe the difference in performance.

The overall purpose of this assignment is to introduce the concept of parallelization and demonstrate its benefits in terms of performance improvement when dealing with time-consuming tasks such as harvesting and downloading large amounts of data.
