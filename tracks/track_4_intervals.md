# Intervals — Sorting, Merging, and Greedy Scheduling

Track: `track_4_intervals`

Sort-by-start, merge-or-pick-by-end, two-pointer intersections, coverage, and scheduling with heaps.

See generation instructions in ../README.md.

## Problems

| Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Summary Ranges](../problems/0228-summary-ranges/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Merge Intervals](../problems/0056-merge-intervals/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Insert Interval](../problems/0057-insert-interval/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Interval List Intersections](../problems/0986-interval-list-intersections/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Non-overlapping Intervals](../problems/0435-non-overlapping-intervals/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Minimum Number of Arrows to Burst Balloons](../problems/0452-minimum-number-of-arrows-to-burst-balloons/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Remove Covered Intervals](../problems/1288-remove-covered-intervals/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Meeting Rooms](../problems/0252-meeting-rooms/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Meeting Rooms II](../problems/0253-meeting-rooms-ii/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Employee Free Time](../problems/0759-employee-free-time/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Partition Labels](../problems/0763-partition-labels/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Two City Scheduling](../problems/1029-two-city-scheduling/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |


## Extensions (Optional)

| Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Car Pooling](../problems/1094-car-pooling/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Corporate Flight Bookings](../problems/1109-corporate-flight-bookings/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [My Calendar I](../problems/0729-my-calendar-i/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [My Calendar II](../problems/0731-my-calendar-ii/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [My Calendar III](../problems/0732-my-calendar-iii/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Minimum Number of Taps to Open to Water a Garden](../problems/1326-minimum-number-of-taps-to-open-to-water-a-garden/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Video Stitching](../problems/1024-video-stitching/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Remove Interval](../problems/1272-remove-interval/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Data Stream as Disjoint Intervals](../problems/0352-data-stream-as-disjoint-intervals/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| [Minimum Interval to Include Each Query](../problems/1851-minimum-interval-to-include-each-query/readme.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
