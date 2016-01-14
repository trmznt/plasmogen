
================================
TUTORIAL 1 - UPLOADING YOUR DATA
================================

.. contents::
.. sectnum::

This tutorial shows step-by-step direction to prepare your datasets and to upload your prepared datasets to |plasmogen| platform, with the accompanying example datasets containing **microsatellite data**. A more detailed guide for data preparation and uploading can be found on the Guide: Data preparation and Uploading.

Since the accompanying data contains microsatellite data, it is assumed that users have a good understanding of the concepts on microsatellite markers.

Preparing Input Files
---------------------

The accompanying example datasets consists of three files:

1. ``sampleinfo.txt`` - A tab-delimited file containing sample information
#. ``fsa.zip`` - A zipped file containing all microsatellite data in FSA-formatted files
#. ``assayinfo.txt`` - A tab-delimited file containing FSA meta data

You can inspect those files by opening the ``sampleinfo.txt`` and ``assayinfo.txt`` files in any software that can read text file, or use any spreadsheet software such as Microsoft Excel or LibreOffice Calc.

A more detailed information about the file format (and the meaning of each field) can be found on Guide: File Format.

If you want to prepare your own input files, any name can be used for each of the three files as long as you follow the format of each file.

Also note that the system is primarily set up to accept data from *Plasmodium vivax* (which is the species of the accompanying example datasets). If data is available for other *Plasmodium Spp*, this can be accomodated in the same input files as long as the relevant fields are filled appropriately (especially the PANEL field in the FSA meta data input file). However, *it is strongly recommended to use different batches for different species* as best practice in order to avoid any problems in the future.


Creating a New Batch
--------------------

Before you can upload the example datasets, you need to create a new batch (unless you want to add to an existing batch). A batch is essentially a collection of samples and molecular data from the same study, or from the same preparation methods.

Log in to |plasmogen| using your username and password, then select **Manage data** button or select **Browse >> Batch** from the navigational menu. A list of existing batch names will be displayed (these names cannot be used for new batches). To create a new batch, select **Add New Batch** (for adding or updating to an existing batch, you will need to select the intended batch name instead).

You will be provided with a form with details fo fill in as listed below. Bold fields are compulsory.

:Batch code: A unique (i.e. not already present in the database) string that identifies  your batch. Allowed characters for the string are alphanumerics, dash or underscore. **Do not use any spaces**.

:Primary group: A string indicating the name of the group or organization providing the data, i.e. the data owner. For this tutorial, set as DEMOGROUP.

:Assay provider group: A string indicating the name of the organization where the assays were run. For the accompanying example datasets in this tutorial, set as MACROGEN.

:Species: A string indicating the Plasmodium Spp.: the system currently supports Pv and Pf assays. For the tutorial, set as **Pv**. *Important*: by setting species, the system will assume that any markers without explicit species code mentioned in any input files are markers for this intended species, unless the species is explicitly stated. For example, marker **MS16** will be assumed as **pv/MS16**.

:Description: A brief description outlining the nature of the samples and the study for which the data was generated.

:Remarks: An optional field for any information regarding this batches, further details on the samples or the study that may be helpful for those who are going to use the data in this batch.

When you have filled up the forms, select **Save**. You will then directed to the batch view page, where you can manage this particular batch.


Adding Sample Data
------------------

On the Batch view, click **Browse** next to Sample info file, and choose the prepared sample info file (or use sampleinfo.tab). Then click on the Upload to temporarily save the info file to server.  Click on Verify to check if the sample info contains errors or problems. Please correct any remaining errors and reupload the sample file. Click on Proceed to save the sample data file into the database.


Adding FSA Zip File
-------------------

From the Batch view, select Start upload session, and then select the fsa zip file (fsa.zip in the tutorial) to upload the files to the server. Once the uploading is finished, click on Verify file to check that the files were uploaded correctly.

If there are no errors, select and upload the assayinfo file (assayinfo.tab in the tutorial) to the server, and then select Verify file to check that the file was uploaded correctly.

If there are no errors, select Proceed to save each of the fsa files to the server.

If there are errors at any step in the process, please contact the systems administrator at anto@eijkman.go.id.


Processing FSA Microsatellite Data
----------------------------------

Once the fsa files have been saved, *fragment analysis* (see the manuscript for further details on this process) must be undertaken. From the Batch view, select **Start FSA FA Manager**, and then select **Process** assays. Note that this is a lengthy task, with the time required depending on the number of fsa files/assays submitted, and how noisy they are. It is possible to do other things, even log out from vivaxgen and then come back again to the FSA FA manager view to inspect the progress, since the processing will be performed as a long-running background task.

Once the fragment analysis process has finished, the assays can be inspected to view the allele calls and adjust values manually if necessary. Once the allele-calling has been finalized, several population genetic analyses can be performed using a suite of tools available in the Analysis tab (see Tutorial 2). Note that further filtering of alleles by absolute and relative allele peak intensity are provided in the analysis tools.


Assessing Fragment Analysis Results
-------------------------------------

On the FSA FA manager view, select **Browse FSA**.

.. |plasmogen| replace:: PlasmoGEN

