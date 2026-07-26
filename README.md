# SafeRoute BD 🇧🇩 🗺️
### Community-Based Safe Route Recommendation System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Leaflet](https://img.shields.io/badge/Leaflet-1.9+-orange.svg)](https://leafletjs.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue.svg)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**SafeRoute BD** is a full-stack, community-driven web application designed to address urban transit vulnerabilities in Bangladesh—specifically targeting the safety needs of women, students, and night-shift commuters.

Unlike standard navigation applications that calculate routes purely to minimize distance ($Distance_{min}$), SafeRoute BD uses a localized cost matrix to compute alternative paths that maximize overall route safety ($Safety_{max}$).

---

## 🚀 Core Problem & Solution

* **The Problem:** Night commuters and vulnerable citizens in urban Bangladesh lack actionable data on street-level hazards. Critical safety metrics—such as unlit alleyways, active crime hotspots, or completely isolated streets—are absent from conventional map tools.
* **The Solution:** A crowdsourced platform where verified citizens log real-time incident reports, streetlight failures, and crowd density. A custom safety-weighted routing engine integrates these social signals to dynamically route users around high-risk zones.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (ES6), **Leaflet.js** (OpenStreetMap canvas engine).
* **Backend:** **Python 3.10+**, **Django 4.2+**, Django REST Framework (DRF).
* **Database:** **PostgreSQL** (with spatial query support).
* **Version Control:** Git & GitHub using modular commit history.

---

## 📊 The Safe Route Algorithm

The platform's core innovation relies on a dynamic weighted cost matrix. Every road segment ($e$) within the spatial graph network receives an adjusted computational cost ($Cost_{total}$):

$$Cost_{total} = Weight_{distance} \times D(e) + Weight_{risk} \times R(e)$$

Where the segment Risk Variable ($R(e)$) is dynamically computed from active database reports:

$$R(e) = \frac{(\text{Recent Crime Logs} \times 4) + (\text{Broken Lights} \times 2) - (\text{Crowd Level} \times 1.5)}{\text{Average User Rating}}$$

If an unlit alleyway accumulates reported incidents, its mathematical cost increases exponentially, directing the routing machine to recommend a safer, well-lit main road instead.

---

## 📁 Repository Structure

```text
SafeRouteBD/
│
├── backend/                  # Core Django Project & API App Modules
│   ├── accounts/             # Authentication & User Profile management
│   ├── reports/              # Crowdsourced incident & streetlight logs
│   ├── routes/               # Safe Route graph processing & algorithm logic
│   └── dashboard/            # Admin moderation & spatial analytics engine
│
├── frontend/                 # Client-side Interface
│   ├── static/               # CSS, JavaScript (Leaflet scripts), and images
│   └── templates/            # Django HTML5 / Bootstrap 5 template files
│
├── .gitignore                # Environment & secret key exclusion rules
├── LICENSE                   # MIT License
├── manage.py                 # Django entrypoint script
├── requirements.txt          # Python dependencies list
└── README.md                 # Project documentation
