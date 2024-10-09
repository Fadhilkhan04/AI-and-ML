def find_s(examples):
   
    hypothesis =  ['ϕ', 'ϕ', 'ϕ', 'ϕ', 'ϕ', 'ϕ']

   
    for a in examples:
        if a[-1] == 'Yes':  
            for i in range(len(hypothesis)):
                
                if hypothesis[i] == 'ϕ':
                    hypothesis[i] = a[i]
                elif hypothesis[i] != a[i]:
                    hypothesis[i] = '?'

    return hypothesis
# Example usage:
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]
hypothesis = find_s(data)
print("Final hypothesis:", hypothesis)
