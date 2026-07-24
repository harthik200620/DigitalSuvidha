"""services/catalog.py — Digital Suvidha company facts + service catalog + business-type guide,
embedded directly into the `consult` scenario's prompt as static reference text (not a tool call —
same precedent as the sibling repos' CLINIC["services"]/PRODUCT_CATALOG).

Company facts (legal name, CIN, founder, incorporation date, Delhi office) are real, researched
from public records (MCA/company-registry lookups) and Digital Suvidha's own site. Service
pricing is a constructed, realistic India-agency estimate — Upendra Yadav's own published prices
($50/$90) are from a freelance-marketplace profile aimed at international clients, not
representative of direct-client India pricing, so they were not used verbatim. Spot-check against
a real rate card before a live pitch — same "illustrative demo data" precedent every sibling
repo's case data already uses.
"""
from __future__ import annotations

COMPANY = {
    "legal_name": "Digital Suvidha Private Limited",
    "brand_name": "Digital Suvidha",
    "brand_name_hi": "डिजिटल सुविधा",
    "short_name": "Digital Suvidha",
    "short_name_hi": "डिजिटल सुविधा",
    "founder_name": "Upendra Yadav",
    "founder_alias": "Digital Yadav",
    "region": "Delhi",
    "since": "2016",   # Upendra's own years in digital marketing, NOT the company's 2021
                        # incorporation year — keep this distinction precise in every prompt.
}

SERVICE_CATALOG = {
    "Website Packages": [
        {"name": "Starter Site", "price": "₹9,999 one-time",
         "for": ["businesses with no website yet", "single-location shops", "simple service providers"],
         "note": "up to 5 pages, mobile-responsive, WhatsApp click-to-chat button, 1 round of revisions"},
        {"name": "Growth Site + SEO", "price": "₹24,999 one-time",
         "for": ["businesses wanting to be found on Google", "service businesses taking enquiries online"],
         "note": "up to 10 pages, on-page SEO, Google Business Profile setup, enquiry/contact forms"},
        {"name": "Premium Full-Service", "price": "₹49,999 one-time",
         "for": ["businesses wanting a complete, ready-to-grow online presence"],
         "note": "everything in Growth, plus social media page setup + branding kit and a first-month content calendar"},
    ],
    "SEO & Visibility Add-ons": [
        {"name": "Google Business Profile setup & optimization", "price": "₹4,999 one-time"},
        {"name": "Local SEO audit", "price": "₹2,999 one-time"},
        {"name": "Keyword-targeted blog article", "price": "₹1,499 per article"},
    ],
    "Social Media & WhatsApp": [
        {"name": "Social media page setup & branding kit", "price": "₹6,999 one-time"},
        {"name": "WhatsApp Business setup & broadcast marketing", "price": "₹4,999 one-time"},
    ],
    "Ongoing Growth Retainers": [
        {"name": "Growth Retainer (SEO + social media management)", "price": "₹12,999 per month"},
        {"name": "1-on-1 Digital Growth Consultation", "price": "free, no obligation"},
    ],
}

# Business type → the services above that actually fit — the "what should I get for my business"
# answer, keyed loosely (lowercase, a couple of common synonyms per type).
BUSINESS_TYPE_GUIDE = {
    "restaurant": ["Google Business Profile setup & optimization", "Starter Site"],
    "cafe": ["Google Business Profile setup & optimization", "Starter Site"],
    "local shop": ["Starter Site", "WhatsApp Business setup & broadcast marketing"],
    "kirana": ["Starter Site", "WhatsApp Business setup & broadcast marketing"],
    "boutique": ["Social media page setup & branding kit", "Growth Site + SEO"],
    "clothing": ["Social media page setup & branding kit", "Growth Site + SEO"],
    "d2c": ["Social media page setup & branding kit", "Growth Site + SEO"],
    "clinic": ["Growth Site + SEO", "Google Business Profile setup & optimization"],
    "doctor": ["Growth Site + SEO", "Google Business Profile setup & optimization"],
    "gym": ["Growth Site + SEO", "Social media page setup & branding kit"],
    "salon": ["Growth Site + SEO", "Google Business Profile setup & optimization"],
    "consultant": ["Starter Site", "Growth Site + SEO"],
    "freelancer": ["Starter Site"],
    "no website yet": ["Starter Site"],
    "no online presence": ["Starter Site"],
}


def format_catalog_for_prompt() -> str:
    lines = []
    for category, items in SERVICE_CATALOG.items():
        lines.append(f"{category}:")
        for it in items:
            for_whom = f" — for {', '.join(it['for'])}" if it.get("for") else ""
            note = f" ({it['note']})" if it.get("note") else ""
            lines.append(f"  - {it['name']}: {it['price']}{for_whom}{note}")
    return "\n".join(lines)


def format_business_guide_for_prompt() -> str:
    lines = []
    for biz, services in BUSINESS_TYPE_GUIDE.items():
        lines.append(f"  - {biz}: {', '.join(services)}")
    return "\n".join(lines)
