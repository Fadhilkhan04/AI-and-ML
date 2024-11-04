import Orange

# Define a simple dataset using a list of lists
data = [
    # Sepal Length, Sepal Width, Petal Length, Petal Width, Class
    [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],
    [4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],
    [4.7, 3.2, 1.3, 0.2, 'Iris-setosa'],
    [4.6, 3.1, 1.5, 0.2, 'Iris-setosa'],
    [5.0, 3.6, 1.4, 0.2, 'Iris-setosa'],
    [7.0, 3.2, 4.7, 1.4, 'Iris-versicolor'],
    [6.4, 3.2, 4.5, 1.5, 'Iris-versicolor'],
    [6.9, 3.1, 4.9, 1.5, 'Iris-versicolor'],
    [5.5, 2.3, 4.0, 1.3, 'Iris-versicolor'],
    [6.5, 2.8, 4.6, 1.5, 'Iris-versicolor'],
    [6.3, 3.3, 6.0, 2.5, 'Iris-virginica'],
    [5.8, 2.7, 5.1, 1.9, 'Iris-virginica'],
    [7.1, 3.0, 5.9, 2.1, 'Iris-virginica'],
    [6.3, 2.9, 5.6, 1.8, 'Iris-virginica'],
    [6.5, 3.0, 5.8, 2.2, 'Iris-virginica'],
]

# Define a domain specifying the attribute types and class variable
domain = Orange.data.Domain(
    attributes=[
        Orange.data.ContinuousVariable("sepal_length"),
        Orange.data.ContinuousVariable("sepal_width"),
        Orange.data.ContinuousVariable("petal_length"),
        Orange.data.ContinuousVariable("petal_width"),
    ],
    class_vars=Orange.data.DiscreteVariable.make("class", values=["Iris-setosa", "Iris-versicolor", "Iris-virginica"])
)

# Load the data into an Orange Table using the new method
data = Orange.data.Table.from_list(domain, data)

# Split data into training and testing sets (70% training, 30% testing)
train_data, test_data = Orange.evaluation.testing.sample(data, n=0.7)

# Initialize a Decision Tree learner
tree_learner = Orange.classification.TreeLearner()

# Train the model on the training data
model = tree_learner(train_data)

# Test the model on the test data and calculate accuracy
results = Orange.evaluation.testing.TestOnTestData(train_data, test_data, [tree_learner])
accuracy = Orange.evaluation.scoring.CA(results)

# Print the accuracy
print("Accuracy:", accuracy)
