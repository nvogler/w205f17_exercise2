Ensure all depencies are properly installed prior to executing the application. For guidance, see TODO

# Clone git repository
git clone 

# Change to the appropiate directory and run the application
cd w205f17_exercise2/extweetwordcount/
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


