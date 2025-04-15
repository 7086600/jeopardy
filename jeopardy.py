import pandas as pd

pd.set_option('display.max_colwidth', None)

# step1: inspecting dataset
df = pd.read_csv('jeopardy.csv', parse_dates=[1])
# print(df.head(10))
# print(df.columns)

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

# print(df.iloc[39:56])
print(df.question.head(10))

# step3: function that filters the dataset for questions that contains all of the words in a list of words

def filterDataQuestionsByWords(data, words):
    # lambda function return True if all of the words in the list of words are in a question
    # lowercase both: word, question
    checkQuestion = lambda question: all([True if word.lower() in question.lower() else False for word in words])
    # apply lambda function to question column and return data frame with True question column
    # filterData = data[data.question.apply(checkQuestion)]
    filterData = data.loc[data["question"].apply(checkQuestion)]
    return filterData

# step4: testing function
print()
words = ["KinG", "eNglAnd"]
fd = filterDataQuestionsByWords(df, words)
print(fd.info())
print(fd.head(10))
print()

# step 5: add column floatValue with converting values to float
print()
# wich values are in value column
# print(df["value"].unique())
floatValue = lambda v: float(v.replace('$', '').replace(',', '').replace('no value', '0'))
df['floatValue'] = df['value'].apply(floatValue)
print(df.iloc[100:121])

print()
# the average value of questions that contain the word
words = ["Queen"]
fd = filterDataQuestionsByWords(df, words)
print(fd.head(15))
print(f"The average value of questions that contain the word - {words[0].lower()} is {fd.floatValue.mean():.4f}")

# step 6: a function that returns the count of the unique answers to all of the questions in a filtering dataset
def countUniqueAnswer(data):
    return data["answer"].value_counts()

print(countUniqueAnswer(fd))

# step 7: function that filters the dataset for questions that date between start and end date

def filterDataQuestionsByDate(data, start, end):
    # convert start and end to datetime format
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    # lambda function return question if date between start-end
    checkDate = lambda date: True if (date > start) & (date < end) else False
    # apply lambda function to question column and return data frame with question between start and end date
    filterData = data.loc[data["airDate"].apply(checkDate)]
    return filterData

print(filterDataQuestionsByDate(df, '1989-12-31', '2000-01-01').head(10))
# Investigating how many questions from the 90s use the different words compared to questions from the 2000s
# filtering dataset by date
jeopardy1990df = filterDataQuestionsByDate(df, '1989-12-31', '2000-01-01')
jeopardy2000df = filterDataQuestionsByDate(df, '2000-01-01', '2011-01-01')
# filtering dataset by word
words = ["apple"]
jeopardy1990fd = filterDataQuestionsByWords(jeopardy1990df, words)
jeopardy2000fd = filterDataQuestionsByWords(jeopardy2000df, words)

print(f'The count of question from 90s with word {words[0]} is {jeopardy1990fd["question"].count()}')
print(f'The count of question from 2000s with word {words[0]} is {jeopardy2000fd["question"].count()}')

# a = input("Enter something: ")
# print(a)