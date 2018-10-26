from histomicstk.segmentation.nuclear.min_model import *
import skimage
import numpy as np


def _list_to_array(shape, X, Y):
    assert len(shape) == 2
    img = np.zeros(shape)

    for x,y in zip(X,Y):
        #print x, y
        img[x, y] = 1
    #print np.max(coord)
    return img


def test_seed_contours():
    # Verifies that `seed_contours_slow()` and `seed_contours()` return the same
    # results.

    I = skimage.io.imread('/tmp/01.jpg')
    I=np.average(I, 2).astype(np.int)
    skimage.io.imsave('/tmp/01_gray.tif', I)
    I=skimage.filters.gaussian(I,3, preserve_range=True)
    skimage.io.imsave('/tmp/01_g.tif', I)
    [X_s, Y_s, Min_s, Max_s] = seed_contours_slow(I)
    img = _list_to_array(I.shape, X_s,Y_s)
    skimage.io.imsave('/tmp/01_s.tif', img)
    [X, Y, Min, Max] = seed_contours(I, Delta=None)
    img = _list_to_array(I.shape, X,Y)
    skimage.io.imsave('/tmp/01_.tif', img)
    print "__________________________________"
    print X_s.shape
    print X.shape
    print "__________________________________"
    assert X_s == X
    assert Y_s == Y
    assert Min_s == Min
    assert Max_s == Max