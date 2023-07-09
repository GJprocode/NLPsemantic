#### NLPsemantic
##### Semantic similarity with NLP python Spacy library
##### 1. Defining word objects and measuring similarity.
##### These lines define word objects using the loaded model and measure the 
##### similarity between pairs of words using the similarity method. 
##### 2. This code demonstrates how to work with word vectors.
##### It creates word objects for the words "human," "alien," "shoe," and "sock" 
##### and measures the similarity between all pairs of words. 
##### 3. This code compares the similarity between a given sentence
##### and a list of other sentences. It uses the loaded model to
##### calculate the similarity and prints the sentences along with
#####  their respective similarity scores.
##### Code description 1. 2. 3. 
###### IDE used = Virtual Studio, OP = Windows 11, Language = Python
###### 3.1 Clone repository with command below. Must have Git & Github installed.
###### git clone https://github.com/CrypticDG/NLPsemantic
######  3.2 Move to project root folder
######  cd NLPsemantic
###### 3.3 Create a virtual environment
######  virtualenv 'env1' - (create virtual environment and give it a name)
######  env1\scripts\activate (activate virtual environment that stored all your modules for your project)
######  3.4 Install requirements.txt, (this will install all the modules you will need to run this app)
###### py -m pip install -r requirements.txt
######  3.5 run you app  (not containerized before deploy, see Docker section 3.6)
###### 3.6 Docker(Have Docker Hub and Docker desktop installed)
###### Run in terminal: docker build -t nlp1 .    
###### Run in terminal: docker run nlp1  
