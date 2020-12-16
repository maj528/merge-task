def merge(intervals):
    '''
    :param list[list[int]] intervals: eine Liste von numerischen Intervallen
    :rtype: list[list[int]]
    :raises ValueError: wenn Intervalle ungueltig sind
    '''

    if len(intervals)==0:
        raise ValueError('leere Liste')
                  
    # Liste wird sortiert
    intervals.sort(key=lambda x: x[0])

    # Liste wird mit dem kleinsten Intervall gefuellt
    list_merged = [intervals[0]]

    for interval in intervals:
        #prueft ob Eingabe ungueltig ist
        if len(interval) != 2:
            raise ValueError('falsche Eingabe')
        if interval[0] > interval[1]:
            raise ValueError('falsche Eingabe')
        # das vorherige Intervall wird als Varible gespeichert
        previous = list_merged[-1]

        # Untere Zahl des aktuellen Intervalls <= obere Zahl des Vorherigen
        if interval[0] <= previous[1]:
            previous[1] = max(previous[1], interval[1])
        else:
            list_merged.append(interval)

    return list_merged