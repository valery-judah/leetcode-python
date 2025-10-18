# Intervals — Sorting, Merging, and Greedy Scheduling

Track: `track_4_intervals`

Sort-by-start, merge-or-pick-by-end, two-pointer intersections, coverage, and scheduling with heaps.

See generation instructions in ../README.md.

## Problems

| <span style="display:inline-block; min-width: 260px;">Problem</span> | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| <span style="display:inline-block; min-width: 260px;">[Summary Ranges](../problems/0228-summary-ranges/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Merge Intervals](../problems/0056-merge-intervals/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Insert Interval](../problems/0057-insert-interval/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Interval List Intersections](../problems/0986-interval-list-intersections/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Non-overlapping Intervals](../problems/0435-non-overlapping-intervals/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Minimum Number of Arrows to Burst Balloons](../problems/0452-minimum-number-of-arrows-to-burst-balloons/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Remove Covered Intervals](../problems/1288-remove-covered-intervals/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Meeting Rooms](../problems/0252-meeting-rooms/readme.md)</span> | Easy | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Meeting Rooms II](../problems/0253-meeting-rooms-ii/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Employee Free Time](../problems/0759-employee-free-time/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Partition Labels](../problems/0763-partition-labels/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Two City Scheduling](../problems/1029-two-city-scheduling/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |


## Extensions (Optional)

| <span style="display:inline-block; min-width: 260px;">Problem</span> | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|:---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| <span style="display:inline-block; min-width: 260px;">[Car Pooling](../problems/1094-car-pooling/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Corporate Flight Bookings](../problems/1109-corporate-flight-bookings/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[My Calendar I](../problems/0729-my-calendar-i/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[My Calendar II](../problems/0731-my-calendar-ii/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[My Calendar III](../problems/0732-my-calendar-iii/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Minimum Number of Taps to Open to Water a Garden](../problems/1326-minimum-number-of-taps-to-open-to-water-a-garden/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Video Stitching](../problems/1024-video-stitching/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Remove Interval](../problems/1272-remove-interval/readme.md)</span> | Medium | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Data Stream as Disjoint Intervals](../problems/0352-data-stream-as-disjoint-intervals/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
| <span style="display:inline-block; min-width: 260px;">[Minimum Interval to Include Each Query](../problems/1851-minimum-interval-to-include-each-query/readme.md)</span> | Hard | ✖️ | ✖️ | ✖️ |  | 0 | 1 | ✖️ | ✖️ | ✖️ | ✖️                 | ✖️ |  |
