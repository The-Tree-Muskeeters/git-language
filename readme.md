# The Tree Musketeers

## Mission

To develop an NLP model that predicts which language is used in a GitHub repository based solely on its README file.

### Hypotheses # 1

- $H_0$ There is NO CORRELATION between the length of a repo's README file and its underlying programming language
- $H_a$ There IS A CORRELATION between the length of a repo's README file and its underlying programming language


## Executive Summary 

Using natural language processing (NLP), we were asked to predict the programming language contained in hundreds of Github repositories based solely on the README files for that repository.  After briefly discussing the project and analyzing the data we pulled in, we formed a simple hypothesis that the length of the README file would be a good indicator of the programming language used.  Provided information that Python (the language used throughout this project) was a preferred language amongst programmers because of its strict adherence to documentation guidelines, we assumed that longer README files pointed to program contents being written in Python as opposed to other languages like C# ('C-sharp') or Java.

After acquiring our dataset using Python and its library 'BeautifulSoup', we explored our findings to actually 'see' them through various visualizations made possible with Matplotlib and Seaborn.  Some of what we found follows:


## Glossary of Terms

To better understand our mission, it should be noted that jargon is rampant in every industry, and Data Science is no different.  Industry terms get tossed around like shotputs at an Olympic qualifier, so it is easy for the outsider to get mired down in our everyday verbiage.  Below is a simplified glossary of terms to help in understanding exactly what it is we're talking about.

**Model** - in Data Science, a model is an organized look at the parts of the data and how they relate to each other.  Just imagine getting in your car every day: in some combination, you open the door, collapse in the seat, put your foot on the brake, put the keys in, put on your seatbelt, etc.  Since you repeat this process over and over, your brain starts learning the relationships between all those little actions, and the whole process gets more efficient.  That's all a model is.

**Webscraping** - going through the source code on a website and selecting the data we want based on the information we find.  Think of a web page as a human body: what you see when you go to a website is the skin, but underneath it are the muscles and bones supporting that skin.  Webscraping is like using an MRI or X-Ray to see and study those supporting structures in which we're most interested.  

**API** - short for 'Application Programming Interface,' an API is basically a set of rules that allow two software programs talk to each other.  You use APIs on a daily basis - that app on your iPhone, for instance.  Apple has an API full of code that app developers can 'borrow' with just a few commands instead of having to rewrite that whole chunk of code every time they need it.

**Repo** - short for 'repository.'  You may know it as the term 'directory,' which is a place on your computer where you store your files.  A 'repo' is exactly that, but instead of those files being stored on *your* computer, they are housed within the GitHub supercomputer.

**README** - a common file found in any GitHub repo that describes the details of the repo's contents.  There are no standards on length or content, so the information on a README can be as extensive as either a Tolstoy novel or a fortune cookie.  (You, dear reader, have stumbled upon a Tolstoy.)

**JSON** - although tech-y shorthand for 'JavaScript Object Notation,' JSON actually comes in quite handy for most people.  When you get online and go to a website, you are actually going to a server.  The server is kind of the gatekeeper that determines your elibibility to access the information you want from the web application.  What JSON does is send you back that information in a human-readable format.  In other words, it takes complicated computer language and pretties it up for us to read.

**Pandas** - a library written specifically for our chosen programming langauge (Python), Pandas takes information and returns it to us in a vivid, easy-to-read table format.  The table consists of three main parts: rows, columns, and the data itself.  Each vertical column is a feature of the dataset, whereas each horizontal row is an event or occurence within the dataset.  There is a whole lot that goes on behind the scenes to make this possible, but the end result is all that matters: an appealing yet informative look at data.

**The train-validate-test data split** - taking the data and dividing it into training, validating, and testing portions.  Think of your favorite football team - the players don't just get up off the couch and go play on Sundays, they train long before the season begins to see where their strengths and weaknesses are, which schemes work the best, and how to see which players play best at their respective positions.  Think of the 'train' portion as the off-season work, 'validate' as the scrimmages to make sure their work is effective, and 'test' as showtime: your team's up against real unknowns. 

**Tokenization** - the process of breaking something down into more discrete units.  You don't swallow a whole burger, you take bites. 

**Normalizing** - to normalize data is to restructure it so that it looks and reads the same way across all records.  In this project, we normalize our data to make it more unifrom (i.e. minimized variation) for ease of use in NLP processing.

**Lemmatize** - to 'lemmatize' a word means to strip the entire word down to its base word.  Computationally more expensive than stemming (a similar process that reduces a word down to its root but less gracefully), lemmatized words still retain their readability.  Reading lemmatized text you still get the gist of the message even though the excess letters and characters are gone.

**Stopwords** - words not unique to our situation.  They are words like 'a, an, the, like' that can be found in any document and can be thought of as filler words.  They can be eliminated from our analyzed text while still preserving the general meaning of the text itself.

## What Is Natural Language Processing? 

Natural Language Processing (NLP) is a subfield of Artificial Intelligence (AI) concerned most specifically with human - computer interactions.  It involves assembling a body of data (a 'corpus') and reading through each aspect of it in search of patterns for prediction.  Google's latest Gmail installment provide us with a clear, although very simple, example:

People are creatures of habit, and in typing an email, Google's NLP algorithm will compare your current email's contents to countless other emails you've previously written.  In real-time, it matches patterns of those emails with the one you are currently writing;  previous phrases tend to follow a certain string of characters / commands you've used in the past, and as you type, it will offer time-saving suggestions that will speed up your productivity with the simple stroke of your 'Tab' key.

There are many other uses for NLP (chatbots that 'assist' you in your online purchasing endeavors, the spam filter on your personal / business email accounts, etc), and its ability to predict patterns of action / behavior is streamlining business at an ever-expanding rate.

## Project Introduction

Beginning 1 June 2020, our team was tasked with building an NLP model to predict the programming language of a GitHub repository based solely on the text of the README file. 

GitHub is an online version control platform that provides hosting services for software development.  Each repository is a publicly accessible file from which users can pull information and see the development of a program at various points in its evolution.

To those unfamiliar with the jargon-heavy vocabulary of programming, think of baking a pie for friends.  

GitHub is the giant cookbook filled with recipes from all over the world.  Each recipe is detailed in both its ingredients list and the step-by-step processes you need to achieve a perfectly flaky - yet tender - pie crust.

But unlike a regular cookbook, as people try these recipes, they can make adjustments to them and contribute these changes to improve the pie itself.  For instance, baking times and temperatures will be different for the cook at a low sea-level like New Orleans than it would be for the aspiring chef in the mountains of Colorado.  Each change is as detailed as possible so that anyone finding it can browse through the contents of that recipe and see exactly what it is they're looking for.  

That is the essence of GitHub: a cloud platform where people can view software development at various stages and - with the proper permissions - volunteer their contributions in an effort to improve the performance of the original product.  

Unlike previous projects involving provided sets of data, we were tasked with developing our own dataset from which to lauch our efforts, meaning consistent communication and collaboration throughout this project's lifecycle.  Among other things, this included individual contributions from three different origin computers into a single, readable Jupyter notebook without unknowingly rewriting / adjusting previous code.  

Team members include Shay Altshue, Ravinder Singh, and Nick Joseph.

## Scope:

In our efforts to complete this project, we followed the typical Data Science Pipeline:

1.) Acquisition - getting the data;

2.) Preparation - cleaning and deciding what to do and how to use the data we've acquired;

3.) Split - taking the data and dividing it into train, validate, and test portions; 

4.) Exploration - visualizing the training data so we can see what and how things are related; 

5.) Scaling - a change in data to make all values rest between 0 and 1 for better representation.  However, in this project we are instead 'normalizing' in an effort to describe our data as a normal distribution (or, 'bell curve');

6.) Modeling - devising a baseline model to run various other models (Decision Trees, etc) against to test our null hypothesis; and

7.) Delivery - a final notebook and slide deck for presentation and peer review 

## Acquisition

Because Github frowns on actual webscraping, acquiring the data for our project involved dealing directly with GitHub's API (Application Programming Interface).  While both deal with the harvesting of data, using GitHub's API required an access token, which is basically your computer telling GitHub, "Here is everything about me and my user.  Is it okay if we come in and look around?"  

Webscraping (or, 'scraping') GitHub requires no credentials and is regulated only by the ethics of the person scraping their page.  All someone has to do is right click on a page, follow a few menu choices, and then have all the page's information right in front of them.  Thus, it is easy to see why a site filled with ideas on the future of computing would not take a shine to something so easy and anonymous as a webscrape.

The Python functions written for this phase of the project are designed to get the README portion from the various repos on the GitHub API and return it to us in a more easily-digestible JSON format.  Kicking off this phase were some helper functions from our instructor (Zach Gulde) that got us the needed tokens to work with GitHub.

## Preparation

Because the JSON format is essentially a list of dictionaries, we can easily convert the data into the more familiar Pandas DataFrame or Series for preparation.  In this format, we can see the data easily and develop some 'horse-sense' predictions on what it tells us.  A quick look into the data reveals that of the 280 README's we originally looked at, 35 were missing values labeled as 'language.'  

It was decided that while those 35 null-values were over 10% of our sample data, some further investigation concluded that these values could be dropped from our dataset because we were looking language itself - can't extract data from what is not there.  Also facing the chopping block were repos with less than five (5) languages, which reduced our data pool from twenty-six (26) different languages down to twelve(12).  

These 12 languages were then graphed with a horizontal bar plot to reveal the overwhelming majority of the repos we scraped were written using JavaScript.  

A function was written to create a new language category called 'Other.'  In it were any languages that didn't include 'The Big Five' of 'JavaScript',  'Java' ,'Python' , 'C++' , or 'HTML.'  The reasoning for this was [COMPLETE]

Running a similar bar plot to what we did earlier, it's apparent there are many other languages to consider, as the 'Other' numbers took the lead.

Part of our job is to make the data as uniform as possible.  With letters and words as our interest, you can imagine the variation in both when it comes to the global span of GitHub users.  It is our job to strip those occurences from our data as much as possible.  

Though this preparation stage was rather exhausting, Ravinder and Shay developed the necessary functions to do just that.  We end up with a dataframe with columns representing cleaned, lemmatized, and tokenized README data from which the stopwords have been removed.  

There were a few tools used that may need some further explanation.  In cleaning the data, we implemented a meta-language called 'regex' (short for 'Regular Expressions') that can go through any type of data and remove the parts we don't want.  From accent marks to unwanted symbols and spaces, it is extremely useful in giving the data uniformity,  and not just in Python, but in other programming languages as well. 

A decision was made to drop the column labeled 'repo,' as it gave us back the actual repository name, and getting rid of that column would make our exploration easier without jeopardizing the data itself.

An essential device in any NLP repertoire, the NLTK ('Natural Language Toolkit') is imported into our notebooks as 'nltk.'  It is a suite of resources ("libraries") that aims to help machines understand human language.  Think of it as an actual library filled with books.  Each book helps us do a slew of things to the letters and words we choose, all with the goal of normalizing our data.  

Along with that library, we ran the necessary functions (details in notebook) that cleaned, normalized, tokenized, and lemmatized the data, and removed all suggested stopwords as well.  This all happened because we wanted to reduce the variability of our data, and all these processes cut the fat off the words we want our machines to understand.  From the DataFrame our functions returned, we dropped the column total down to the four that had the information pertaining to our mission: the language, the README contents, and the 'cleaned up' version of the README contents (the fourth column was our index column).

From here, exploration began.

## Exploration

Once the README data has been normalized, we proceeded to visualize the cleaned training portion of our data (split 80% training, 20% testing)using the Matplotlib and Seaborn libraries.

One of the first things we checked was the top 15 words appearing most often in our README corpus ('body' of files).  The word 'com' was the runaway winner, with a total of 9,172 occurences.  You'd think silver was a good medal, but 'org' got silver, and it was only represented 1,773 times in our sample data.  (Oddly enough, the word 'data' ranked 15th with only 821 occurences.)

An Inverse Document Frequency ('IDF') function was written to find out just how much information a word provides.  To quickly paraphrase its purpose: our data is in the form of documents.  The more frequently we see a word in the documents, the less important it is to us.  The more often the word is found, the lower its relevance, or here, the lower its IDF score.  If you want to find an important word, look for less frequency and a higher IDF.

Once the IDF was evaluated, a DataFrame was created from the number of unique words and the IDF score attached to them.  The data from the DataFrame showed us that these unique words have significant relevance throughout the README documentation.  Also, we wanted to see how many words the average README file contained (at least, those README files from our sample), and we saw a normal distribution (though skewed right): an overwhelming majority contained between 1,000 and 1,200 'cleaned' words in total.  

A boxplot revealed that while the middle 50% of the Python language had the most range in the number of words used in README files, the median number of words across 'C++,' 'Other,' 'Java,' 'JavaScript,' and 'HTML' were very close - somewhere in the range of about a thousand words.  This validates the distribution plot we discussed in the prior paragraph.

## Testing

Because we are testing to see the relationship between a fluctuating variable (number of words) and a fixed variable (the programming language), a statistical T-Test was run.  The hypotheses we were testing are laid out in the following:

- $H_0$ - The average number of words in either a Python or JavaScript file is identical; vs.

- $H_a$ - The average number of words in either a Python or JavaScript file is different.

Because we found a high probability value that the first of the two hypotheses could indeed happen, we fail to reject the idea that the average number of words between the two languages could be the same. 

## Modeling

Since the features have been extracted, we now must figure out how to represent them in a way the computer can understand them.  To do so, we use a SciKit-Learn library called CountVectorizor.  What this does is encode (translate) our programming languages into binary characters (0's and 1's) the computer understands: where our word appears, the computer will see a '1.'  Where it doesn't, a '0.'

There are a series of models we ran, each with varying levels of accuracy, but before we did anything we had to first come up with a baseline model.  Basically, it's what you would predict would happen if you listened to your horse sense.  That baseline performed poorly, with an accuracy of 26%.  Other models (the ,K-Nearest Neighbors, Random Forest, Decision Tree, and Logistic Regression) performed better, but the Naive-Bayes Model was our best performing model, as it had a prediction accuracy of 68%.

What is Naive-Bayes?  Think of it this way: There are two Math books, Book 1 and Book 2.  You have no idea what's in them, but someone rips out a few pages from each of them and hands them to you.  The pages from Book 1 have numbers like 2, 4, and 6.  The pages from Book 2 have numbers with exponents and Greek letters next to them.  Without even opening the books, you can tell that Book 2 is the more complicated Math book than Book 1.  That is, in essense, Naive-Bayes: it tells you the probability of what's in those books without ever actually looking into the books themselves.

## Conclusion

To develop a model from scratch that is 68% accurate in its predictions based solely on one facet of an entire, expansive database is pretty solid.  However, we're not breaking our arms while patting ourselves on the back - this could be improved.  How much so, we don't know, but if we were tasked with (or allowed to) examine the GitHub repos based on something like file extensions or re-create our models so that we could see any images, we believe we could bump or final model's accuracy by a significant percentage.

## Google Slides Link

To view our slide deck and how we visually represented our findings, we welcome you to visit the actual [presentation](https://docs.google.com/presentation/d/1i98IIckO5pwUA-o4od7V_7PEWDJPPgVTUTGCONnoga0/edit#slide=id.p). Thank you for your time, and we look forward to hearing your thoughts!
