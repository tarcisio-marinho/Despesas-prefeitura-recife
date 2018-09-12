setwd(".")



library(data.table)
whisky = fread("whiskies.txt")
library(ggplot2)

#Clustering ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# Prepare Data
whisky.removed.omit <- na.omit(whisky) # listwise deletion of missing
whisky.scaled <- scale(whisky.removed.omit[,3:14]) # standardize variables

#Correlation Test ~-~-~-~-~-~-~-~-~-~-~

corr <- round(cor(whisky.scaled), 1)

# Plot
library(ggcorrplot)
ggcorrplot(corr, hc.order = TRUE, 
           type = "lower", 
           lab = TRUE, 
           lab_size = 3, 
           method="circle", 
           colors = c("tomato2", "white", "springgreen3"), 
           title="Correlogram of Whisky Flavors", 
           ggtheme=theme_bw)

#Number of Clusters ~-~-~-~-~-~-~-~-~-~-~

ssPlot <- function(data, maxCluster = 20) {
  # Initialize within sum of squares
  SSw <- (nrow(data) - 1) * sum(apply(data, 2, var))
  SSw <- vector()
  for (i in 2:maxCluster) {
    SSw[i] <- sum(kmeans(data, centers = i)$withinss)
  }
  plot(1:maxCluster, SSw, type = "b", xlab = "Number of Clusters", ylab = "Within groups sum of squares")
}

ssPlot(whisky.scaled)

#Clustering ~-~-~-~-~-~-~-~-~-~-~

#Try 6 clusters
return <- kmeans(whisky.scaled, centers=6)

library(cluster)
clusplot(whisky.scaled, return$cluster, main='2D representation of the Cluster solution',
         color=TRUE, shade=TRUE,
         labels=2, lines=0)

# Centroid Plot against 1st 2 discriminant functions
library(fpc)
plotcluster(whisky.scaled, return$cluster)

#Add cluster information to a original vector
cluster <- data.frame(return$cluster)
whisky.clustered <- cbind(cluster,whisky.removed.omit)

#plot in the map
library(maptools)
library(rgdal)

whiskies.coord <- data.frame(whisky.clustered$Latitude, whisky.clustered$Longitude)
coordinates(whiskies.coord) = ~whisky.clustered.Latitude + whisky.clustered.Longitude
proj4string(whiskies.coord) = CRS("+init=epsg:27700") # Specify that our coords are in osgb grid coord
whiskies.coord <- spTransform(whiskies.coord, CRS("+init=epsg:4326")) # spTransform to convert osgb grid to lat/lon
coord <- data.frame(whiskies.coord)
whisky.clustered.geo <- cbind(whisky.clustered, coord)

library("ggmap")
whiskyMap <- qmap(location = "Scotland", zoom = 6, legend = "topleft", maptype = "terrain", 
                  color = "bw", darken = 0.5)
geocodeQueryCheck()


plot <- whiskyMap+ 
  theme(legend.position="none",strip.text = element_blank(),strip.background = element_blank())+
  geom_point(data = whisky.clustered.geo, 
             aes(x = whisky.clustered.Latitude, y = whisky.clustered.Longitude, colour = as.factor(return.cluster)),
             size=0.1
  )+
  geom_text(data = whisky.clustered.geo, 
            aes(x = whisky.clustered.Latitude,y = whisky.clustered.Longitude, label = Distillery, 
                color = as.factor(return.cluster)), size=1, hjust = 0
  )+
  facet_wrap( ~ return.cluster)

print(plot)
pdf("WhiskyMap.pdf",width=3, height=4)
print(plot)
dev.off()



#Hierarchical clustering ~-~-~-~-~-~-~-~-~-~-~
d <- dist(whisky.scaled, method = "euclidean") # Euclidean distance matrix.
H.fit <- hclust(d, method="ward.D2")
# Put the labels at the same height: hang = -1
plot(H.fit, labels = t(whisky[,2]), hang = -1, cex = 0.6) # display dendogram
groups <- cutree(H.fit, k=6) # cut tree into 6 clusters
# draw dendogram with red borders around the 6 clusters
rect.hclust(H.fit, k=6, border="red") 



# Model Based Clustering ~-~-~-~-~-~-~-~-~-~-~
library(mclust)
fit <- Mclust(whisky.scaled)
plot(fit) # plot results 
summary(fit) # display the best model

#Distância entre dois agrupamentos
fit1 <- kmeans(whisky.scaled, centers=6)
fit2 <- kmeans(whisky.scaled, centers=6)
cluster.stats(d, fit1$cluster, fit2$cluster)
