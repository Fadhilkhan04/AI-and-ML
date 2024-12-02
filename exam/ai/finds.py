def finds(data):

  hypothesis = ['ϕ', 'ϕ', 'ϕ', 'ϕ', 'ϕ', 'ϕ']

  for a in data:
    if a[-1] == 'Yes':
      for i in range(len(hypothesis)):
        if hypothesis[i] == 'ϕ':
          hypothesis[i] = a[i]
        elif hypothesis[i] != a[i]:
          hypothesis[i] = '?'
  return hypothesis



data = [
        ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
        ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
      ]

hypothesis = finds(data)

print("The final hypothesis is :",hypothesis)