
======================
GUIDE ON DATA ANALYSIS
======================

.. contents::
.. sectnum::

This document provides a summary of the analysis which can be performed in |plasmogen|.

SAMPLE PROCESSING
-----------------

The steps in the sample processing are performed to obtain sample sets with the corresponding allele/genotype data suitable for further analysis.

1. Sample selection and grouping by differentiation

   |plasmogen| starts by creating initial sample sets based on the user query setting.
   It collects samples from the database according to the metadata selection and then groups these samples according to the differentiation setting.

2. Allele selection and filtering

   Binned alleles from corresponding markers for each sample in the sample sets are collected and filtered based on the rfu absolute and relative threshold, relative cut-off, stutter ratio and stutter range.

3. Sample quality filtering

   Based on the collected alleles from the previous step, each sample is assessed by the number of genotyping fails.
   Samples with less than the required number of expected genotyping successes are dropped from the sample set.

4. Marker quality filtering

   From the remaining samples in each sample set, markers are then assessed by the number of genotyped samples for each corresponding markers.
   Markers with less than the required number of successful genotyped samples are dropped, and the corresponding alleles are also dropped from the whole sample sets.

5. Sample characteristics filtering

   If users set an option for further sample filtering, the filtering process is performed on the remaining samples and markers in each sample sets.
   For monoclonal samples setting, |plasmogen| will drop any samples that have multiple alleles in any of each marker.
   For strict/low-complexity samples setting, samples with multiple alleles in more than one marker will be dropped from sample sets.
   For unique genotype samples setting, consecutive samples with identical MLGs within a particular sample set will be dropped, as well as samples without complete MLGs.

6. Filtered sample sets

   Each sample set now has the remaining samples in each sample set with filtered markers and ready for use in the analysis.


DATA ANALYSIS
-------------

The following tools are suitable for simple descriptive statistics to provide overall summaries of the sample sets.
Purposes of these tools include, but not limited to, background checks on the sample metadata, overall summary of alleles and markers, and allele quality controls which may aid in the data editing/data annotation.


Sample summary
++++++++++++++

This tool provides metadata summaries on samples.

Allele summary
++++++++++++++

This tool provides summaries of the alelles in each sample set such as the number of unique alleles, the number of total genotyped alleles, the frequency of each allele and the quality of the allele binning.

Genotype summary
++++++++++++++++

This tool is useful to observe samples in the given sample sets with their respective alleles within haplotype setting (each row represent a sample).
Genotype summary may aid in data editing/data annotation as each allele of a particular samples can be inspected manually by observing its FSA trace.


POPULATION GENETICS ANALYSIS
----------------------------

Depending on the type of analysis, either *all alleles*, *predominant alleles* or *multi-locus genotypes* (MLG - major alleles for all locus) samples were used.
Some analyses use the predominant alleles to ensure an unbiased estimate of the minor allele frequency.
Other analyses use MLG samples and discard the non-MLG samples as those analyses can only be performed on the haplotype bases.

It is advised that only day-0 population samples (i.e. non-recurrent samples) are included for the population genetics analysis, unless there are specific needs to do otherwise.
A minimal threshold of 30 samples for each sample set is generally advised for population genetic studies.
Caution is therefore advised in the interpretation of results derived from sample sets with lower sample size.

Multiplicity of Infection (MoI)
+++++++++++++++++++++++++++++++

This tool reports on the statistics for Multiplicity of Infection analysis, such as the number of polyclonal samples, the polyclonality of samples and markers, as well as the statistics to test the significance of the differences between each sample sets in regard to their polyclonality.

A sample is defined as polyclonal if any of its loci has more than one allele.
The MOI in each sample is defined by the maximum number of alleles observed at any n markers tested.
The MOI provides a lower bound estimate of the number of genetically distinct parasite clones within a sample.

This tool uses all available alleles of each sample.

Expected Heterozygosity
+++++++++++++++++++++++

Expected heterozygosity (HE) provides a measure of population diversity at a given marker or averaged across a range of markers for a given sample set.
The expected heterozygosity for each marker is calculated using the equation given below, where *pi* is the frequency of the *i* th of *k* alleles.

.. math::

  He =  \frac{n}{n-1} (1 - \sum_{i=1}^{k} p_i^2)

Values range from 0 (no diversity) to nearly 1 (large number of equally frequent alleles).
Only the predominant allele at each marker in each sample is used for this analysis.

Linkage Disequilibrium (LD)
+++++++++++++++++++++++++++

Multi-locus linkage disequilibrium (LD) is assessed by the standardised index of association (ISA) using LIAN 3.5 software [4].
Testing the null hypothesis of linkage equilibrium, the significance of the ISA estimates is assessed using 100,000 random permutations of the data.

Comparing LDs between all samples, low-complexity samples and unique haplotype samples in a given sample sets enables identification of potential clonal expansions, whereby the ISA is expected to drop substantially in the unique haplotype samples relative to the all (full) samples.

This tools uses MLG samples (haplotype data).

COMPARATIVE POPULATION GENETICS ANALYSIS
----------------------------------------

FST
+++

FST calculation is performed by Arlequin software.
|plasmogen| calculates FST, the *FSTmax* which uses recoded alleles so that each allele was only spesific only for its respective sample set, and the *FSTstd* or standardized FST which is obtained by dividing FST with FTSmax (FST / FSTmax).

This tools uses MLG samples (haplotype data).


Jost's D Index
++++++++++++++

Jost's D-index is similar to FST.
|plasmogen| uses DEMEtics library from R statistical suite to perform this analysis.

This tools uses MLG samples (haplotype data).


Principal Coordinate Analysis (PCoA)
++++++++++++++++++++++++++++++++++++

Principal Coordinate Analysis (PCoA) is a method to generate cluster plots, which are useful to inspect the relatedness (or allele similarity) amongst each sample.
The method works by first generating a genetic distance matrix, and then performs PCA (Principal Component Analysis) on the distance matrix.
The genetic distance between 2 samples is defined as the proportion of the differing alleles from the haplotypes of both samples.

This tools uses MLG samples (haplotype data).

Multiple Correspondence Analysis (MCA)
++++++++++++++++++++++++++++++++++++++

Multiple Correspondence Analysis (MCA) is another method to generate cluster plots, similar to PCoA.
While PCoA uses genetic distance matrix, MCA uses the allele data directly and treats each allele as a discrete (categorical/nominal) data. Put in simple terms, MCA is to qualitative data, as PCoA is to quantitative data.
|plasmogen| employes FactoMineR library from the R statistical software for calculating MCA.

This tools uses MLG samples (haplotype data).

Neighbor Joining
++++++++++++++++

The neighbor-joining tree is constructed from the same genetic distance matrix used in the PCoA analysis.
APE library from R statistical suite is used to generate and plot the phylogenetic tree.

This tools uses MLG samples (haplotype data).


.. |plasmogen| replace:: VivaxGEN
