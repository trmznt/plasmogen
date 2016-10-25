
===================
UPLOADING YOUR DATA
===================

.. contents::



This tutorial provides step-by-step directions on how to prepare and upload your FSA files and metadata to the |plasmogen| platform, with an accompanying example *Plasmodium vivax* **microsatellite** dataset.
A more detailed guide for data preparation and uploading can be found in the Guide: Data preparation and Uploading.
Note, it is assumed that users have a good understanding of the general concepts of microsatellite-based genotyping.


Preparing Input Files
---------------------

The example datasets, available as `data-01.zip`_, consist of three files:

1. ``sampleinfo.txt`` - A tab-delimited file containing sample metadata.
#. ``fsa.zip`` - A zipped file containing all microsatellite data in FSA-formatted files.
#. ``assayinfo.txt`` - A tab-delimited file containing FSA metadata

.. _data-01.zip: http://vivaxgen.menzies.edu.au/docs/tutorials/01/data-01.zip

The ``sampleinfo.txt`` and ``assayinfo.txt`` files can be opened for inspection using any software capable of reading text files or spreadsheet-based softwares such as Microsoft Excel or LibreOffice Calc.

More detailed information on the file format  can be found here: `Guide - File Format`_.

.. _Guide - File Format: http://vivaxgen.menzies.edu.au/docs/guides/fileformats.rst

When preparing your own input files, any name can be used for each of the three files, but the file formatting must be strictly adhered to.

Please note that the system is primarily set up to accept data from *Plasmodium vivax*.
If data is available for other *Plasmodium Spp*, this can be accommodated using the same input file formatting as long as the relevant fields are filled appropriately.
*It is strongly recommended to use different batches for different species* as downstream analytical processes will require separation of the different species.


Creating a New Batch
--------------------

Before uploading the example datasets, you will need to create a new batch (unless you plan to add data to an existing batch).
A batch is essentially a collection of samples and associated molecular data which the user intends to analyse together (i.e. from the same study).

Log in to |plasmogen| using the guest or private account details. To establish a private account, with private username and passowrd, you will need to send an email request to the systems administrator at |admin|.

Once logged in to |plasmogen|, select **Manage data**  or **Browse >> Batch** from the navigation menu.
A list of existing batch names, including publically available batches, will be displayed (these names cannot be used for new batches).
To create a new batch, select **New batch**. To add data or update an existing batch, you will need to select the intended batch name instead.

For new batches, you will be provided with a form with details to fill in as listed below.
Compulsory fields are stated.

:Batch code:
  *Compulsory field*.
  A unique (i.e. not already present in the database) string that identifies  your batch.
  Allowed characters for the string are alphanumerics, dash or underscore.
  The maximum length for batch code is 16 characters.
  **Do not use any spaces**.
  Best practise is to use a combination of country identification, species and year, such as IDPV2015 for Indonesian *P vivax* in year 2015.

:Description:
  *Optional but recommended field*.
  A brief description outlining the nature of the samples and the study for which the data was generated.

:Primary group:
  *Compulsory field*.
  A string indicating the name of the group or organization providing the data, i.e. the data owner. For this tutorial, set as DEMOGROUP.

:Assay provider group:
  *Compulsory field*.
  A string indicating the name of the organization where the assays were run. For the accompanying example datasets in this tutorial, set as MACROGEN.

:Batch for bins setting:
  *Compulsory field*.
  This is the batch code that will be used as the reference for bin settings.
  This option allows different batches to have different bins settings and parameters (for examples, bins for LIZ600 and bins for LIZ500).
  For now, just use **default**.

:Species:
  *Compulsory field*.
  A string indicating the Plasmodium Spp.
  The system currently supports Pv and Pf assays.
  For this tutorial, set as **Pv**.
  *Important*: by setting species, the system will assume that any markers without explicit species code mentioned in any input files are markers for this intended species, unless the species is explicitly stated.
  For example, marker **MS16** will be assumed as **pv/MS16**.

:Remarks:
  *Optional field*.
  An optional field for any information regarding this batches, further detailed description on the samples or the study that may be helpful for those who are going to use the data in this batch.

Once you have completed the forms, select **Save**. You will then be directed to the batch view page, where you can manage the given batch.


Adding Sample Data
------------------

On the Batch view, select **Choose file** or **Browse** next to **Sample Info** file, and select the sample info file (sampleinfo.tab in the tutorial).
Then select **Upload** to temporarily save the sample information file in the |plasmogen| platform.
Select **Verify** to check if the sample information file contains any errors.
In case of errors, a message detailing the error lines will be returned.
Correct any errors and re-upload the sample information file.
Ensure that the appropriate sample submission option is checked - for the tutorial, leave as default (Add new samples and update existing samples).
Select **Proceed** to save the sample information file in  the |plasmogen| platform.
On the **Uploading Report** view, if the sample information was uploaded successfully, select **Continue** to return to the Batch view.


Adding FSA Zip File
-------------------

From the Batch view, under **FSA Bulk Uploading**, select **Start** upload session.
In the FSA Bulk Upload Manager view, click on **Select and upload FSA archive file** and select the fsa zip file (fsa.zip in the tutorial) to upload the FSA files to |plasmogen|.
Once the uploading is finished, select **Continue to verify the uploaded archive file** to check that the files were uploaded correctly.
In case of errors, a message detailing the error lines will be returned.
Correct any errors and re-upload the fsa zip file.

If there are no errors, click on **Continue to upload FSA info file (CSV or tab-delimited)** and select the assay information file (assayinfo.tab in the tutorial) to the |plasmogen| platform.
Select **Continue to verify FSA info file** to check that the file was uploaded correctly.
In case of errors, a message detailing the error lines will be returned.
Correct any errors and re-upload the assayinfo file by selecting **Change/replace the uploaded FSA info file**.

If there are no errors, select **Continue to process FSA files** to save each of the FSA files to the |plasmogen| platform.
This process may take a few minutes.
Once uploading is finished, select **Continue** to return to the Batch view.
In case FSA Bulk Uploading is interrupted at any point, you can return to the incomplete session by selecting **List pending sessions** and then selecting the corresponding session.



Processing FSA Microsatellite Data
----------------------------------

Once the FSA files have been saved, *fragment analysis* (see the manuscript for further details on this process) must be undertaken.
From the Batch view, select **Start FSA FA Manager**, and then select **Process FSA**.
Note that this is a lengthy task, with the time required depending on the number of FSA files/assays submitted, and how “noisy” the traces are.
Please also note that you can continue other tasks in |plasmogen| in parallel or log out of the platform without impeding the fragment analysis processing.
If you choose to log out during this processing step, on returning to |plasmogen|, you can navigate back to the FSA FA manager view to inspect progress.
Once assay processing is finshed, select **Continue**, and then select **Browse FSA** files to starting inspecting individual FSA files as described in step 6 (or batch name to return to the batch view).
Note that further filtering of alleles by absolute and relative allele peak intensity are provided in the analysis tools.

Assessing Fragment Analysis Results
-------------------------------------

Once the fragment analysis process has finished, it is recommended to assess the results of the processing.
On the FSA FA manager view, select **Browse FSA** files to open a new page showing the list of the uploaded FSA files together with their parameter results.

The details of the parameters are outlined below:

:FSA Filename: The name of the FSA file

:Sample Code: The sample code for the corresponding FSA file

:Panel: The panel used for the corresponding FSA file

:Score: The quality of ladder peaks of the FSA file, from 0.00 to 1.00 (highest score).

:RSS: The Residual Sum of Squares of the ladder peaks against the regression line. Lower RSS value (< 50.00) indicates higher quality of the FSA file.

:Proctime: The time taken for the system to process the FSA file in miliseconds. Higher processing time usually indicates that the FSA file is noisy.

To inspect individual FSA files, select the corresponding FSA filename (good practise is by right-clicking the mouse button to open a new tab) which will open the FSA viewer.
Individual peaks (alleles) can be manually edited (or re-annotated) by selecting the **Edit** link in the corresponding peak/allele tables.
Once the allele-calling has been finalized, several population genetic analyses can be performed using a suite of tools available under **Analyze** in the navigation menu (see Tutorial 2).
Note that further filtering of alleles by absolute and relative allele peak intensity thresholds are provided in the analysis tools.

If there are any errors at any of steps in the process that cannot be resolved, please contact the systems administrator at |admin|.


.. |plasmogen| replace:: VivaxGEN

.. |admin| replace:: anto@eijkman.go.id

