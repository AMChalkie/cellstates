cimport numpy as np
from .cluster cimport Cluster


cpdef np.ndarray[np.float64_t, ndim = 1] get_cluster_distances(Cluster clst)
