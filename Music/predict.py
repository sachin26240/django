
def predict_gen(meta1):
    import pickle
    import os
    from django.conf import settings
    import pandas as pd
    from xgboost import XGBClassifier, XGBRFClassifier
    from xgboost import plot_tree, plot_importance
    path = os.path.join(settings.MODELS, 'models.p')
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    # svmp = data['svmp']
    # norma = data['norma']
    # lgn = data['lgn']
    rforest = data['model']
    features = pd.DataFrame([meta1], columns=['tempo', 'chroma_stft', 'rmse', 'spectral_centroid', 'spectral_bandwidth', 'rolloff', 'zero_crossing_rate', 'mfcc1', 'mfcc2', 'mfcc3',
                            'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11', 'mfcc12', 'mfcc13', 'mfcc14', 'mfcc15', 'mfcc16', 'mfcc17', 'mfcc18', 'mfcc19', 'mfcc20'])
    # x = norma.transform([meta1])
    pred = rforest.predict(features)
    # return(lgn[pred[0]])
    return pred[0]
