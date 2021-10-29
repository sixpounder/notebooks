import pandas as pd
import matplotlib.pyplot as plt

def plot_loss_curve(history, x_label="Epochs", y_label="Loss"):
    pd.DataFrame(history.history).plot()
    plt.xlabel(x_label)
    plt.ylabel(y_label)