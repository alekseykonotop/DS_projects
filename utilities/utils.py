import pandas as pd

def get_unique_feature_counts(df: pd.DataFrame) -> pd.DataFrame:
    """Функция определяет число уникальных категорий в каждом столбце переданной
    таблицы df и возвращает отсортированный по частоте уникальных значений новый
    датафрейм.

    Args:
        df (pd.DataFrame): объект типа  pandas.DataFrame

    Returns:
        pd.DataFrame: объект типа  pandas.DataFrame
    """
    
    # создаём пустой список
    unique_list = []

    # пробегаемся по именам столбцов в таблице
    for col in df.columns:
        # создаём кортеж (имя столбца, число уникальных значений)
        item = (col, df[col].nunique(), df[col].dtypes) 
        # добавляем кортеж в список
        unique_list.append(item) 
        

    # создаём вспомогательную таблицу и сортируем её
    unique_counts = pd.DataFrame(unique_list,
                                columns=['col_name', 'num_unique', 'type']
                        ).sort_values(by='num_unique',  ignore_index=True)
    
    return unique_counts


