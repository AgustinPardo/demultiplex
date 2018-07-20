# demultiplex

1) You must conitn a folder with sam_R1.fastq, sam_R2.fastq and mapping.txt files solely.
2) Change the "input_path" variable insie main.py to the location of the work folder
3) excute main.py


This will separeta reads from sam_R1.fastq and sam_R2.fastq in diferents files by barcode.
The finall output will be in the FullDemux forlder.

The barcodes must be provides in a tabs separated file call "mapping.txt", like this:

|SampleID|BarcodeSequence|
|-------------|-------------|
|planta.1a|CGTAACCA|
|planta.1d|CGTAAGAA|
|ref.3|CGTCGCAT|
|sev1|CGTGAGAC|
|prep1|CGTGGGAC|

It must has the example columns name "SampleID" and "BarcodeSequence". You can incluide another columns.
