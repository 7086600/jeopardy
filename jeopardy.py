import pandas as pd

pd.set_option('display.max_colwidth', None)

df = pd.read_csv('jeopardy.csv')
#print(df.columns)

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

#print(df['question'])

# function that filters the dataset for questions that contains all of the words in a list of words

ws = ["King", "England"]
qs = ["How many King in England?", "How old r u", "United kingdom of Great Britain", "Charles is the King of England"]


def checkWordsInQuestion(words, questions):
    checkQuestionsList = []
    check = lambda question: all([True if word in question else False for word in words])
    for q in questions:
        checkQuestionsList.append(check(q))
    return(checkQuestionsList)

print(checkWordsInQuestion(ws, qs))



#checkWordsInQuestion(questions, words)

# filterDataByWords = lambda listOfWords: all(listOfWords)

# df['wordInQuestion'] = df.question.apply(filterDataByWords["King", "England"])
# print(df)
