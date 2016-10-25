
============
FILE FORMATS
============

This guide provides detailed information on file formats for input files.

Sample Information File Format
------------------------------

The sample information input file contains sample metadata.
The format is a tab-delimited text file or comma-separated value text file.
The system will deduce the format by the extension of the filename: use .txt, .tab or .tsv for the tab-delimited format, and use .csv for the comma-separated value format.

The list of fields is presented below.

Only the **SAMPLE** field is mandatory, but it is highly recommended to add details on **COUNTRY** and **COLLECTION_DATE**.
Please note that some of the fields can only contain *controlled vocabularies*.
These are predefined terms set by the systems administrator.
The controlled vocabularies are used to maintain consistency between datasets.
Current available vocabularies/keywords are listed at the end of this document.
If you require a new keyword, please contact the systems administrator at anto@eijkman.go.id.

:SAMPLE: (mandatory) A unique string (unique within the batch) indicating sample identifier/name.
  Allowed characters are alphanumerics, dash, dot and underscore. **Do not use space**.

:COUNTRY: The country where the sample was collected or where the patient presented with the infection.
  Use the 2-character country code (refer to ISO-3166_ ) or internet identification for consistent data.

:ADMINL1: Administrative Level 1 region where the patient presented with the infection (refer to ISO-3166_ ).

:ADMINL2: Administrative Level 2 region where the patient presented with the infection.

:ADMINL3: Administrative Level 3 region where the patient presented with the infection.

:ADMINL4: Administrative Level 4 region where the patient presented with the infection.

:COLLECTION_DATE: Date at which the patient donated the sample.
  Must be in format of **YYYY/MM/DD** to be read correctly into the platform.

:PASSIVE_DETECTION: Y (yes) or N (no).

:AGE: Patient age in years.
  Must be an integer.

:GENDER: F (female), M (male).

:BLOOD_WITHDRAWAL: (Controlled Vocabularies) String indicating the blood withdrawal method e.g. capillary, venous or other.

:BLOOD_STORAGE: (Controlled Vocabularies) String indicating the blood storage method e.g. blood tube, dried blood spot or other.

:MICROSCOPY_IDENTITY: (Controlled Vocabularies) Plasmodium Spp. determined by microscopy.
  For single species infections: Pf, Pk, Pm, Po, Pv or X (for unknown).
  For mixed species infections, list the species present in alphabetic order, separated by “/” e.g. Pf/Pv or Pf/Pk/Pv

:PCR_IDENTITY: (Controlled Vocabularies) Plasmodium Spp. determined by microscopy.
  Details as for field MICROSCOPY_IDENTITY

:PCR_METHOD: String indicating the PCR method used for species confirmation.

:SYMPTOMATIC_STATUS: Indication of whether the patient was symptomatic or not; Y (yes) or N (no).

:PARASITE_DENSITY: Estimated number of parasites per microliter of blood. Must be an integer.

:TYPE: [P/R/D] Type of the sample, either P (for population sample), R (for reference sample) or D (for dummy sample).
  If left blank, the value will be the default, which is P (population).
  A sample will be included in the population analysis if the type is P, otherwise it will be discarded from the analysis set (unless the user specifically asks to include others)

:DAY: Sampling day after the first blood collection date.
  Must be an integer.
  The default value is 0 (as in day-0).
  Most population genetic analysis will only use the day-0 samples.

:RECURRENT: Indication of whether the sample is a recurrence or not; Y (yes) or N (no).

:RELATED_SAMPLE: If multiple samples have been obtained from the same patient, the sample identifer(s) field SAMPLE of the related sample(s) must be provided.

:SUBJECT_CODE: Subject code (only fill this if the subject has been saved to the data base previously).
  This will only be used if there are different samples on different batches that are donated by a same patient (subject).

:INT1: Free field that the user may use to add additional sample metadata of interest that is not provided in the above fields.
  Custom integer.

:INT2: Free field that the user may use to add additional sample metadata of interest that is not provided in the above fields.
  Custom integer.

:STRING1: Free field that the user may use to add additional sample metadata of interest that is not provided in the above fields.
  Custom string.

:STRING2: Free field that the user may use to add additional sample metadata of interest that is not provided in the above fields.
  Custom string.

:REMARK: Field for providing any general remarks/comments on a given sample.

FSA Information File Format
---------------------------

The FSA information input file contains information on each FSA file to be uploaded to the database to enable the system to match each FSA file with the correct sample (SAMPLE) and to identify the assays (PANEL) present in each FSA file.
The format is a tab-delimited text file or comma-separated value text file.
The system will deduce the format by the extension of the filename: use .txt, .tab or .tsv for the tab-delimited format, and use .csv for the comma-separated value format.

The list of fields is presented below.

All fields are mandatory, however **OPTIONS** can be left blank.

:SAMPLE: A string indicating the sample identifier/name.
  This field is used to match the FSA files with the corresponding Sample Information and the sample identifiers must therefore be written exactly the same as in the Sample Information file.
  The system will not upload any FSA files that cannot be matched with an existing SAMPLE string in the Sample Information file.

:FILENAME: A string indicating the FSA file name.
  This field is used to match the FSA files with the corresponding FSA Information and the FSA filenames must therefore be written exactly the same as in the FSA zip file.

:PANEL: A string indicating the panel of assays in a given FSA file.
  For example, MZ2 is a panel of assays for markers MS5, MS12 and MS20 using LIZ-600 size standard.
  The panel must be selected from an existing list available in the database: to view this list,  select **Browse** from the drop-down menu and then **Panel**.
  If your panels or markers are not available on the existing list, please contact the systems administrator at anto@eijkman.go.id.

:OPTIONS: A string indicating the markers to exclude from a given FSA file, for example if an assay was repeated and data on that assay is therefore present in two or more FSA files to be uploaded to the database.
  Must be in the format exclude=markername e.g. exclude=MS10.
  Please use marker names as detailed in the system: to view the list of marker names, select Browse from the drop-down menu and then Markers.
  If no markers are to be excluded from a given FSA file, leave this field blank.

Controlled Vocabularies / Keywords
----------------------------------

All available, updated controlled vocabularies / keywords can be inspected within |plasmogen|.

.. _ISO-3166: http://www.iso.org/iso/country_codes

.. |plasmogen| replace:: VivaxGEN
