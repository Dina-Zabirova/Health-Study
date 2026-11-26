import numpy as np
import matplotlib.pyplot as plt

def multiple_linear_regression(x_values, y_values):
    """
    Beräknar regressionskoefficienter för en multipel linjär
    regression med hjälp av normalekvationerna.

    Parametrar:
        x_values: Matris med oberoende variabler.
        y_values: Vektor med den beroende variabeln.

    Returnerar:
        beta: Array med intercept och regressionskoefficienter.
    """
    ones_column = np.ones(x_values.shape[0])
    design_matrix = np.column_stack([ones_column, x_values])

    transposed_design = design_matrix.T
    gram_matrix = transposed_design @ design_matrix
    design_response = transposed_design @ y_values

    beta = np.linalg.solve(gram_matrix, design_response)

    return beta

def predict(x_values, beta):
    """
    Beräknar predikterade värden med hjälp av
    regressionskoefficienterna.
    """
    ones_column = np.ones(x_values.shape[0])
    design_matrix = np.column_stack([ones_column, x_values])

    return design_matrix @ beta

def plot_regression_results(y_values, y_pred):
    """
    Visualiserar regressionsmodellens resultat genom att
    jämföra observerade och predikterade värden samt
    undersöka residualerna.
    """
    residuals = y_values - y_pred

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].scatter(y_values, y_pred, alpha=0.5)                            # Observerade och predikterade värden

    min_value = min(y_values.min(), y_pred.min())
    max_value = max(y_values.max(), y_pred.max())

    axes[0].plot(
    [min_value, max_value],
    [min_value, max_value],
    color="red",
    linestyle="--",
    label="Observerat = predikterat"
    )

    axes[0].set_title("Observerade och predikterade värden")
    axes[0].set_xlabel("Observerat blodtryck (mmHg)")
    axes[0].set_ylabel("Predikterat blodtryck (mmHg)")
    axes[0].legend()

    axes[1].scatter(y_pred, residuals, alpha=0.5)                           # Residualdiagram
    axes[1].axhline(
    0,
    color="red",
    linestyle="--",
    label="Residual = 0"
    )
    axes[1].axhline(0, color="red", linestyle="--")
    axes[1].set_title("Residualdiagram")
    axes[1].set_xlabel("Predikterat blodtryck (mmHg)")
    axes[1].set_ylabel("Residual (mmHg)")
    axes[1].legend() 

    plt.tight_layout()
    plt.show()