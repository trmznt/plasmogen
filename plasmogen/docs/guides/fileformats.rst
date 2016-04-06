
============
FILE FORMATS
============

This guide provides the detailed information about file formats for input files.

Sample Info File Format
-----------------------

The sample info input file contains any information regarding each sample. The format is a tab-delimited text file or comma-separated value text file. The system will deduce the format by the extension of the filename: use .txt, .tab or .tsv for the tab-delimited format, and use .csv for the comma-separated value format.


The list of of fields can be found below. Although only *SAMPLE* field is mandatory, it is highly recommended to at least have **SAMPLE**, **COUNTRY** and **COLLECTION_DATE** fields. Please note that some of the fields can only contain controlled/allowed keywords/vocabularies for data consistency. Controlled/allowed keywords/vocabularies are listed in the last section of this document.

:SAMPLE: (mandatory) A unique string (within the batch) indicating a particular sample. Allowed characters are alphanumerics, dash, dot and underscore. **Do not use space**.

:COUNTRY: The country where the sample was collected or where the patient presented with the infection. Use the 2-character country code (refer to ISO-3166_ ) or internet identification for consistent data.

:ADMINL1: Administrative Level 1 region where the patient presented with the infection (refer to ISO-3166_ ).

:ADMINL2: Administrative Level 2 region where the patient presented with the infection (refer to ISO-3166_ ).

:ADMINL3: Administrative Level 3 region where the patient presented with the infection (refer to ISO-3166_ ).

:ADMINL4: Administrative Level 4 region where the patient presented with the infection (refer to ISO-3166_ ).

:COLLECTION_DATE: Date at which the patient donated the sample. Must be in format of **YYYY/MM/DD** for consistent data, otherwise the system will sometime confuse with the DD/MM/YYYY and MM/DD/YYYY format.

:PASSIVE_DETECTION: Y (yes) or N (no).

:AGE: Patient age in years. Must be an integer.

:GENDER: F (female), M (male).

:BLOOD_WITHDRAWAL: (Controlled Vocabularies) String indicating the blood withdrawal method e.g. capillary, venipuncture or other.

:BLOOD_STORAGE: (Controlled Vocabularies) String indicating the blood storage method e.g. edta, dried blood spot or other.

:MICROSCOPY_IDENTITY: (Controlled Vocabularies) Plasmodium Spp. determined by microscopy. For single species infections: Pf, Pk, Pm, Po, Pv or X (for unknown). For mixed species infections, list the species present in alphabetic order, separated by “/” e.g. Pf/Pv or Pf/Pk/Pv

:PCR_IDENTITY: (Controlled Vocabularies) Plasmodium Spp. determined by microscopy. Details as for field MICROSCOPY_IDENTITY

:PCR_METHOD: String indicating the PCR method used for species confirmation.

:SYMPTOMATIC_STATUS: Indication of whether the patient was symptomatic or not; Y (yes) or N (no).

:PARASITE_DENSITY: Estimated number of parasites per microliter of blood. Must be an integer.

:TYPE: [P/R/D] Type of the sample, either P (for population sample), R (for reference sample) or D (for dummy sample). The default is P (population). A sample will be included in the population analysis if the type is P, otherwise it will be discarded from the analysis set.

:DAY: Sampling day after the first blood collection date. Must be an integer. The default value is 0 (as in day-0).

:RECURRENT: Indication of whether the sample is a recurrence or not; Y (yes) or N (no).

:RELATED_SAMPLE: If multiple samples have been obtained from the same patient, the sample identifer(s) field SAMPLE of the related sample(s) must be provided.

:SUBJECT_CODE: Subject code (only fill this if the subject has been saved to the data base previously).

:INT1: Custom integer.

:INT2: Custom integer.

:STRING1: Custom string.

:STRING2: Custom string.

:REMARK: Any remark or comments for this particular sample.

FSA Info File Format
--------------------

The FSA info input file contains the necessary information for each of FSA file so that the system knows which sample does a FSA file belongs and the markers contained in a FSA file. This file is also a tab-delimited or comma-separated value text file. Similar to sample info file, the system will deduce the format based on the file extension, .txt, .tab, .tsv or .csv.

Below is the list of the fields for this file. All the fields, except OPTIONS, are mandatory.

:SAMPLE: A string as sample identifier. This must exactly match with any of the sample in the database prior to the uploading of FSA info file.

:FILENAME: The FSA file names. These must exactly match with the corresponding FSA filenames in the FSA zip file.

:PANEL: The panel (combination of dye/marker) used for this particular sample, which must be selected from an existing list of markers available in the database. To list all available panels, browse the panel (in navigaton bar, select **Browse >> Panel** ). If your intended panels or markers are not available on the existing list, please contact anto@eijkman.go.id

:OPTIONS: Indication of markers to exclude from a given fsa file. Must be in the format exclude=markername e.g. exclude=MS10. Please use marker names as detailed on the system.

Controlled Vocabularies / Keywords
----------------------------------

Some of the field in the input file require controlled vocabularies/keywords. These are predefined terms which can only be inserted by the adminisrator. The controlled vocabularies help the consistency of the data in the database. If there is a neccessity to add new keywords, please contact |admin|.

Current keywords for BLOOD_WITHDRAWAL:

..  list_ekeys:: @BLOOD-WITHDRAWAL

Current keywords for BLOOD_STORAGE:

..  list_ekeys:: @BLOOD-STORAGE

Current keywords for PCR_IDENTITY and MICROSCOPY_IDENTITY:

..  list_ekeys:: @SPECIES

.. _ISO-3166: http://www.iso.org/iso/country_codes
