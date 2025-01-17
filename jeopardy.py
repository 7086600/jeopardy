import pandas as pd

pd.set_option('display.max_colwidth', 70)

df = pd.read_csv('jeopardy.csv')

# step2: rename columns
df.rename(columns={
    'Show Number': 'showNumber', 
    ' Air Date': 'airDate',
    ' Round': 'round',
    ' Category': 'category',
    ' Value': 'value',
    ' Question': 'question',
    ' Answer': 'answer'},
    inplace=True)

print(df.iloc[39:56])
print()

# step3: function that filters the dataset for questions that contains all of the words in a list of words
def filterDataQuestionsByWords(data, words):
    # lambda function return True if all of the words in the list of words are in a question
    # lowercase both: word, question
    checkQuestion = lambda question: all([True if word.lower() in question.lower() else False for word in words])
    # apply lambda function to question column and return data frame with True question column
    filterData = data[data.question.apply(checkQuestion)]
    return filterData

# testing function
words = ["viking"]
fd = filterDataQuestionsByWords(df, words)
# print(fd.head(5))
print()

# step 5: add column floatValue with converting values to float
floatValue = lambda v: float(v.replace('$', '').replace(',', '').replace('no value', '0'))
df['floatValue'] = df['value'].apply(floatValue)
print(df.iloc[39:56])
print()
# the average value of questions that contain the word
word = ["KinG"]
fd = filterDataQuestionsByWords(df, words)
print(f"The average value of questions that contain the word - {word[0].lower()} is {fd.floatValue.mean():.2f}")