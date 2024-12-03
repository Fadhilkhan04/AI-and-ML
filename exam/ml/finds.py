import pandas as pd

def finds(data):
    hypothesis = ['ϕ', 'ϕ', 'ϕ', 'ϕ', 'ϕ', 'ϕ']

    positive_rows = data[data.iloc[:, -1] == 'Yes']

    for row in positive_rows.iloc[:, :-1].values: 
        for i in range(len(hypothesis)):
            if hypothesis[i] == 'ϕ':
                hypothesis[i] = row[i]
            elif hypothesis[i] != row[i]:
                hypothesis[i] = '?'
    return hypothesis


data = pd.read_excel("data.xlsx")

hypothesis = finds(data)

print("The final hypothesis is:", hypothesis)
