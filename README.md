# demultiplex

1) You must contain  sam_R1.fastq, sam_R2.fastq and mapping.txt files solely in a work folder.
2) Excute main.py with the path of the work folder as fisrt argument (i.e.: python main.py path).

The barcodes must be provides in a tab separated file call "mapping.txt", like this [mapping_file_example.txt](https://github.com/AgustinPardo/demultiplex/tree/master/example).
It must has the columns name "SampleID" and "BarcodeSequence", and two more colums to identified the files separated by barcode. You cannot leave that colums in blank.

**Result:**
+ Separate reads from sam_R1.fastq and sam_R2.fastq in diferents files by barcode. Only exact matches are taken into account. The finall output will be in the FullDemux folder. The ids of the other columns will be joined forming the name of each file.
+ Create reads_counts.txt file in the work folder contaning the reads counts of every file demultiplexed by barcode, the read counts of the sam files, and the percentage of reads lost in the process.


