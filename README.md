# MakingCovidDataset
Parsing and displaying XML files, making a dataset about Covid.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
XML (Extensible Markup Language) is a markup language similar to HTML, but without predefined tags to use. Instead, you define your own tags designed specifically for your needs. This is a powerful way to store data in a format that can be stored, searched, and shared.
Since this standard format is used in two different contexts and dimensions, in this exercise we will parse, extract and display XML file information.
There are several ways to process XML, three of which we will look at.
this was a good Assignment for Advanced DB Course , Shiraz Univesity Fall 2021.
Exercise description:
Write a program that reads the data set file and does the following:

The xml.covid19 file contains the daily statistics of coronavirus infections in different countries. The structure of this file has a series of record tags for each day and each country
- Write a program that will parse this file using the SAX method and generate output for days when the number of patients in each country is greater than or equal to 100 people.

- Write a program using the DOM parser that generates new versions     of the given XML file so that:
  - Remove the countryterritoryCode tag.
  - Convert the dateRep tag to a plain text date.
- Convert the XML file obtained from the previous step with XSLT to tabulated HTML so that only the records related to Iran are included and each record is placed in one line. Set the border value for this table to 1 for simple framing.
    - Exercise outputs should be the following files:
    - sax.txt contains the SAX parser output in question one.
    - dom.xml contains the XML file generated in question two.
    - dom.xsl contains XSLT definition to convert question three.
 - Calculate the correlation between the features using the cosine 
- There are no restrictions on the use of programming languages. 


