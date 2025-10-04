# first line: 1
@memory.cache
def fit_garch(train, exog, param):
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            model = arch_model(train, x=exog, vol='GARCH', p=param[0], q=param[1], dist='skewt')
            results = model.fit(disp='off')
        return results.aic
    except Exception as e:
        return None
