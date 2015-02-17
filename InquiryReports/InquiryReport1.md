#Problem

I want to cluster all of the beats in a given song.

#Questions

1. How do you cluster beats in a song?
2. Could you replace a beat with a different beat in it's cluster while maintaining the overall sound of the piece?
3. Does the number of clusters change with different genres, artists, and albums? (using the thresholds set in InfiniteJukebox)

#Resources

1. [Programming Collective Intelligence]
2. [The Beatles Genome Project: Cluster Analysis and Visualization of Popular Music]
3. [Million Song Dataset]

### 1. Mini-abstract and relevance of [Programming Collective Intelligence]

Programming Collective Intelligence is a book on processing data using Python. It has multiple chapters on different clustering algorithms that I would like to implement for this project. The two specific algorithms I would like to work with are [Hierarchical Clustering] and [K-Means Clustering]. Hierarchical Clustering creates a hierarchy of grouped items by "continuously merging the two most similar groups" in the dataset. Hierarchical Clustering first computes the the distance between every single pair of items. It takes the two items that are found to be the closest and creates a cluster with these two items setting the average of their data as the value of the cluster. This process it repeated many times until the hierarchy is completed. The downside to the method is that it's complexity is not good, so it will not work for a large dataset. I could, however, apply it to a song. With K-means clustering, you must specify the number of clusters you want before hand. Then it arranges the data into that many clusters. It first chooses k random centroids and aligns all of the data up with the points that are most similar. It then recalculates the centroids values by averaging all of items in the cluster. The process is repeated until the clusters stop changing. The disadvantage to K-means clustering is that you must specify the number of clusters beforehand and that your clusters will not stay constant with multiple tests. This resource helps me answer question 1 by providing two different methods for clustering beats in a song.

### 2. Mini-abstract and relevance of [The Beatles Genome Project: Cluster Analysis and Visualization of Popular Music]

In this research paper, Douglas J. Mason applies [Hierarchical Clustering] " to show statistical phenomena occuring in a corpus of popular songs written by the Beatles." For his hierarchical clustering, Mason used "a feature vector space that links each dimension to an individual chord in relation to the tonal center" for the "Rolling Stone list of the 100 Greatest Beatles Songs." "The value of a song
in each dimension corresponds to the percentage of the song which plays that chord." This is similar to what I want to be able to do. I just want to do it according to indivual beats across multiple genres and artists. I also want to use the analysis from [The Echo Nest] opposed to analysis from "a single melodic line written in standard music notation." While Douglas J. Mason's project is very much different from my own, I hope it may help me with what I am trying to accomplish.

### 3. Mini-abstract and relevance of [Million Song Dataset]

The Million Song Dataset provides analysis from [The Echo Nest] for a million different songs. With the analysis of many different genres, artists, and albums found in the Million Song Dataset, I hope to use this data to answer question 3 once I have implemented my clustering algorithm. 

[Programming Collective Intelligence]: http://0-proquest.safaribooksonline.com.wncln.wncln.org/book/web-development/9780596529321
[The Beatles Genome Project: Cluster Analysis and Visualization of Popular Music]: http://web.cse.ohio-state.edu/~raghu/teaching/CSE5544/Visweek2012/infovis/posters/mason.pdf
[Million Song Dataset]: http://labrosa.ee.columbia.edu/millionsong/
[Hierarchical Clustering]: http://0-proquest.safaribooksonline.com.wncln.wncln.org/book/web-development/9780596529321/3dot-discovering-groups/hierarchical_clustering
[K-Means Clustering]: http://0-proquest.safaribooksonline.com.wncln.wncln.org/book/web-development/9780596529321/3dot-discovering-groups/hierarchical_clustering#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODA1OTY1MjkzMjElMkZrbWVhbnNfY2x1c3RlcmluZyZxdWVyeT1ub24tbmVnYXRpdmU=
[The Echo Nest]: http://the.echonest.com/
