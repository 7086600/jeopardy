import pandas as pd
import string

pd.set_option('display.max_colwidth', 100)

df = pd.read_csv('jeopardy.csv')

# rename columns
df.rename(columns={
    'Show Number': 'showNumber', 
    ' Air Date': 'airDate',
    ' Round': 'round',
    ' Category': 'category',
    ' Value': 'value',
    ' Question': 'question',
    ' Answer': 'answer'},
    inplace=True)

# lowercase every question
df['question'] = df.question.apply(str.lower)

print(df.head())
print()

# step3: function that filters the dataset for questions that contains all of the words in a list of words
def filterDataQuestionsByWords(data, words):
    # lambda function return True if all of the words in the list of words are in a question 
    checkQuestion = lambda question: all([True if word in question else False for word in words])
    # apply lambda function to question column and return data frame with True question column
    filterData = data[data.question.apply(checkQuestion)]
    return filterData

# testing function
words = ["King", "England"]
fd = filterDataQuestionsByWords(df, words)
print(fd.question)
print()

# step 4: lowercase words; testing function with various values
words = ["King", "England"]
wordsLower = [w.lower() for w in words]
fd = filterDataQuestionsByWords(df, wordsLower)
print(fd.question)
print()
