# Putting a fresh copy of Goji on your memory card

Status: **DRAFT, not published.** Written 2026-11-25 for GTM milestone M3
("consumer reflash doc + recovery SD procedure"). Nobody has followed these
steps on a real unit yet, and no golden image exists to download. Square
brackets mark what only Patrick can fill in. "Before publishing" at the end
lists what is open.

Everything between the two rules is the customer-facing guide.

---

## Putting a fresh copy of Goji on your memory card

Do this only if we have asked you to, or if your Goji will not start and the
steps under "Try these first" did not help.

**This erases everything on the Goji.** Every profile, and everything your
children have written, read and saved, will be gone. There is no way to get
it back afterwards. If the Goji still starts, save anything you want to keep
to a USB stick first: open the item and choose **Save to USB**.

### Try these first

1. **Turn it off and on.** Unplug the power, wait ten seconds, plug it back in.
2. **Check the screen.** Make sure the TV or monitor is on the right HDMI
   input, then move the cable to the other small HDMI port on the Goji.
3. **If it starts but something is wrong,** try Settings → Help and support →
   **Erase this Goji**. That gives you a clean start without these steps. It
   needs your parent PIN.
4. **If you see a red screen that says "This Goji needs service",** write
   down the code on it (K1 or K2) and email us at [support email]. Do not
   reflash yet; we may be able to help without erasing anything.

### What you need

- Another computer (Windows, Mac or Linux) with internet.
- A memory card reader. Many laptops have one; otherwise a USB card reader
  costs a few dollars.
- About [30] minutes, most of it waiting.

### Step 1: Take the memory card out of the Goji

Unplug the Goji's power first. The card is a small black microSD card in a
slot on the [underside / end] of the computer. [Describe or picture how to
reach it with the case on.] Push it gently and it slides out.

### Step 2: Download the Goji image

Download this file to your other computer: [download link].

It is a large file ([size] GB), so it may take a while. Do not open it or
unzip it.

### Step 3: Install Raspberry Pi Imager

Raspberry Pi Imager is a free program from the makers of the computer inside
your Goji. Download it from raspberrypi.com/software and install it.

### Step 4: Write the image to the card

1. Put the memory card in your card reader.
2. Open Raspberry Pi Imager.
3. For the device, choose **Raspberry Pi 5**.
4. For the operating system, scroll to the bottom and choose **Use custom**,
   then pick the Goji file you downloaded.
5. For storage, choose your memory card. Check the size shown matches your
   card (64 GB). **Be careful here: choosing the wrong one erases that drive.**
6. If it asks whether to apply customisation settings, choose **No**.
7. Choose **Write** and wait. It writes the card, then checks it.
8. When it says you can remove the card, take it out.

### Step 5: Put the card back and start the Goji

1. Push the card back into the Goji until it clicks.
2. Plug in the screen, keyboard and mouse, then the power.
3. The first start takes longer than usual, [up to N minutes], while the
   Goji sets itself up. Leave it alone until you see "Welcome to Goji".
4. Follow the setup questions: choose a parent PIN, type your child's name,
   and add Wi-Fi if you want updates.

If you add Wi-Fi, the Goji will fetch the newest version by itself over the
next few hours.

### If that did not work

- **The Imager says the card is too small, or the write fails:** the card may
  be worn out. Email us; see "A replacement card" below.
- **The Goji shows nothing after ten minutes:** check the card is pushed all
  the way in, and try the other HDMI port.
- **Anything else:** email [support email] and tell us what you see on the
  screen.

### A replacement card

If you would rather not do this yourself, or your card has failed, we can
post you a memory card with Goji already on it. [Price or "free within
warranty"; how to ask; how long it takes.] When it arrives, follow Step 1 to
take the old card out, then Step 5.

---

## Before publishing

1. **There is no image to download yet.** The golden image has never been
   built. Step 2 needs a real file, a hosting location (the plan puts large
   files on Cloudflare R2, GTM D13), its size, and a published checksum.
2. **The image must be shrunk for this to work at all.** A full-card image
   will not fit a card a few megabytes smaller, and a replacement card is
   unlikely to be the same model. `deployment/image/shrink-image.sh` exists;
   it has not run on a real image. Each unit grows its storage on first boot.
3. **Which image does a customer get?** The image carries the release it was
   built with, and the unit updates itself afterwards. That works as long as
   every later release can still be installed from the image's version
   (stepping stones, contract §12.1). Decide how often the download is
   refreshed.
4. **Stable channel.** The downloadable image must be a stable-channel image
   with SSH off, never a dev or beta build.
5. **Getting at the card.** Step 1 depends on the case. Check it with the
   printed case on, and add a photo or drawing. If the card cannot be reached
   without opening the case, say so and say how.
6. **First-boot time** on a 64 GB card is unmeasured. Storage growth runs
   then, before the app starts.
7. **Imager wording.** The menu names in Step 4 are from memory of the
   current Imager and must be checked against the version customers will
   download. In particular confirm that declining customisation is offered
   and is the right choice: the Goji image must not be given a user, Wi-Fi or
   SSH by the Imager.
8. **Save to USB** is offered in Step 0 as the way to keep work. It ships
   with printing (GTM D19) and saves one item at a time. There is no
   whole-device backup; say so plainly or build one.
9. **The "needs service" codes** (K1, K2) come from the lockdown launcher
   (`docs/LOCKDOWN.md`). Confirm what support can actually do for each
   before telling customers to email first.
10. **Replacement card policy:** price, warranty terms, turnaround, and the
    procedure on your side (flash, boot once to check? no: a card must not be
    booted before it ships, because first boot is what makes each unit
    unique; flash and verify only).
11. **Fill the brackets:** support email, download link and size, first-boot
    time, card location, replacement terms.

## Your side: making a recovery card

For a card you post to a customer:

1. Flash the current stable golden image to a new 64 GB high-endurance card
   with Raspberry Pi Imager ("Use custom", no customisation).
2. Let the Imager verify the write.
3. Do **not** boot the card. First boot generates the unit's identity and
   locks it down; a card that has been booted is no longer a clean image.
4. Label it with the image version and the date.
