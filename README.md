# demultiplex

1) You must conitn a folder with sam_R1.fastq, sam_R2.fastq and mapping.txt files solely.
2) Change the "input_path" variable insie main.py to the location of the work folder
3) excute main.py


This will separeta reads from sam_R1.fastq and sam_R2.fastq in diferents files by barcode.
The finall output will be in the FullDemux forlder.

The barcodes must be provides in a tabs separated file call "mapping.txt", like this:

SampleID	BarcodeSequence
planta.1a	CGTAACCA
planta.1d	CGTAAGAA
planta.4b	CGTACCCA
planta.4d	CGTAGATA
yucra.1a	CGTAGGCT
yucra.1b	CGTATTCA
yucra.4a	CGTATTTC
yucra.4b	CGTCAAGA
yucra.7a	CGTCACAG
yucra.7b	CGTCCAGG
ref.3	CGTCGCAT
ref.4	CGTCTGAA
sev1	CGTGAGAC
sev2	CGTGATAA
prep1	CGTGGGAC
prep2	CGTGGTCA

It must has the example columns name "SampleID" and "BarcodeSequence". You can incluide another columns.
