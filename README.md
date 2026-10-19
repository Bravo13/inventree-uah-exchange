# inventree-uah-exchange

[InvenTree](https://inventree.org) currency exchange plugin that uses the official daily rates of the
National Bank of Ukraine ([bank.gov.ua](https://bank.gov.ua/en/open-data/api-dev)). Unlike the built-in
plugin (frankfurter.app / ECB), it includes **UAH**. No API key needed.

## Install

Admin center → Plugins → Install Plugin:

| Field | Value |
|---|---|
| Package name | `inventree-uah-exchange` |
| Source URL | `git+https://github.com/Bravo13/inventree-uah-exchange.git@v0.1.0` |

Or add to `plugins.txt`:

```
inventree-uah-exchange @ git+https://github.com/Bravo13/inventree-uah-exchange.git@v0.1.0
```

Then:

1. Activate **UAH Exchange (NBU)** in the plugin list and restart server + worker.
2. Settings → Pricing → *Exchange Rate Update Plugin*: select it.
3. Add `UAH` to *Supported Currency Codes* if it isn't there yet.
4. Settings → Pricing → *Update Now* (otherwise rates refresh on the next daily task).

## Notes

- NBU publishes ~45 currencies as "UAH per 1 unit"; the plugin converts them to the InvenTree base
  currency. Currencies the NBU doesn't publish are skipped with a warning in the log.
- The NBU sets new rates once per business day.

## Development

```sh
python -m pytest tests   # conversion logic only, no InvenTree needed
```
