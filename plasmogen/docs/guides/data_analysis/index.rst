
======================
GUIDE ON DATA ANALYSIS
======================

.. contents::


This document provides a summary of the analyses which can be performed in |plasmogen|.

SAMPLE PROCESSING
-----------------

The sample processing steps enable the user to select **genotype data** for specific **sample sets** and **marker sets**, and to define if/how the samples should be grouped in downstream analyses.

1. Sample selection and grouping

   The platform creates a sample set based on the user query settings by identifying samples in the database with metadata values concordant with the user selection criteria.
   The samples are then assigned to groups according to the user-defined differentiation settings.
   Using the user-defined marker set, the platform identifies the corresponding genotype data for each sample in the sample set, and differentiates the genotype data in accordance with the sample differentiation settings.

2. Allele selection and filtering

   The platform collects all binned alleles (i.e. called alleles) at the user-defined markers for each sample in the user-defined sample set, and then filters out all alleles that do not meet the user-defined allele absolute threshold, allele relative threshold, allele relative cut-off, stutter ratio and stutter range.

3. Sample quality filtering

   Using the allele-filtered data set the platform determines the  proportion of genotyping fails (i.e. proportion of markers with no binned alleles) for each sample.
   Samples with less than the user-defined proportion of successfully genotyped markers (**Sample quality threshold**) are filtered out of the sample and corresponding genotype data sets.

4. Marker quality filtering

   Using the sample quality-filtered samples and corresponding genotype data sets, the platform determines the proportion of genotyping fails for each marker.
   Markers with less than the user-defined proportion of successfully genotyped samples (**Marker quality threshold**) are filtered out of the marker and corresponding genotype data sets.

5. Sample characteristics filtering

   Additional user-defined sample filtering options are performed on the data sets remaining after step 4 (i.e. on the sample and marker quality-filtered data sets).
   Additional sample filtering options include selection of monoclonal samples only.
   For the monoclonal sample setting, the platform identifies all samples with multiple alleles at one or more of the given markers, and subsequently filters out these samples and their corresponding genotype data.
   Another sample filtering option is the selection of strict/low-complexity samples.
   For the strict/low-complexity sample setting, the platform identifies all samples with multiple alleles at two or more one of the given markers, and subsequently filters out these samples and their corresponding genotype data.
   A further sample filtering option is the selection of unique genotype samples.
   For the unique genotypes sample setting, the platform identifies and excludes samples with incomplete multi-locus genotypes (MLGs) and then identifies and excludes consecutive samples with identical MLGs and their corresponding genotype data.

6. Filtered sample sets

   After step 5, the genotype data is ready to be analysed.

DATA SUMMARIES
--------------

The following tools provide simple descriptive statistics of a given data set.
Utilities of these tools include, but are not limited to, background checks on the sample metadata, and allele and marker summaries, which can be a useful aid in data editing/data annotation.


Sample summary
++++++++++++++

This tool provides metadata summaries on a given sample set.
The summary includes the number of samples which have

Allele summary
++++++++++++++

This tool provides summaries of the alleles in a given  data set, including the number of unique alleles, the number and frequency of successful genotype calls for each allele, and the quality of the allele binning.

Genotype summary
++++++++++++++++

This tool provides an overview of the allele calls in a given data set with the data organized with samples in rows and markers in columns.
Where a given sample/marker combination has multiple alleles, each allele is presented in a separate row, with alleles ordered by peak intensity, whereby the predominant allele (highest intensity peak) is on the top row.
The genotype summary is a useful aid in data editing/data annotation: the FSA trace for an allele can be easily accessed from this view by simply clicking on the allele of interest.

POPULATION GENETIC ANALYSES
----------------------------

Depending on the analytical procedure, the platform will either use *all alleles*, *predominant alleles* or *MLGs* (*multi-locus genotypes* comprising the predominant alleles at each locus in samples with complete data only).
Several analyses are restricted to the predominant alleles to ensure an unbiased estimate of the minor allele frequency [Anderson2000]_.
Analyses requiring complete data, such as those entailing the construction of distance matrices, are restricted to MLGs.

To avoid potential bias in allele frequency estimates resulting from the inclusion of samples that are not independent, such as pairs of day-0 and recurrent samples, it is advisable to restrict population genetic analyses to day-0/independent samples (defined as “population samples” in |plasmogen|).


Multiplicity of Infection (MoI)
+++++++++++++++++++++++++++++++

This tool provides statistics on Multiplicity of Infection and the proportion of polyclonal samples by sample group and by marker.
Statistics on the significance of the differences between sample groups are provided for the proportion of polyclonal samples.

A sample is defined as polyclonal if any of the given markers have more than one allele.
The MOI in each sample is defined by the maximum number of alleles observed at any of the given markers.
The MOI provides a lower bound estimate of the number of genetically distinct parasite clones within a sample.

This tool uses all available alleles in each sample.

Expected Heterozygosity
+++++++++++++++++++++++

Expected heterozygosity (HE) provides a measure of population diversity at a given marker or averaged across a range of markers for a given sample set.
The expected heterozygosity for each marker is calculated using the equation given below, where *pi* is the frequency of the *i* th of *k* alleles.

.. math::

  H_E =  (\frac{n}{n-1}) (1 - \sum_{i=1}^{k} p_i^2)

Values range from 0 (no diversity) to nearly 1 (large number of equally frequent alleles).
Only the predominant allele at each marker in each sample is used for this analysis.

Linkage Disequilibrium (LD)
+++++++++++++++++++++++++++

Multi-locus linkage disequilibrium (LD) is assessed by the standardised index of association (|ISA|) using LIAN 3.5 software [Haubold2000]_.
Testing the null hypothesis of linkage equilibrium, the significance of the (|ISA|) estimates is assessed using 100,000 random permutations of the data.

Using the additional sample filtering options described in section 1.5, users can derive LD estimates for all samples, strict/low-complexity samples and unique genotypes in a given sample sets.
Comparison of the results aids the detection  of any recent clonal expansions, whereby the IAS is expected to drop substantially in the unique genotypes relative to the full (all) sample set.

This tool uses MLG samples (requires complete data).

COMPARATIVE POPULATION GENETIC ANALYSES
---------------------------------------

Genetic Differentiation using the Fixation Index (|FST|)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This tool measures the genetic differentiation between sample groups using pairwise measures of the fixation index (|FST|), using Arlequin software version 3.5.5.2 [Excoffier2010]_.
In addition to the classic |FST|, |plasmogen| calculates a standardized measure of the genetic differentiation (|FsST|), which adjusts for high marker diversity [Hedrick2005]_.
The |FsST| provides a measure of |FST| expressed as a fraction of the maximum possible value of this statistic, whereby 

.. math::

    F'_{ST} = \frac{F_{ST}}{F_{STmax}}

:math:`F_{STmax}` is calculated by recoding the data to obtain the maximum divergence among populations.

This tools uses MLG samples.


Jost's D Index
++++++++++++++

This tool measures the genetic differentiation between sample groups using Jost's D index.
Jost's D index incorporates normalization of the genetic data by heterozygosity, thus providing adjustment for high marker diversity [Jost2008]_.
VivaxGEN uses the DEMEtics library from the R statistical suite to perform this analysis.

This tools uses MLG samples


Principal Coordinate Analysis (PCoA)
++++++++++++++++++++++++++++++++++++

Principal Coordinate Analysis (PCoA) is a method to generate cluster plots, which are useful to inspect the relatedness (or allele similarity) between samples.
The method works by first generating a genetic distance matrix, and then performing PCA (Principal Component Analysis) on the distance matrix.
The genetic distance between any two samples is defined as the proportion of differing alleles between their MLGs.

This tools uses MLG samples.


Multiple Correspondence Analysis (MCA)
++++++++++++++++++++++++++++++++++++++

Multiple Correspondence Analysis (MCA) is another method to generate cluster plots, similar to PCoA.
While PCoA uses a genetic distance matrix to measure the genetic distance between samples, MCA uses the allele data directly and treats each allele as a discrete (categorical/nominal) data point.
Put in simple terms, MCA is to qualitative data, as PCoA is to quantitative data.

|plasmogen| employs the FactoMineR library from the R statistical software to perform the MCA [Le2008]_.

This tools uses MLG samples.

Neighbor-Joining Analysis
+++++++++++++++++++++++++

This tool generates neighbor-joining trees, constructed from the same genetic distance matrix used in the PCoA analysis.
|plasmogen| employs the APE library from the R statistical suite to generate and plot the neighbour-joining tree [Paradis2004]_.

This tools uses MLG samples.


.. |plasmogen| replace:: VivaxGEN


.. |ISA| replace:: :math:`I_A^s`
.. |FST| replace:: :math:`F_{ST}`
.. |FsST| replace:: :math:`F'_{ST}`


.. [Anderson2000] Anderson TJ, et. al. 2000. Microsatellite markers reveals a spectrum of population structures in the malaria parasite Plasmodium falciparum. *Mol Biol Evol* - `PUBMED:11018154 <http://www.ncbi.nlm.nih.gov/pubmed/11018154>`_
.. [Excoffier2010] Excoffier L, Lischer HEL. 2010. Arlequin suite ver 3.5: A new series of programs to perform population genetics analysis under Linux and Windows. *Mol Ecol Resour* - `PUBMED:21565059 <http://www.ncbi.nlm.nih.gov/pubmed/21565059>`_
.. [Haubold2000] Haubold B, Hudson RR. 2000. LIAN 3.0: detecting linkage disequilibrium in multilocus data. *Bioinformatics* - `PUBMED:11108709 <http://www.ncbi.nlm.nih.gov/pubmed/11108709>`_
.. [Hedrick2005] Hedrick PW. 2005. A standarized genetic differentiation measure. *Evolution* - `PUBMED:16329237 <http://www.ncbi.nlm.nih.gov/pubmed/16329237>`_
.. [Jost2008] Jost L. 2008. G(ST) and its relatives do note measure differentiation. *Mol Ecol* - `PUBMED:19238703 <http://www.ncbi.nlm.nih.gov/pubmed/19238703>`_
.. [Le2008] Le S, Josse J, Husson F. 2008. FactoMineR: An R package for multivariate analysis. *Journal of Statistical Software* - `DOI:10.18637/jss.v025.i01 <http://dx.doi.org/10.18637/jss.v025.i01>`_
.. [Paradis2004] Paradis E, Claude J, Strimmer K. 2004. APE: Analyses of phylogenetics and evolution in R langueage. *Bioinformatics* - `PUBMED:14734327 <http://www.ncbi.nlm.nih.gov/pubmed/14734327>`_




