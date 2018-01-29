Step 1: Supreme Court Modelling Homework


STEP ONE: Data Collection & Preparation. This step pulls in data from a BeautifulSoup which pulls data from HTML, XML. Pandas helps with the relational data or labled data. This can be helpful for supreme court data, for example, the differing dates of decisions. The numpy will add support for large relational matricies. This step pulls in the data and the organizes it, possibly numerically, into a matrix of some kind so the data is organized and easy to retrieve. It then sets a range of supreme court decision dates. It refines the data to reflect the supreme court only and returns requests based on the range and parameters set.

STEP TWO: Data Collection & Preparation. the code pulls in the URL data with the casename. it then seperates out the case title, using Pickle? Next, it pulls out the year and then the case name. 


STEP THREE: Data Processing. Starts with lists, state names, case names, female names (incl.plural), male names (incl. plural). This step excludes the female and male names. Designates the case list as the list to be used in the model selection. 

STEP FOUR: Topic Modeling Methods. Starts with importing documents and then extracting certain features of those documents. use of LDA to use natural language processing to pull out greater legal themes. Then use NMF to extract the relevant topics. 

STEP FIVE: Topoc Modeling Application. Run the data with all of these parameters and present the data in a model. Starts by running data against the #of topics, features, and top words. Then it extracts the irrelevant list if features, topics and top words. Once this data is extracted it then is applied into a dataframe and is run as a series. This way the most relevant cases appear in their respective columns. 


Step 2: Tensorflow Homework 

The first step included importing all of the data. The data was then downloaded into a zip file and classified into a different strings - useful language for the program to store the data. The next command line includes building two dictionaries - one that assigns number to words, the other assigning words to numbers.  The following step is titled: "Function to generate a training batch for the skip-gram model." The skip-gram model takes two inputs. One is a batch full of integers representing the source context words, the other is for the target words. The next step includes building and training the skip-gram model. This seems like the actual AI part of the exercise where the input data is classified, labeled, and trained in order to be useful for building a graph.  Some of the code segments include batch size, embedding size, num_skip, and num-samples. The batch size  (128) looks like the total number of examples analyzed in forming the graph. The embedding size is the same (128). The skip window command is set at 1. Due to this, the algorithm looks, not only at each input value, but at 1 value to the left and 1 value to the right of each input. This allows the algorithm to look at each value in context, not as a standalone - most likely providing for a more accurate interpretation. Num_skips is set at 2. This means that the algorithm reuses the input twice in order to label the input. Reusing the input twice ensures that the input is appropriately labeled. Num_sampled is set at 64. This is the number of negative examples to sample in the data set. This quantity of negative samples will most likely help to refine the code, appropriately classifying the input data. Once, the input data has been classified, it is inputted into the graph (the mathematical equation that is associated with the graph). The final step is "Visualize the embeddings." This occurs after training has finished. The commands executed in this section include plotting, labeling the x and y intercepts, and displaying in matplotlib. All of the above resulted in a graph showing words that are similar ending up clustered nearby each other. 

Madeleine Tavcar
Marinna Radloff
Nichole Hathorn# AI-Law-Minicourse-HW

