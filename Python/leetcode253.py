def minMeetingRooms(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """

    ret = 0
    heap = []  # contains end times

    for it in sorted(intervals, key=lambda it: (it.start, it.end)):
        start, end = it.start, it.end

        while heap and heap[0] <= start:
            heappop(heap)

        heappush(heap, end)

        ret = max(ret, len(heap))

    return ret