# Goji unit cost and margin

Status: **working sheet, started 2026-11-25.** Every figure says where it came
from. Replace estimates with real quotes as they arrive, and date the change.
Price and terms are the locked ones in `GTM_PLAN.md` (sell-now plan v6):
$400, shipping included, 30-day returns with the buyer paying return shipping.

## Parts for one unit

| Part | Prototype (retail, one unit) | Production | Source |
|---|---|---|---|
| Raspberry Pi 5, 8 GB | $174.99 | $174.99 | Micro Center Fairfax shelf price, 2026-11-23 |
| Official active cooler | $9.99 | $9.99 | Micro Center, 2026-11-23 |
| Official 27 W USB-C power supply | $11.99 | $11.99 | Micro Center, 2026-11-23 |
| 64 GB microSD | $42.99 | **~$15 (estimate)** | Prototype: SanDisk Max Endurance, Micro Center. Production: High Endurance in bulk, no quote yet |
| Micro-HDMI to HDMI cable, 1 m | $7.99 | $7.99 | Micro Center, 2026-11-23 |
| Case (printed at home) | **~$3 (estimate)** | **~$3 (estimate)** | Filament only; no figure for printer time or failed prints |
| Box and quickstart card | **~$5 (estimate)** | **~$5 (estimate)** | No quote |
| **Parts total** | **~$256** | **~$228** | |

## Per sale

| Line | Prototype basis | Production basis | Source |
|---|---|---|---|
| Parts | ~$256 | ~$228 | above |
| Outbound shipping | **~$12 (estimate)** | **~$12 (estimate)** | No carrier quote; depends on box size and weight |
| Card processing | $11.90 | $11.90 | Stripe standard, 2.9% + $0.30 on $400 |
| **Cost per unit** | **~$280** | **~$252** | |
| **Left from $400** | **~$120 (30%)** | **~$148 (37%)** | |

Not in the table: sales tax paid on your own purchases, returns and
replacements, your time, hosting (Supabase, storage egress), and the cost of
the five dogfood units.

## What moves the number

| Lever | Effect | State |
|---|---|---|
| Bulk price for the memory card | The largest known saving; assumed above | Need a quote for ~20 and ~100 |
| 4 GB board instead of 8 GB | Unknown until priced; likely the biggest remaining lever | Needs the Pi 5 memory test (the apps session measured ~850 MB in use on a Pi 4). Record the 4 GB shelf price here |
| Board price in quantity | Unknown | Ask an approved Raspberry Pi reseller for 10 and 25 |
| Price | +$49 at $449, +$99 at $499 (before the extra ~$1.40 to $2.90 in processing) | Hold at $400 for launch; nobody has seen a price yet |

## Target

Keep at least a third of the price after parts, shipping and processing. At
$400 that is a cost per unit of about $265 or less. The production estimate
(~$252) clears it; the prototype basket (~$280) does not, almost entirely
because of the retail memory card.

## Open

- [ ] Bulk quote: 64 GB high-endurance microSD
- [ ] 4 GB Pi 5 price, and the result of the memory test
- [ ] Reseller quote for boards at 10 and 25
- [ ] Shipping quote for the real box
- [ ] Printed box and card quote
- [ ] Virginia sales tax: what is collected on sales, and whether resale exemption applies to parts
