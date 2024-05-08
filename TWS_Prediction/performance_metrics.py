import numpy as np

def performance_metrics(y_test, y_pred):
    # Calculate RMSE
    rmse = np.sqrt(np.mean(np.power((y_test - y_pred), 2)))
    rmse = round(rmse, 2)

    # Calculate Normalized RMSE
    nrmse = rmse / np.std(y_test, ddof=1)
    nrmse = round(nrmse, 2)

    # Calculate NSE
    nse = 1 - (np.sum((y_test - y_pred) ** 2) / np.sum((y_test - np.mean(y_test)) ** 2))
    nse = round(nse, 2)

    # Calculate Kling Gupta Efficiency
    kge = 1 - np.sqrt((np.corrcoef(y_test, y_pred)[0, 1] - 1) ** 2 +
                    (np.std(y_test) / np.std(y_pred) - 1) ** 2 +
                    (np.mean(y_test) / np.mean(y_pred) - 1) ** 2)
    kge = round(kge, 2)
    
    r_squared = np.corrcoef(y_test, y_pred)[0, 1] ** 2
    r_squared = round(r_squared, 2, )
    metrics_dict_ = {
        'RMSE': rmse,
        'NRMSE': nrmse,
        'NSE': nse,
        'KGE': kge,
        'R-squared': r_squared
    };
    import json
    # Convert the dictionary to a JSON string
    json_str = json.dumps(metrics_dict_, indent=4);

    # Print the JSON string
    print(json_str)
    return metrics_dict_