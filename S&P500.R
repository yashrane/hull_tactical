library(tidyverse)
library(readr)
library(ggplot2)

dataset <- read_csv("Desktop/Python/Data/dataset.csv")
financial <- read.csv("Desktop/R Studio/Constituent Financials.csv")
View(dataset)

#Mutating the "X1" column in the dataset to be a date type with form month-day-year
dataset <- dataset %>%
  mutate(X1=as.Date.factor(dataset$X1), "%m-%d-%y")

sector <- financial$Sector

#Setting date as the date column in the dataset
date <- dataset$X1

#Basic plot of a set of data, with date on the x axis and any variable corresponding to that date in y axis
#geom_smooth refers to the line of best fit going through the data
ggplot(data=dataset, mapping=aes(x=date, y=CLOSE), alpha=0.25) +
  geom_hline(yintercept=mean(dataset$CLOSE), color="blue") +
  geom_line(alpha=1, color="black") +
  geom_smooth(color="red", alpha=0.1) +
  xlab("Put 'x' label here") +
  ylab("Put 'y' label here") +
  theme_minimal()

ggplot(data=dataset) +
  geom_point(mapping=aes(x=LOW, y=CLOSE), origin=0)

ggplot(data=dataset) +
  geom_smooth(mapping=aes(x=date, y=CLOSE), origin=0, color="black", alpha=0.5) +
  geom_smooth(mapping=aes(x=date, y=EPS), origin=0, color="red", alpha=0.5) +
  geom_smooth(mapping=aes(x=date, y=ASP*5), origin=0, color="blue", alpha=0.5)+
  geom_hline(yintercept=mean(dataset$CLOSE), color="grey") +
  theme(panel.background=element_rect(color="black", fill="white")) +
  theme(plot.background=element_rect(color="black", fill="white")) +
  scale_x_date(position="bottom", name="Date") +
  ylab("S&P 500 Close Price") +
  scale_fill_manual(guide=guide_legend(title="Close Price")) +
  theme_minimal()

ggplot(data=financial) +
  geom_point(mapping=aes(x=Sector, y=Price, color=Sector, alpha=0.5)) +
  theme(axis.text.x=element_text(angle=90, hjust=1)) +
  geom_hline(yintercept=mean(financial$Price)) +
  scale_fill_manual(guide=guide_legend(title="Sector", nrow=2))

financial <- financial %>%
  mutate(Market.Cap=as.numeric(Market.Cap))

ggplot(data=financial) +
  geom_boxplot(mapping=aes(x=Sector, y=Market.Cap/1000000000, fill=Sector)) +
  theme(axis.text.x=element_text(angle=90, hjust=1)) +
  ggtitle("Market Cap. by Sector") +
  ylab("Market Capitalization (in Billions)") +
  xlab("Sector")

ggplot(data=financial) +
  geom_point(mapping=aes(x=Price, y=Market.Cap/1000000000), alpha=0.5) +
  geom_smooth(mapping=aes(x=Price, y=Market.Cap/1000000000)) +
  ylab("Market Capitalization (in Billions)")



summary(dataset)
unique(dataset$CLOSE)
unique(dataset$X1)