# Class Kmer
second homework

## Description
Find common kmers (len=23) of Yersinia pestis easily!

## Usage
**input:** fasta file  
**output:** most common kmers+locus

## Notes
Here: works only with 100.000 n

## Example
**input:** seq[100000:200000]  
**output:**  
kmer: ATGAGTGGCGTTGACCGGTAAGC  
locus_list: [25065, 25178, 25291, 25404]  
Details:  
chrom_name: AE009952.1 locus: 25065  
chrom_name: AE009952.1 locus: 25178  
chrom_name: AE009952.1 locus: 25291  
chrom_name: AE009952.1 locus: 25404  

kmer: TGAGTGGCGTTGACCGGTAAGCC  
locus_list: [25066, 25179, 25292, 25405]  
Details:  
chrom_name: AE009952.1 locus: 25066  
chrom_name: AE009952.1 locus: 25179  
chrom_name: AE009952.1 locus: 25292  
chrom_name: AE009952.1 locus: 25405  
 
kmer: GAGTGGCGTTGACCGGTAAGCCG   
locus_list: [25067, 25180, 25293, 25406]    
Details:  
chrom_name: AE009952.1 locus: 25067  
chrom_name: AE009952.1 locus: 25180  
chrom_name: AE009952.1 locus: 25293  
chrom_name: AE009952.1 locus: 25406  

kmer: AGTGGCGTTGACCGGTAAGCCGC      
locus_list: [25068, 25181, 25294, 25407]        
Details:   
chrom_name: AE009952.1 locus: 25068   
chrom_name: AE009952.1 locus: 25181    
chrom_name: AE009952.1 locus: 25294    
chrom_name: AE009952.1 locus: 25407    

kmer: GTGGCGTTGACCGGTAAGCCGCT  
locus_list: [25069, 25182, 25295, 25408]  
Details:  
chrom_name: AE009952.1 locus: 25069  
chrom_name: AE009952.1 locus: 25182  
chrom_name: AE009952.1 locus: 25295  
chrom_name: AE009952.1 locus: 25408  

kmer: TGGCGTTGACCGGTAAGCCGCTT  
locus_list: [25070, 25183, 25296, 25409]      
Details:  
chrom_name: AE009952.1 locus: 25070  
chrom_name: AE009952.1 locus: 25183  
chrom_name: AE009952.1 locus: 25296  
chrom_name: AE009952.1 locus: 25409  

kmer: GGCGTTGACCGGTAAGCCGCTTT  
locus_list: [25071, 25184, 25297, 25410]  
Details:  
chrom_name: AE009952.1 locus: 25071  
chrom_name: AE009952.1 locus: 25184  
chrom_name: AE009952.1 locus: 25297  
chrom_name: AE009952.1 locus: 25410  

kmer: GCGTTGACCGGTAAGCCGCTTTC  
locus_list: [25072, 25185, 25298, 25411]  
Details:  
chrom_name: AE009952.1 locus: 25072  
chrom_name: AE009952.1 locus: 25185  
chrom_name: AE009952.1 locus: 25298  
chrom_name: AE009952.1 locus: 25411  

kmer: CGTTGACCGGTAAGCCGCTTTCT    
locus_list: [25073, 25186, 25299, 25412]    
Details:    
chrom_name: AE009952.1 locus: 25073    
chrom_name: AE009952.1 locus: 25186    
chrom_name: AE009952.1 locus: 25299    
chrom_name: AE009952.1 locus: 25412    

kmer: GTTGACCGGTAAGCCGCTTTCTT  
locus_list: [25074, 25187, 25300, 25413]  
Details:  
chrom_name: AE009952.1 locus: 25074  
chrom_name: AE009952.1 locus: 25187  
chrom_name: AE009952.1 locus: 25300  
chrom_name: AE009952.1 locus: 25413  

kmer: TTGACCGGTAAGCCGCTTTCTTT  
locus_list: [25075, 25188, 25301, 25414]  
Details:  
chrom_name: AE009952.1 locus: 25075  
chrom_name: AE009952.1 locus: 25188  
chrom_name: AE009952.1 locus: 25301  
chrom_name: AE009952.1 locus: 25414  

kmer: TGACCGGTAAGCCGCTTTCTTTT  
locus_list: [25076, 25189, 25302, 25415]  
Details:  
chrom_name: AE009952.1 locus: 25076  
chrom_name: AE009952.1 locus: 25189   
chrom_name: AE009952.1 locus: 25302  
chrom_name: AE009952.1 locus: 25415    

....etc...

## Authors
Lisa Skalon

  
