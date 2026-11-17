# Goji privacy policy (draft for v1)

Status: **DRAFT, not published.** Written 2026-11-17 against `GTM_PLAN.md` (D2, D12),
`goji-cloud/OTA_CONTRACT.md` §8 and §12.4, and the code on `kodi-computer` `main`.
It needs a lawyer's review before it goes on the website or in the box. The
section "Before publishing" at the end lists what is still open.

Everything between the two rules below is the policy text. Square brackets
mark details only Patrick can fill in.

---

## Goji privacy policy

Effective [date]. Narrow Road Studios ("we") makes the Goji learning computer.

### The short version

- Your child's work stays on the Goji. Their writing, journal, reading, typing,
  math, code, notes and profile never leave the device. We cannot see them.
- Goji has no accounts, no ads, no tracking and no microphone or camera features.
- If you connect Goji to Wi-Fi, it does two things online: it checks for
  software updates, and it sends a small technical health report. The health
  report has nothing about your child in it, and you can turn it off.
- Goji works with no internet connection at all.

### What stays on the Goji

All of this is stored only on the device's memory card:

- Profiles: the name you type for each child.
- Everything a child makes or does: documents, notebooks, journal entries,
  code, flashcards, reading and typing progress, math results, imported PDFs.
- The parent PIN, stored in a scrambled form that cannot be read back.
- Your Wi-Fi password, if you connect to Wi-Fi, stored encrypted.

We have no copy of any of it and no way to retrieve it. If the memory card is
lost or erased, that information is gone.

### What Goji does online

Goji only goes online if you connect it to Wi-Fi. It has a firewall that
blocks everything except the following.

**Software updates.** Goji regularly asks our update server whether a new
version exists and downloads it if so. The request contains no information
about you or your child.

**The device health report.** About once an hour while online, and after each
update, Goji sends a short report so we can tell whether updates are
installing correctly. It contains exactly these items and nothing else:

| Item | Example | Why we collect it |
|---|---|---|
| A random install number | `8c1e2f0a-…` | To tell one Goji from another. It is made up at random on the device. It is not the serial number and is not linked to your name, order or address. |
| Update channel | `stable` | Which stream of updates the Goji follows. |
| Software versions | `1.2.0` | The app version and three internal version numbers (updater, data format, system image). |
| Update status | `committed` | Whether the Goji is idle, downloading or installing. |
| Result of the last update | `OK_COMMITTED`, from `1.1.0` to `1.2.0`, the time, and a short machine-written note such as "health ok in 41s" | To see whether an update worked or was rolled back. The note never contains file names, profile names or anything a person typed. |
| Time since the Goji was switched on | `86400` seconds | To tell a fresh restart from a long-running device when diagnosing a problem. |
| Hardware model | `Raspberry Pi 5 Model B Rev 1.0` | To know which hardware a problem affects. |
| Memory size | `8064` MB | Same reason. |
| Free storage space | `41230` MB | To avoid sending an update that will not fit. |
| Time the report was sent | `2026-11-03T02:15:00Z` | To order reports. |

The health report never includes names, the number of profiles, anything a
child wrote or did, which apps were used, your Wi-Fi network name, or log
files.

**Your internet address.** Any device that contacts a server reveals its
internet (IP) address to that server; that is how the internet works. We do
not store your IP address with health reports. For a short time our server
keeps a scrambled, daily-changing fingerprint of the address so that it can
refuse floods of fake reports. Our hosting provider may keep its own
short-term connection logs.

**The clock and address lookups.** Like any networked computer, Goji asks
public time servers what time it is and uses your network's name lookup
service (DNS) to find our update server.

Goji does not contact any other company's servers. The browser inside Goji
is locked to the Goji app and cannot open websites.

### Turning the health report off

On the Goji: Settings (the gear) → Software update → Device health report →
Turn off. It asks for your parent PIN.

Turning it off stops the health report only. Goji still checks for and
installs updates, so it stays secure. You can turn it back on the same way.

### How long we keep health reports

- We keep the record of each update result for up to 365 days, then delete it.
- We keep one current record per Goji (its latest versions and status) for
  [as long as the Goji keeps reporting, and delete it 365 days after its last
  report].
- Only Narrow Road Studios can read these records. We do not sell or share
  them, and we do not combine them with order information.

### When you buy a Goji

Payment is handled by Stripe. We do not see or store your card number. From
your order we receive your name, email address, shipping address and what you
bought. We use them to ship your Goji, handle returns and answer support
requests, and we keep order records for as long as tax and accounting rules
require. We do not use them for marketing unless you ask to hear from us.

Order information is never linked to a Goji's install number.

### When you ask for help

If you email us, we keep the conversation so we can help you. If we ask for a
log file, you choose whether to make one: Settings → Help and support → Save
logs to USB. The file contains technical logs from the Goji's software. It
does not contain anything your child wrote, read or saved. You decide whether
to send it to us.

### Children's privacy

Goji is made for children and is set up by a parent. We do not collect
personal information from children. Goji has no child accounts, no sign-in, no
messaging with people outside the home, and no way for a child to send
information to us or anyone else.

### Erasing a Goji

Settings → Help and support → Erase this Goji removes every profile and
everything saved on the device, plus saved Wi-Fi networks. It needs your
parent PIN and cannot be undone. Do this before giving or selling the Goji to
someone else.

The random install number is kept through an erase so that we can still tell
updates are working on that device. To remove the health records we hold for
your Goji, email us [how the owner identifies their device].

### Your choices and rights

- You can use Goji without ever connecting it to the internet.
- You can turn the health report off at any time.
- You can ask what order and support information we hold about you, and ask
  us to correct or delete it, by emailing [support email]. We will answer
  within [30] days.

### Future features

A later update may add an optional parent app. If it does, it will need your
permission before any information leaves the Goji, and we will update this
policy first and tell you what changes.

### Changes to this policy

If we change this policy we will post the new version at [URL] with a new
effective date. If a change means Goji would send anything new from the
device, we will say so in the update's release notes before it installs.

### Contact

Narrow Road Studios
[postal address]
[support email]

---

## Before publishing

Open items, most important first.

1. **Lawyer review.** This is a plain-language draft, not legal advice. It
   makes specific promises ("never", "cannot see", "exactly these items") that
   are true of the code today and become liabilities if the code drifts. In
   particular, ask counsel about COPPA (the draft's position is that no
   personal information is collected from children), state privacy laws, and
   whether the Virginia sales-tax and returns terms belong in a separate terms
   of sale.
2. **Retention has to be made true.** The policy promises deletion after 365
   days. Today the purge of `ota_device_events` is a manual SQL statement in
   `goji-cloud/HUMAN_CHECKLIST.md`, not a scheduled job, and nothing deletes
   an `ota_devices` row at all. Either schedule both or change the wording.
3. **Decide the `ota_devices` retention.** The bracketed text proposes
   deleting a device's row 365 days after its last report. The contract does
   not say; it needs a line in `OTA_CONTRACT.md` §8.5.
4. **Deleting one device's records on request.** The policy offers it, but an
   owner has no way to tell us their install number: it is not shown anywhere
   on the Goji. Showing it under Software update would close that. Until then
   the honest wording is that turning the report off stops new records and
   existing ones expire after 365 days.
5. **The hardware fields are in.** `GTM_PLAN.md` still lists the extra
   heartbeat fields (hardware model, memory, uptime, internal versions) as an
   open question. The contract already records Patrick's answer (2026-10-24)
   that they are sent and must be named here, and this draft names them. The
   "Open" line in `GTM_PLAN.md` §1 can be closed.
6. **Hosting provider logs.** The update server and health-report function run
   on Supabase. Confirm what connection logs Supabase keeps and for how long,
   and whether the policy should name it.
7. **Fill the brackets:** effective date, postal address, support email,
   policy URL, response time.
8. **Printed one-pager.** `TODO.md` has "Printed privacy one-pager for the
   box"; its linked draft describes the paired parent-app product, which is
   not v1. "The short version" above is the right basis for the card.

## What each claim rests on

So a reviewer can check the policy against the product.

| Claim | Where it is enforced |
|---|---|
| Child data never leaves the device | v1 runs in stub sync mode (`GOJI_SYNC_MODE=stub`, written by `goji-updater bake`); the sync agent is disabled (`units.json`); `OTA_CONTRACT.md` §8.4 forbids child data in the heartbeat |
| The health report is exactly this list | `updater/goji_updater/heartbeat.py` builds the payload; a closed-set test fails if a key is added; the cloud function rejects unknown fields |
| The note never contains user text | `heartbeat.py` truncates `detail` to 200 characters and rejects any containing the data path; contract §8.2 |
| IP address not stored | `OTA_CONTRACT.md` §8.4; the heartbeat tables have no IP column (schema test in `goji-cloud`) |
| Opt-out stops reports, not updates | `OTA_CONTRACT.md` §12.4; `heartbeat.should_send`; PIN-gated route `POST /api/updates/heartbeat` |
| Firewall blocks everything else | `kodi-computer/deployment/image/nftables-goji.conf` (outbound: DNS, DHCP, NTP, ICMP, HTTPS, local printing) |
| Browser cannot open websites | Chromium managed policy `URLBlocklist: *` with a localhost allowlist (`deployment/image/files/chromium-policy.json`) |
| Wi-Fi password encrypted | `backend/utils/crypto.py` (per-device key, never shared between units) |
| PIN not readable | `backend/utils/pin.py` (PBKDF2 hash) |
| Log file has no child data | `backend/routes/support.py` reads only the log directory, updater status and service journals, never the database or data directory |
| Erase removes everything | `updater/goji_updater/factoryreset.py` (data, logs, backups, saved Wi-Fi, browser storage); install ID kept per contract §8.2 |
