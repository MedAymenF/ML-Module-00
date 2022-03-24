import numpy as np


class TinyStatistician:
    @staticmethod
    def mean(x):
        if not isinstance(x, (list, np.ndarray)):
            print('x has to be a list or a numpy array.')
            return None
        error_msg = f'x must not contain non-numeric types.'
        if isinstance(x, np.ndarray) and not np.issubdtype(x.dtype, np.number):
            print(error_msg)
            return None
        elif isinstance(x, list):
            types = set(map(type, x))
            if len(types) > (int in types) + (float in types):
                print(error_msg)
                return None
        u = 0
        for elem in x:
            u += elem
        u /= len(x)
        return float(u)

    @staticmethod
    def percentile(x, p):
        if not isinstance(x, (list, np.ndarray)):
            print('x has to be a list or a numpy array.')
            return None
        error_msg = f'x must not contain non-numeric types.'
        if isinstance(x, np.ndarray) and not np.issubdtype(x.dtype, np.number):
            print(error_msg)
            return None
        elif isinstance(x, list):
            types = set(map(type, x))
            if len(types) > (int in types) + (float in types):
                print(error_msg)
                return None
        if not isinstance(p, int) or p < 0 or p > 99:
            print('p has to be an int from 0 to 99.')
            return None
        x = sorted(x)
        idx = p * len(x) // 100
        return float(x[idx])

    @staticmethod
    def median(x):
        return TinyStatistician.percentile(x, 50)

    @staticmethod
    def quartile(x):
        p_25 = TinyStatistician.percentile(x, 25)
        if p_25 is None:
            return None
        p_75 = TinyStatistician.percentile(x, 75)
        return [float(p_25), float(p_75)]

    @staticmethod
    def var(x):
        u = TinyStatistician.mean(x)
        if u is None:
            return None
        v = 0
        for elem in x:
            v += (elem - u) ** 2
        v /= len(x)
        return float(v)

    @staticmethod
    def std(x):
        v = TinyStatistician.var(x)
        if v is None:
            return None
        return float(v ** 0.5)
