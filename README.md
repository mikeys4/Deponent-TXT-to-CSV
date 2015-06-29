# Deponent-TXT-to-CSV
A simple string parser that converts a txt list of case names, depositions, and dates to a .CSV file for use in Excel

This program takes a text file, formatted like so:

Case Name vs. Example: Deponent Name MM/DD/YY, Deponent Name MM/DD/YY

  OR
  
Case Name vs. Example: Deponent Name M/D/YY

And puts it into a CSV file with three columns, Case Name | Deponent Name | Date.
For multiple deponents per case (ie, for the first line of our example formatting), it will duplicate the case name
across rows.

I wrote this to help myself learn programming so I doubt anyone would have any use for it.
