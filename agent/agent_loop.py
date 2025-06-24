from agent.sensor import sense
from agent.decision import decision  

def agent_loop(image_paths, model):
    """
    Run the perceive–decide loop over a list of image paths.

    Args:
        image_paths (list of str): Filepaths to the images to process.
        model (tf.keras.Model): The preloaded Keras model.

    Returns:
        list of dict: Logs containing image_path, predicted_class, confidence, and action.
    """
    logs = []

    for image_path in image_paths:
        predicted_class, confidence = sense(image_path, model)
        action = decision(predicted_class, confidence)

        logs.append({
            "image_path": image_path,
            "predicted_class": predicted_class,
            "confidence": confidence,
            "action": action
        })

    return logs
