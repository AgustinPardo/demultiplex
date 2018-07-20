# demultiplex

1) You must conitn a folder with sam_R1.fastq, sam_R2.fastq and mapping.txt files solely.
2) Change the "input_path" variable insie main.py to the location of the work folder
3) Excute main.py


This will separeta reads from sam_R1.fastq and sam_R2.fastq in diferents files by barcode.
The finall output will be in the FullDemux forlder.

The barcodes must be provides in a tab separated file call "mapping.txt", like this [mapping_file_example.txt].(https://github.com/AgustinPardo/demultiplex/tree/master/example)
It must has the example columns name "SampleID" and "BarcodeSequence". You can incluide another columns.
