reddit <- read.csv('reddit.csv')
table(reddit$employment.status)
str(reddit)
levels(reddit$age.range)

library(ggplot2)
qplot(data=reddit, x = age.range)

reddit$age.range <- factor(reddit$age.range, levels = c('Under 18','18-24','25-34','35-44','45-54','55-64','65 of Above'), ordered = T)

