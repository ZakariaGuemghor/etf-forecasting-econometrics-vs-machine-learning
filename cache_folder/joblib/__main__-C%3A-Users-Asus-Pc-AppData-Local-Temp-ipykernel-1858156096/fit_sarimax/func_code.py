# first line: 1
@memory.cache
def fit_sarimax(train, exog, param, param_seasonal):
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            model = SARIMAX(train, exog=exog, order=param, seasonal_order=param_seasonal,
                            enforce_stationarity=False, enforce_invertibility=False)
            results = model.fit(max_iter=1000)
        return results.aic
    except Exception as e:
        return None
