# Programming2
The purpose of this assignment is to use Dask Dataframes to read, manipulate, summarize, and analyze a large dataset of protein annotation information obtained from the InterProScan protein annotation service. The dataset contains approximately 4,200,000 protein annotations and is around 11GB in size. The goal is to write a script that performs various analyses on the dataset using Dask Dataframes. Here is a summary of the questions to be answered:

1. How many distinct protein annotations (InterPRO numbers) are found in the dataset?
2. What is the average number of annotations per protein?
3. What is the most common GO Term found in the dataset?
4. What is the average size of an InterPRO feature found in the dataset?
5. What are the top 10 most common InterPRO features?
6. Among the InterPRO features that are almost the same size as the protein itself (within 90-100%), what are the top 10 features?
7. Among the selected features with textual annotation, what are the top 10 most common words found?
8. Among the selected features with textual annotation, what are the top 10 least common words found?
9. Combining the answers for questions 6 and 7, what are the 10 most common words found for the largest InterPRO features?
10. What is the coefficient of correlation between the size of the protein and the number of features found?

The assignment aims to demonstrate the use of Dask Dataframe interface to efficiently process and analyze the large dataset of protein annotations. It is recommended to work on the dataset directly on the server without downloading it to a local machine. The script should be developed in the `/commons/conda` environment and utilize a maximum of 16 threads for computation.
