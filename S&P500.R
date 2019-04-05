library(tidyverse)
library(readr)
library(ggplot2)

dataset <- read_csv("Desktop/Python/Data/dataset.csv")
financial <- read.csv("Desktop/R Studio/Constituent Financials.csv")
View(dataset)

dataset <- dataset %>%
  mutate(X1=as.Date.factor(dataset$X1), "%m-%d-%y")

sector <- financial$Sector

date <- dataset$X1

ggplot(data=dataset, mapping=aes(x=EPS, y=CLOSE, color="Close Price vs. EPS"), origin=0, alpha=0.25) +
  geom_hline(yintercept=2000, color="grey") +
  geom_hline(yintercept=1000, color="grey") +
  geom_vline(xintercept=30, color="grey") +
  geom_vline(xintercept=60, color="grey") +
  geom_vline(xintercept=90, color="grey") +
  geom_hline(yintercept=mean(dataset$CLOSE), color="blue") +
  geom_line(alpha=0.5, limits=c(0,2000, color="Close Price vs. EPS")) +
  geom_smooth(color="black", alpha=0.1) +
  theme(panel.background=element_rect(color="black", fill="white")) +
  xlab("Earnings per Share") +
  ylab("S&P 500 Close Price") +
  scale_fill_manual(guide=guide_legend(title="Close Price"))

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