# demultiplex

1) You must contain  sam_R1.fastq, sam_R2.fastq and mapping.txt files solely in a work folder.
2) Excute main.py with the path of the work folder as fisrt argument (i.e.: python main.py path).

The barcodes must be provides in a tab separated file call "mapping.txt", like this [mapping_file.txt](https://github.com/AgustinPardo/demultiplex/tree/master/example).
It must has the columns name "SampleID" and "BarcodeSequence", and two more colums to identified the files separated by barcode. You cannot leave that colums in blank.

**Result:**
+ Separate reads from sam_R1.fastq and sam_R2.fastq in diferents files by barcode. Only exact matches are taken into account. The finall output will be in the FullDemux folder. The ids of the other columns will be joined forming the name of each file.
+ Create reads_counts.txt file in the work folder contaning the reads counts of every file demultiplexed by barcode, the read counts of the sam files, and the percentage of reads lost in the process.


**Software used publications:**

[Vignale, F.A., Bernal Rey, D., Pardo, A.M. et al. Spatial and Seasonal Variations in the Bacterial Community of an Anthropogenic Impacted Urban Stream. Microb Ecol 85, 862–874 (2023). https://doi.org/10.1007/s00248-022-02055-z](https://www.google.com](https://link.springer.com/article/10.1007/s00248-022-02055-z)https://link.springer.com/article/10.1007/s00248-022-02055-z)

[Raiger Iustman, L.J., Almasqué, F.J. & Vullo, D.L. Microbiota Diversity Change as Quality Indicator of Soils Exposed to Intensive Periurban Agriculture. Curr Microbiol 78, 338–346 (2021). https://doi.org/10.1007/s00284-020-02298-4](https://link.springer.com/article/10.1007/s00284-020-02298-4)
