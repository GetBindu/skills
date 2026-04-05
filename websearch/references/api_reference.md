# websearch API Reference

## Backend
DuckDuckGo HTML search (`https://html.duckduckgo.com/html/?q=...`). No API key required.

## Dependencies
- `requests` — HTTP client
- `beautifulsoup4` — HTML parsing

## CLI flags
| Flag | Description | Default |
|------|-------------|---------|
| `--query` | Search query (required) | — |
| `--max-results` | Maximum results to return | 10 |
| `--science` | Append science-focused terms to query | false |
| `--format` | Output format: `summary`, `detailed`, or `json` | `summary` |

## Output schema (json mode)

```json
[
  {
    "title": "Result title",
    "url": "https://example.com/page",
    "display_url": "example.com/page",
    "snippet": "Short excerpt of matched content..."
  }
]
```

## Rate limiting
DuckDuckGo HTML endpoint has no documented rate limit, but is intended for
light use. For heavy queries, consider the DuckDuckGo Instant Answer API
or a paid provider (Serper, Brave Search, etc.).

## Known limitations
- HTML scraping is fragile to DuckDuckGo layout changes
- No pagination support — capped at what DDG returns on page 1
- Non-English queries may return mixed regional results
- `--science` mode just appends `"research" OR "scientific" OR "study"` to the query
