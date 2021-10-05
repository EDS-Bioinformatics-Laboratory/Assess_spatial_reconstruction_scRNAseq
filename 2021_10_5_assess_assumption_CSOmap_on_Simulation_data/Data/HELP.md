# Directory: Data

Description: this directory contains data used in the project. 

Notes:

* Rename 'NameOfDataset_1' to a more descriptive name.

* The Data directory is also found in the Processing directory, and in specific analysis directories (i.e., currently yyyymmdd_NameOfDataAnalysis). You can use either one or all of these directories based on what you find convenient.

* In case you only have one dataset then you are allowed to remove the intermediate \Data layer and move the dataset directory one directory up. For example, yyyymmdd_ProjectName\Affymetrix_WTmouse or \Processing\Affymetrix_WTmouse

  instead of 

  yyyymmdd_ProjectName\Data\Affymetrix_WTmouse or \Processing\Data\Affymetrix_WTmouse

* If you use multiple datasets then still use intermediate \Data layer. 



The Data directory includes:

* Raw data

  *  **Raw data comprise the files that come from the machine** 
  *  Unprocessed data obtained from collaborators or public databases. 
  *  e.g., fastq for NGS, 'raw' for metabolomics

* Meta data (data about data)

  * **Meta data is a description of the data**
  * Description of the data obtained from collaborators
    * Description of samples (e.g., sample sheets)
    * Experimental design
    * Who created the data
    * What the data file contains
    * When the data were generated
    * Where the data were generated
    * Why the data were generated
    * How the data were generated
    * ........

* Processed data

  * Data that is normalized, summarized, or pre-processed in any other way.
  * This directory should contained the data resulting from the very initial pre-processing steps and which is used for all subsequent downstream processing and analyses (e.g., BAM for NGS, first peak table for metabolomics). All other (pre)processed data can either be placed in Processed or in a Results directory but it should be logical, structured, and documented.


<u>Note:</u> 

1. The meta-data is generally received from our collaborators.
2. If public data is used then specify sufficient information such as Database name, version, URL, description of the data. 
3. It is not necessary to use (meta-)data standards such as minimum information standards, FAIR, vocabularies/ontologies. We assume that we receive all data in proper formats from our collaborators or, otherwise, use the file formats that we received.





