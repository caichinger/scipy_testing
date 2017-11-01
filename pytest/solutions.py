
import pytest
import numpy as np
import pandas as pd


#%%
@pytest.fixture
def create_df():
    df = pd.DataFrame({'a': [1, 2], 
                       'b': [2, 3]})
    return df


@pytest.fixture
def create_data(tmpdir, create_df):
    df = create_df
    path = tmpdir.join('df.csv')
    df.to_csv(path, index=None)
    return path


def test_with_tmpdir_fixture(create_data, create_df):
    df_expected = create_df
    path = create_data
    df_actual = pd.read_csv(path)
    pd.testing.assert_frame_equal(df_actual, df_expected)


#%%
def integrate(f, x):
    y = f(x)
    return np.sum((y[:-1] + y[1:]) * np.diff(x)) / 2


@pytest.mark.parametrize('fun,integral', [(lambda x: x, 0.5), 
                                          (lambda x: 0*x + 1, 1)])
def test_integrate(fun, integral):
    x = np.linspace(0, 1, 100)
    assert integrate(fun, x) == integral


#%%
def some_exception():
    raise ZeroDivisionError('O.o')


def test_some_exception():
    with pytest.raises(ZeroDivisionError) as excinfo:
        some_exception()
    assert excinfo.value.args[0] == 'O.o' 



if __name__ == '__main__':
    pytest.main([__file__])
    