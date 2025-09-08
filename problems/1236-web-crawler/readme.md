# 1236. Web Crawler

## Quick Facts

- URL: [Web Crawler](https://leetcode.com/problems/web-crawler/)
- Function: `crawl`
- Signature: `(urls: list[str], edges: list[list[int]], startUrl: str)  -> list[str]`
- Primary pattern: **String**

## Constraints

- `1 <= urls.length <= 1000`
- `1 <= urls[i].length <= 300`
- `startUrl is one of the urls.`
- `Hostname label must be from 1 to 63 characters long, including the dots, may contain only the ASCII letters from 'a' to 'z', digits  from '0' to '9' and the hyphen-minus character ('-').`
- `The hostname may not start or end with the hyphen-minus character ('-').`
- `See:  https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames`
- `You may assume there're no duplicates in url library.`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| # | Idea | When to use | Correctness invariant | Time | Space |
|---|------|-------------|-----------------------|------|-------|
| A | [primary idea] | [scenario] | [invariant] | O(n) | O(n) |
| B | [alternative] | [scenario] | [invariant] | O(n log n) | O(1) |
| C | [reject] | [why not] | [violated invariant] | - | - |

## Edge Cases Checklist

- [case 1]
- [case 2]
- [case 3]

## Correctness Sketch

[state the invariant and why it guarantees correctness]

## Implementation

- `solutions.py` should expose:
  - `ALL_SOLUTIONS = {"...": fn, "...": fn}`
  - Short notes on tradeoffs and pitfalls.

## Tests

- Deterministic cases covering all edge cases above
- Optional fuzz/property checks as applicable
- Run: `pytest -q -k "1236"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1242 | Medium | [Web Crawler Multithreaded](../1242-web-crawler-multithreaded/readme.md) | [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) |

## Examples

### Example 1

```text
interface HtmlParser {{
  // Return a list of all urls from a webpage of given url.
  public List<String> getUrls(String url);
}}
```

### Example 2

```text
Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
Output: [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]
```

### Example 3

```text
Input: 
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
startUrl = "http://news.google.com"
Output: ["http://news.google.com"]
Explanation: The startUrl links to all other pages that do not share the same hostname.
```

## References

- LeetCode problem and editorial links
