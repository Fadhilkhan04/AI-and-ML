import Orange

# Load the Iris dataset from Orange's built-in datasets
data = Orange.data.Table("iris")

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
