####################################
# Chemical Youth Data Sprint
####################################

# required libraries
library(readr)
library(tidyr)
library(dplyr)
library(ggplot2)

# read in the raw data (preprocessed using Python)
cy <- read_tsv("~/projects/chemical-youth/data/top-edits-users-designer-drugs.tsv")

a <- cy %>% 
  group_by(title) %>% 
  summarise(
    n_users = n(),
    n_edits = sum(n_edits)
  ) 

a <- a %>% arrange(desc(n_users))

# export the new table to file
write.table(a, file='~/projects/chemical-youth/data/top-articles-designer-drugs.tsv', row.names = FALSE, quote=FALSE, sep='\t')

# export the top n articles that were edited by the users that contributed to the
# designer drugs pages as well
n = 50
write.table(head(a, n), file='~/projects/chemical-youth/data/top-articles.tsv', row.names = FALSE, quote=FALSE, sep='\t')

ggplot(data = a) + 
  geom_histogram(aes(x = n_users), binwidth = 1)

