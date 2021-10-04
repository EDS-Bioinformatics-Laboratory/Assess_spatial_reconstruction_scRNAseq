# Directory: Processing

Description:

This directory should all data analyses and results. Its sub-directories include:

* Data (raw, meta, preprocessed)
  * The Processing directory contains a directory Data to hold any data used by software in the different data analysis directories. Alternatively, the Data directory within DataAnalyses can be used to hold data produced as part of the data analyses or simulations, and which is used only for one specific analysis. Note: the Data directory in the main directory (yyyymmdd_ProjectName/Data) may be also be used if this is more convenient.
* Code
  * Any software (e.g., R, Python, C) 
  * Software/scripts to generate the main figures and summary tables from Results/SummaryTables should always be separate from the software that performs the actual data analysis. This excludes (in most case), for example, quality plots from fastqc.
    * e.g., DataAnalysis_script --> results (csv/tab delim files) --> Figure_script --> Figures
    * e.g., DataAnalysis_script --> results (csv/tab delim files) --> table_script --> SummaryTabls
  * Software documentation
* Documentation
  * This should contain documentation about a specific analysis and/or the software
* NoteBooks
  * (e.g, R markdown, Jupyter)
* Results
  * All results from a data analysis
* Settings
  * External configuration or parameter files

<u>Note:</u> 

2. The Processing directory should be pushed to its corresponding GitHub repository without data and results because we do not have the storage space on github to accommodate this. 
3. The Processing directory should contain a <u>github.txt</u> file with at least the name of  the associated GitHub repository (URL)
4. The Processing and/or DataAnalyses directories should contain a <u>.gitignore</u> file to exclude data, results, etc from GitHub. Only code (and relevant code documentation) should be synchronized with GitHub. Note. The gitignore-template.txt should be adjusted and renamed to .gitignore

