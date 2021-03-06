"""
The :mod:`mcmodels.regressors` module implements scikit-learn style estimators
for solving various regression problems. It implements the NadarayaWatson
regressor, and both regularized (L2) and non-regularized non-negative least
squares linear models.
"""
# Authors: Joseph Knox <josephk@alleninstitute.org>
# License: Allen Institute Software License

from .nonnegative_linear import NonnegativeLinear
from .nonnegative_linear import NonnegativeRidge
from .nonnegative_linear import nonnegative_regression
from .nonnegative_linear import nonnegative_ridge_regression

from . import nonparametric
from .nonparametric import NadarayaWatson
from .nonparametric import NadarayaWatsonCV


__all__ = ['NadarayaWatson',
           'NadarayaWatsonCV',
           'NonnegativeLinear',
           'NonnegativeRidge',
           'nonnegative_regression',
           'nonnegative_ridge_regression',
           'nonparametric']
