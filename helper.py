import matplotlib.pyplot as plt

def plot_embeddings(embeddings, figsize=(8, 6), words = ['king', 'queen', 'man', 'woman', 'son', 'daughter', 'rich']):
    """
    Plots a scatter plot of word embeddings.

    Parameters:
    - embeddings: dictionary of word to embedding (word: [embedding_vector])
    - figsize: size of the plot
    """
    embeddings = {k:v for k, v in embeddings.items() if k in words}
    # Create a new figure with the specified size
    plt.figure(figsize = figsize)

    # Extract words and their corresponding embeddings
    words = list(embeddings.keys())
    vectors = [embeddings[word] for word in words]

    # Convert vectors to a 2D list (or array) for plotting
    vectors = [vector[:2] for vector in vectors]  # Assuming 2D embeddings

    # Separate the x and y components of the embeddings
    x_vals = [vector[0] for vector in vectors]
    y_vals = [vector[1] for vector in vectors]

    # Plot each word's embedding
    plt.scatter(x_vals, y_vals)

    # Annotate each point with the corresponding word
    for i, word in enumerate(words):
        plt.annotate(word, (x_vals[i], y_vals[i]))

    # Set labels and title for the plot
    plt.xlabel('Embedding Dimension 1')
    plt.ylabel('Embedding Dimension 2')
    plt.title('Word Embeddings Scatter Plot')

    # Display the plot
    plt.show()
