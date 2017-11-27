Ensure all depencies are properly installed prior to executing the application. For guidance, see TODO

## From the w205 user's home directory
# Clone git repository
git clone 

# Move into directory
cd w205f17_exercise2/

# Update credentials
vim extweetwordcount/src/spouts/tweets.py

# Replace the following four sections with credentials from your Twitter application
#### These keys will be active for a dummy account until 12/30/2017
"consumer_key"        :  "Phl7YAbc9voRiXNss0MH6gUwN",
"consumer_secret"     :  "Nmp6rfPmak8kvh1p5x55rdBOHvrCBaB5G71pPTWOGlJzqLMEOf",
"access_token"        :  "934876405313175559-iYj8f7JHHfDN1wh822bDYruG5tiBzYe",
"access_token_secret" : "Cw9Y5l7dkiSWC1QneHtK8LFupHUpTEXRrLxv980rGMUrj",

# Change to the appropiate directory and run the application
cd extweetwordcount/
sparse run

# After enough tweets have been collected (~2 minutes), press Ctrl+C to stop the listener
<Ctrl+C>

# Now the tcount database contains tweet content and is ready to be analyzed

# Change to appropiate directory
cd ..

# To lookup the counts for all words, run:
python finalresults.py

# To lookup the counts for a specific <word>, run:
python finalresults.py <word>

# To create a histogram for words with counts between boundaries <k1> and <k2>, run:
python histogram.py <k1>,<k2>


