def decision(predicted_class, confidence):
    if predicted_class == 'Glaucoma':
        if confidence >= 0.85:
            return 'Refer immediately'
        elif confidence >= 0.4:
            return 'Refer'
        else:
            return 'Monitor / Refer'

    elif predicted_class == 'Diabetic_retinopathy':
        if confidence >= 0.85:
            return 'Refer for further evaluation'
        elif confidence >= 0.4:
            return 'Monitor closely; schedule follow-up'
        else:
            return 'Monitor'

    elif predicted_class == 'Cataract':
        if confidence >= 0.85:
            return 'Schedule surgical consult'
        elif confidence >= 0.4:
            return 'Monitor; schedule routine follow-up'
        else:
            return 'Ignore / Routine screen'

    elif predicted_class == 'Normal':
        return 'Ignore'

    else:
        return 'Monitor'  # fallback for any unknown class
