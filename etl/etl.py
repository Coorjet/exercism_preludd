def transform(legacy_data):
    shinyNewFormat = {}
    for key, values in legacy_data.items():
        for value in values:
            shinyNewFormat[value.lower()] = key
    return dict(sorted(shinyNewFormat.items()))
