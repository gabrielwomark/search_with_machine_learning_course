1. Do you understand the steps involved in creating and deploying an LTR model?  Name them and describe what each step does in your own words.
    1. Inialize LTR Storage
        Runs a PUT request to OS to let it know where and how our models and other data regarding those models will be stored.

    2. Designate Features to the LTR Store
        Run a request POST request which determines what features our models will use and how to generate the values for those features given a query and a document.

    3. Collect Judgments
        In order to train a model to learn how to rank documents by relevance, well need some sort of judgment for how relevant a document is for a particular query. We can obtain these judgets explicitly, e.g. going through query logs and labelling documents as relevant by hand. Or we can collect implicit judgments e.g. judgments that we can collect through logging such as clicks.

    4. Create Training Data 
        We need to create files of data that contain features and judgment labels for all our query document pairs so that they can be used for training a model. We do this by joining our judgment data to the logged features for our documents. 

    5. Train and Test (with XGBoost)
        Here we take the data that we generated in step 4 and train a ranking model using that data. It is imperative that we holdout some of that data so we can evaluate how well our model performs on data it may not have seen before. 

    6. Deploy your Model
        Upload your model to OS so you can start using it to score documents in your queries to OS

    7. Search with LTR
        Add parameters with your OS query to begin using the model scores you generate with your model to reorder results. 

2. What is a feature and featureset?

A feature is some sort of measurable property of a data point that we'd like to generate a model for (e.g. the size in cm of the petals of a flower). A featureset is  a specific grouping of features.

3. What is the difference between precision and recall?

Precision measures the number relevant results returned by a query divded by the total number of results returned by that query. 
But Recall measures the number of relevant results returned by a query divded by the total number of relevant documents for that query that exist within our corpus. 

4. What are some of the traps associated with using click data in your model?

One potential trap is the bias induced by the position of results. Users are more likely to click on things towards the top of a result set because those are the first results they see before scrolling.

Another trap is presentation bias. We simply cannot get click label data for documents that weren't shown to the user. If we aren't retrieving documents that are truly relevant and showing them to the user, then we can't get click labels for those documents. If your corpus is quite large this makes it virtually impossible to measure metrics like recall using click labels. 

5. What are some of the ways we are faking our data and how would you prevent that in your application?
    We are forced to fake our data in this application because we don't have data for results that we're shown to the user but weren't clicked on. One of the ways we're dealing with this is by rerunning all the queries from our query logs to simulate results that the users might have seen upon entering those queries in the past, and then labeling each document in the results of the replay with a click if that query-document pair had a click in our click logs. 
    To avoid this I would create some sort of impression log, i.e. a logging pipeline to keep track of the results we've shown to users. So that we don't have to replay queries to simulate those logs. 
    
6. What is target leakage and why is it a bad thing?

Target leakage is when your model is somehow able to know the answers to predictions on a test set. One example of this could be if you accidentally fit your model on both your training and test data. Because the test data was used at training time, the model is able to minimize loss on that data, which means that evaluations on that test data won't say anything meaningful about how your model generalizes. And that's the main issue with target leakage. It makes it difficult to tell how well your model generalizes. 

7. When can using prior history cause problems in search and LTR?

If the corpus of documents that you're searching across is constantly changing, then this may present problems for search and LTR. For example if we had a job on a job search website that removed it's 401k benefits, then that might change how often people click on the job, rendering our historical clicks for that job null and void for usage in training. 

8. Submit your project along with your best MRR scores
```
Simple MRR is 0.274
LTR Simple MRR is 0.424
Hand tuned MRR is 0.403
LTR Hand Tuned MRR is 0.434

Simple p@10 is 0.107
LTR simple p@10 is 0.187
Hand tuned p@10 is 0.184
LTR hand tuned p@10 is 0.199
Simple better: 508      LTR_Simple Better: 788  Equal: 7
HT better: 608  LTR_HT Better: 810      Equal: 12
```