import candidate_windows as w
import preproc
import classifiser
import cv2
import numpy as np

labels = ['n01615121', 'n02099601', 'n02123159',
          'n02129604', 'n02317335', 'n02391049',
          'n02410509', 'n02422699', 'n02481823', 'n02504458']



def classify_image(image):
    b, _ = w.get_edge_boxes(image, 50)
    windows = w.extract_windows(image, b)

    windows_scores = []
    for window in windows:
        img = preproc.normalize(window)
        img_feature = preproc.extract_feature(img)
        windows_scores.append(max(classifiser.confidence_score(img_feature)))

    max_v = np.amax(windows_scores)
    top_window = np.where(windows_scores == max_v)
    top_window = windows[top_window[0][0]]

    img = preproc.normalize(top_window)
    img_feature = preproc.extract_feature(img)
    prediciton = classifiser.make_prediction(img_feature)

    return labels[prediciton[0]]


#im = cv2.imread('data/test/images/66.JPEG')
#label = classify_image(im)
#print(label)