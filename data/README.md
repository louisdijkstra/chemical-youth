`data/`
=======

This documents contains some small notes on the data files in this repository. 

`9top-contributors-other-edits.tsv` 
-----------------------------------

A (tab-delimited) CSV file with the columns: `user` (the username), `title` (title of the Wikipedia page) and `n_edits` (the number of edits he/she made). We started with the 12 originally selected designer drugs. From these 12 subtances, we took the three with the largest associated articles (measured in Bytes): 

* Selegiline
* 25I-NBOMe
* Mephedrone

For these substances, we selected the top three users that contributed most to these pages (measured in the number of edits). For *Selegiline* we found the users: 

* Jytdog
* Bbarmadillo
* Bk0

For *25I-NBOMe*:

* Catclock
* Testem
* Mnation2
    
And for *Mephedrone*

* Smartse
* Materialscientist
* Meodipt

For each of these users, we scraped the articles they edited the most. You find all these in this file. 