"""
The :mod:`mcmodels.regressors.nonparametric` module implements Nonparametric
regression models and the polynomial family of kernels. This module includes
NadarayaWatson regression and the general Polynomial kernel.
"""
# Authors: Joseph Knox <josephk@alleninstitute.org>
# License: Allen Institute Software License

from .nadaraya_watson import NadarayaWatson, NadarayaWatsonCV
from . import kernels

__all__ = ['NadarayaWatson',
           'NadarayaWatsonCV',
           'kernels']
