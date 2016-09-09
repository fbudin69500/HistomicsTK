import numpy as np
import scipy.ndimage.measurements as ms


def DeleteLabel(Label, Index):
    """
    Deletes objects with values in 'Index' from label image, writing them over
    with zeros to assimilate with background.

    Parameters
    ----------
    Label : array_like
        A label image generated by segmentation methods.
    Index : array_like
        An n-length array of strictly positive integer values to delete from
        'Label'.

    Returns
    -------
    Deleted : array_like
        A label image where all values in 'Index' are set to zero.

    Notes:
    ------
    A call to CondenseLabel can squeeze label image values to fill in gaps from
    deleted values.

    See Also
    --------
    histomicstk.segmentation.label.CondenseLabel
    """

    # initialize output
    Deleted = Label.copy()

    # get extent of each object
    Locations = ms.find_objects(Deleted)

    # fill in new values
    for i in np.arange(Index.size):
        if Locations[Index[i]-1] is not None:
            Patch = Deleted[Locations[Index[i]-1]]
            Patch[Patch == Index[i]] = 0

    return Deleted
