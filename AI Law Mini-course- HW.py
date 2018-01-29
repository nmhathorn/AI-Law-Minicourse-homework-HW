
# coding: utf-8

# #STEP ONE: Data Collection & Preparation. This step pulls in data from a BeautifulSoup which pulls data from HTML, XML. Pandas helps with the relational data or labled data. This can be helpful for supreme court data, for example, the differing dates of decisions. The numpy will add support for large relational matricies. This step pulls in the data and the organizes it, possibly numerically, into a matrix of some kind so the data is organized and easy to retrieve. It then sets a range of supreme court decision dates. It refines the data to reflect the supreme court only and returns requests based on the range and parameters set.
# 
# ##STEP TWO: Data Collection & Preparation. the code pulls in the URL data with the casename. it then seperates out the case title, using Pickle? Next, it pulls out the year and then the case name. 
# 
# ###STEP THREE: Data Processing. Starts with lists, state names, case names, female names (incl.plural), male names (incl. plural). This step excludes the female and male names. Designates the case list as the list to be used in the model selection. 
# 
# ####STEP FOUR: Topic Modeling Methods. Starts with importing documents and then extracting certain features of those documents. use of LDA to use natural language processing to pull out greater legal themes. Then use NMF to extract the relevant topics. 
# 
# 
# #####STEP FIVE: Topoc Modeling Application. Run the data with all of these parameters and present the data in a model. Starts by running data against the #of topics, features, and top words. Then it extracts the irrelevant list if features, topics and top words. Once this data is extracted it then is applied into a dataframe and is run as a series. This way the most relevant cases appear in their respective columns. 
