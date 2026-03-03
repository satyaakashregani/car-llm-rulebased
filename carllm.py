"""
╔══════════════════════════════════════════════════════════════════════╗
║         🚗  INDIA CARS LLM  –  Pre-Trained Chat Engine              ║
║         Covers Indian car market  2000 → 2026                       ║
║         No external API  |  Fully embedded knowledge base            ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import re
import difflib
import textwrap

# ══════════════════════════════════════════════════════════════════════
#  KNOWLEDGE BASE  –  Every major car sold in India (2000–2026)
# ══════════════════════════════════════════════════════════════════════

CAR_DB = {

    # ─────────────────────────────── MARUTI SUZUKI ────────────────────
    "maruti alto": {
        "brand": "Maruti Suzuki",
        "model": "Alto",
        "years_sold": "2000–present",
        "category": "Hatchback",
        "brief": (
            "The Alto is India's best-selling car for many years running. "
            "Lightweight, fuel-efficient and extremely affordable, it has been the "
            "entry-point to car ownership for millions of Indian families. "
            "The current generation (Alto K10) launched in 2022 rides on a new platform."
        ),
        "variants": ["Std (Alto 800)", "LX", "LXi", "VXi", "VXi+", "Alto K10 – Std/VXi/VXi+/ZXi/ZXi+"],
        "engine_options": {
            "0.8L 3-cyl (F8D)": "796 cc, 47 PS, 69 Nm – Alto 800 (2000–2022)",
            "1.0L K10C DualJet": "998 cc, 67 PS, 89 Nm – Alto K10 (2022–)",
        },
        "transmission": ["5-speed MT", "5-speed AMT (K10)"],
        "mileage": "22–24 km/l (ARAI)",
        "safety": "1-star Global NCAP (2014 test on older model)",
        "key_features": [
            "Dual airbags (newer variants)",
            "ABS with EBD",
            "Power steering",
            "Central locking",
            "USB charging port",
            "Rear parking sensors",
        ],
        "price_range": "₹3.55 lakh – ₹5.30 lakh (ex-showroom, 2024)",
        "rivals": ["Renault Kwid", "Datsun Redi-GO (discontinued)", "Maruti S-Presso"],
        "fun_facts": "Alto 800 held India's best-seller title for over a decade consecutively.",
    },

    "maruti wagon r": {
        "brand": "Maruti Suzuki",
        "model": "WagonR",
        "years_sold": "1999–present",
        "category": "Tall-boy Hatchback",
        "brief": (
            "WagonR pioneered the tall-boy design in India. The 2019 generation moved to a "
            "new platform with two engine options. Loved for its boxy practicality, "
            "it remains a top-3 seller consistently."
        ),
        "variants": ["Lxi", "Vxi", "Vxi+", "Zxi", "Zxi+", "Vxi CNG", "Zxi CNG"],
        "engine_options": {
            "1.0L K10C": "998 cc, 67 PS, 89 Nm",
            "1.2L K12M": "1197 cc, 83 PS, 113 Nm",
            "CNG versions": "Available on 1.0L – ~66 km/kg",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "24.43 km/l (1.0L MT ARAI)",
        "safety": "4-star Global NCAP (2021, adult)",
        "key_features": [
            "SmartPlay Studio infotainment (7-inch)",
            "Apple CarPlay / Android Auto",
            "360-degree camera (top variant)",
            "Keyless entry",
            "Push-button start",
            "Automatic climate control",
        ],
        "price_range": "₹5.54 lakh – ₹7.43 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Grand i10 Nios", "Tata Tiago", "Maruti Celerio"],
        "fun_facts": "WagonR is one of very few cars to have survived 25+ years with zero sales breaks in India.",
    },

    "maruti swift": {
        "brand": "Maruti Suzuki",
        "model": "Swift",
        "years_sold": "2005–present",
        "category": "Hatchback / Sports Hatchback",
        "brief": (
            "Swift changed the definition of a hatchback in India — sporty styling, "
            "sharp handling and an enthusiast following. The 4th generation (2024) brings "
            "a new Z-series engine and refreshed design."
        ),
        "variants": ["Lxi", "Vxi", "Vxi AMT", "Zxi", "Zxi+", "Zxi+ AMT"],
        "engine_options": {
            "1.2L Z12E (2024)": "1197 cc, 82 PS, 112 Nm – new 3-cyl",
            "1.2L K12N DualJet (2021–2023)": "1197 cc, 90 PS, 113 Nm",
            "1.3L DDiS (diesel, discontinued 2020)": "1248 cc, 75 PS, 190 Nm",
        },
        "transmission": ["5-speed MT", "6-speed AMT"],
        "mileage": "24.80 km/l (ARAI 2024 MT)",
        "safety": "3-star Global NCAP (3rd gen); 4th gen not yet tested (as of 2024)",
        "key_features": [
            "9-inch SmartPlay Pro+ infotainment",
            "HUD (Head-Up Display) – 4th gen",
            "6 airbags (top variant)",
            "360 camera",
            "ESP & Hill Hold",
            "LED projector headlights",
            "USB-C fast charging",
        ],
        "price_range": "₹6.49 lakh – ₹9.64 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai i20", "Tata Altroz", "Honda Jazz (discontinued)", "VW Polo (discontinued)"],
        "fun_facts": "Swift is consistently in India's top-5 monthly sales charts since its launch.",
    },

    "maruti baleno": {
        "brand": "Maruti Suzuki",
        "model": "Baleno",
        "years_sold": "2015–present",
        "category": "Premium Hatchback",
        "brief": (
            "Baleno is Maruti's premium hatchback sold via NEXA dealerships. "
            "The 2022 2nd generation brought a bold new design, updated tech and "
            "stronger safety. It's India's best-selling premium hatchback."
        ),
        "variants": ["Sigma", "Delta", "Delta AMT", "Zeta", "Zeta AMT", "Alpha", "Alpha AMT"],
        "engine_options": {
            "1.2L DualJet K12N": "1197 cc, 90 PS, 113 Nm",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "22.35 km/l (MT ARAI)",
        "safety": "2-star Global NCAP (2022 test on new gen — controversial)",
        "key_features": [
            "9-inch SmartPlay Pro+ with wireless Apple CarPlay/Android Auto",
            "360° surround-view camera",
            "Head-Up Display",
            "6 airbags (Alpha)",
            "Arkamys sound system",
            "LED headlights & DRL",
            "Keyless entry & push-button start",
            "Auto AC",
        ],
        "price_range": "₹6.61 lakh – ₹9.88 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai i20", "Tata Altroz", "Honda Jazz (disc.)", "Toyota Glanza"],
        "fun_facts": "Baleno was India's first car to be exported to Japan (as Suzuki Baleno) from an Indian plant.",
    },

    "maruti dzire": {
        "brand": "Maruti Suzuki",
        "model": "Dzire",
        "years_sold": "2008–present",
        "category": "Sub-4m Compact Sedan",
        "brief": (
            "Dzire (formerly Swift Dzire) is India's most popular compact sedan. "
            "The 4th generation (2024) rides on a new platform with a 3-cylinder engine "
            "and promises best-in-class efficiency."
        ),
        "variants": ["Lxi", "Vxi", "Vxi AMT", "Zxi", "Zxi+ AMT", "CNG variants"],
        "engine_options": {
            "1.2L Z12E (2024)": "1197 cc, 82 PS, 112 Nm – 3-cyl",
            "1.2L DualJet K12N (2017–2023)": "1197 cc, 90 PS, 113 Nm",
            "1.3L DDiS diesel (disc.)": "1248 cc, 75 PS",
        },
        "transmission": ["5-speed MT", "6-speed AMT"],
        "mileage": "24.79 km/l (MT, ARAI 2024)",
        "safety": "3-star Global NCAP",
        "key_features": [
            "7-inch or 9-inch SmartPlay infotainment",
            "Apple CarPlay / Android Auto",
            "Rear AC vents",
            "Keyless entry",
            "Cruise control",
            "6 airbags (top variant)",
            "HUD (2024 top trims)",
        ],
        "price_range": "₹6.79 lakh – ₹9.69 lakh (ex-showroom, 2024)",
        "rivals": ["Honda Amaze", "Hyundai Aura", "Tata Tigor"],
        "fun_facts": "Dzire topped India's car sales chart in multiple calendar years.",
    },

    "maruti vitara brezza": {
        "brand": "Maruti Suzuki",
        "model": "Brezza (formerly Vitara Brezza)",
        "years_sold": "2016–present",
        "category": "Sub-4m Compact SUV",
        "brief": (
            "Brezza single-handedly created the 'sub-4m SUV' segment craze in India. "
            "The 2022 facelift (renamed 'Brezza') added a strong-hybrid option, "
            "6 airbags and a comprehensive feature upgrade."
        ),
        "variants": ["Lxi", "Vxi", "Zxi", "Zxi+", "Zxi+ Dual Tone"],
        "engine_options": {
            "1.5L K15C DualJet": "1462 cc, 103 PS, 137 Nm",
            "1.5L Mild Hybrid": "Same engine + SHVS mild hybrid assist",
        },
        "transmission": ["5-speed MT", "6-speed AT"],
        "mileage": "19.80 km/l (AT, ARAI)",
        "safety": "4-star Global NCAP (2020)",
        "key_features": [
            "9-inch SmartPlay Pro+ infotainment",
            "HUD",
            "360 camera",
            "6 airbags",
            "Wireless charging",
            "Sunroof",
            "Connected car technology (Suzuki Connect)",
            "Ventilated front seats",
        ],
        "price_range": "₹8.34 lakh – ₹14.89 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Venue", "Tata Nexon", "Kia Sonet", "Mahindra XUV300"],
        "fun_facts": "Brezza was India's best-selling SUV for 3 consecutive years after launch.",
    },

    "maruti grand vitara": {
        "brand": "Maruti Suzuki",
        "model": "Grand Vitara",
        "years_sold": "2022–present",
        "category": "Mid-size SUV",
        "brief": (
            "Grand Vitara is Maruti's mid-size SUV, co-developed with Toyota (rebadged "
            "as Urban Cruiser Hyryder). The strong hybrid variant achieves over 27 km/l, "
            "the best mileage ever for a mid-size SUV in India."
        ),
        "variants": ["Sigma", "Delta", "Delta+", "Zeta", "Zeta+", "Alpha", "Alpha+"],
        "engine_options": {
            "1.5L K15C (Mild Hybrid)": "1462 cc, 103 PS – mild hybrid",
            "1.5L Atkinson Strong Hybrid": "1490 cc, 92 PS + 80 PS motor = 116 PS combined",
        },
        "transmission": ["5-speed MT (mild hybrid)", "6-speed AT (mild hybrid)", "e-CVT (strong hybrid)"],
        "mileage": "21.11 km/l (mild hybrid) | 27.97 km/l (strong hybrid, ARAI)",
        "safety": "3-star Global NCAP (2023)",
        "key_features": [
            "9-inch SmartPlay Pro+ with wireless Apple CarPlay/Android Auto",
            "Panoramic sunroof",
            "360 camera",
            "6 airbags",
            "Ventilated seats",
            "HUD",
            "AllGrip AWD (select variants)",
            "Connected car tech",
        ],
        "price_range": "₹10.70 lakh – ₹19.99 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Creta", "Kia Seltos", "Honda Elevate", "Skoda Kushaq"],
        "fun_facts": "The strong hybrid Grand Vitara can run on battery-only EV mode at low speeds.",
    },

    "maruti ertiga": {
        "brand": "Maruti Suzuki",
        "model": "Ertiga",
        "years_sold": "2012–present",
        "category": "MPV (7-seater)",
        "brief": (
            "Ertiga is India's most popular MPV in the value segment. "
            "Spacious 7-seat layout, car-like driving dynamics and a strong CNG option "
            "make it a family favourite."
        ),
        "variants": ["Vxi", "Vxi CNG", "Zxi", "Zxi+", "Zxi+ CNG"],
        "engine_options": {
            "1.5L K15C DualJet": "1462 cc, 103 PS, 137 Nm",
            "1.5L CNG": "77.5 PS, 98.5 Nm",
        },
        "transmission": ["5-speed MT", "6-speed AT"],
        "mileage": "20.51 km/l (MT ARAI)",
        "safety": "3-star Global NCAP",
        "key_features": [
            "Smart key",
            "7-inch infotainment",
            "Rear AC vents",
            "3-row seating",
            "Captain seats (Zxi+)",
            "ABS+EBD",
        ],
        "price_range": "₹8.69 lakh – ₹13.07 lakh (ex-showroom, 2024)",
        "rivals": ["Kia Carens", "Toyota Rumion", "Maruti XL6"],
        "fun_facts": "Ertiga was the first Maruti car with a 6-speed automatic gearbox in India.",
    },

    "maruti jimny": {
        "brand": "Maruti Suzuki",
        "model": "Jimny",
        "years_sold": "2023–present",
        "category": "Off-road SUV (4x4)",
        "brief": (
            "Jimny is a legendary off-roader now sold in India in a 5-door avatar "
            "assembled locally. With a part-time 4WD system (AllGrip Pro) and solid "
            "ladder-frame, it's the most capable off-roader under ₹15 lakh."
        ),
        "variants": ["Zeta", "Zeta+ MT/AT", "Alpha", "Alpha+ MT/AT", "Alpha+O"],
        "engine_options": {
            "1.5L K15B": "1462 cc, 105 PS, 134 Nm",
        },
        "transmission": ["5-speed MT", "4-speed AT"],
        "mileage": "16.39 km/l (MT ARAI)",
        "safety": "Not yet rated (NCAP)",
        "key_features": [
            "AllGrip Pro 4WD with low-range transfer case",
            "9-inch infotainment with wireless CarPlay",
            "Hill Hold & Hill Descent Control",
            "Terrain traction control",
            "LED headlights",
            "Spare wheel on tailgate",
        ],
        "price_range": "₹12.74 lakh – ₹15.05 lakh (ex-showroom, 2024)",
        "rivals": ["Mahindra Thar", "Force Gurkha", "Maruti Fronx (different segment)"],
        "fun_facts": "Global Jimny has been produced since 1970. India got the 5-door variant before Japan.",
    },

    "maruti fronx": {
        "brand": "Maruti Suzuki",
        "model": "Fronx",
        "years_sold": "2023–present",
        "category": "Compact SUV Coupe (Sub-4m)",
        "brief": (
            "Fronx is a coupe-styled crossover based on the Baleno platform, "
            "sold via NEXA. Unique in offering a 1.0L turbo petrol option, "
            "which is Maruti's first turbocharged engine since many years."
        ),
        "variants": ["Sigma", "Delta", "Delta+", "Zeta", "Zeta+", "Alpha", "Alpha+"],
        "engine_options": {
            "1.2L K12N DualJet (NA)": "1197 cc, 90 PS, 113 Nm",
            "1.0L K10C BoosterJet Turbo": "998 cc, 100 PS, 148 Nm",
        },
        "transmission": ["5-speed MT", "5-speed AMT", "6-speed AT (turbo)"],
        "mileage": "21.79 km/l (1.2L MT ARAI)",
        "safety": "2-star Global NCAP (2024)",
        "key_features": [
            "9-inch SmartPlay Pro+ with wireless CarPlay",
            "360 camera",
            "Sunroof",
            "Ventilated front seats",
            "HUD (alpha variants)",
            "Paddle shifters (AT)",
        ],
        "price_range": "₹7.51 lakh – ₹13.04 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Exter", "Tata Nexon", "Kia Sonet"],
        "fun_facts": "Fronx's 1.0L BoosterJet turbo is shared with several global Suzuki/Maruti models.",
    },

    # ─────────────────────────────── HYUNDAI ──────────────────────────
    "hyundai santro": {
        "brand": "Hyundai",
        "model": "Santro",
        "years_sold": "1998–2002 (Gen 1) | 2018–2022 (Gen 2)",
        "category": "Tall-boy Hatchback",
        "brief": (
            "Santro was Hyundai's first car in India and became iconic. "
            "The 2018 relaunch brought a modern Santro with an AMT option and CNG. "
            "It was discontinued in 2022 due to slow sales."
        ),
        "variants": ["D-Lite", "Era", "Magna", "Sportz", "Sportz AMT", "Asta", "Asta CNG"],
        "engine_options": {
            "1.1L Epsilon": "1086 cc, 69 PS, 99 Nm (2018 gen)",
            "CNG": "59 PS",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "20.3 km/l (petrol MT)",
        "safety": "Not rated by NCAP",
        "key_features": ["Wireless charging", "Rear camera", "AVN touchscreen", "Voice recognition"],
        "price_range": "₹4.08 – ₹6.34 lakh (at time of sale)",
        "rivals": ["Maruti WagonR", "Tata Tiago", "Maruti Celerio"],
        "fun_facts": "Original Santro's 'Sunshine' campaign with SRK is considered one of India's most iconic car ads.",
    },

    "hyundai i10": {
        "brand": "Hyundai",
        "model": "i10 / Grand i10 / Grand i10 Nios",
        "years_sold": "2007–present",
        "category": "Hatchback",
        "brief": (
            "i10 (2007) evolved into Grand i10 (2013) and then Grand i10 Nios (2019). "
            "The Nios continues to sell as a value hatchback with BSVI engines and a CNG option."
        ),
        "variants": ["Era", "Magna", "Sportz", "Sportz AMT", "Sportz Dual Tone", "Asta", "Asta CNG"],
        "engine_options": {
            "1.2L Kappa2": "1197 cc, 83 PS, 114 Nm",
            "CNG": "69 PS",
            "1.0L Kappa Turbo (i10 only)": "998 cc, 100 PS – discontinued",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "20.7 km/l (petrol)",
        "safety": "Not rated",
        "key_features": ["8-inch BlueLink infotainment", "Wireless Apple CarPlay", "Rear camera", "Dual airbags"],
        "price_range": "₹5.44 lakh – ₹7.99 lakh (Nios, ex-showroom 2024)",
        "rivals": ["Maruti WagonR", "Tata Tiago", "Maruti Celerio"],
        "fun_facts": "Grand i10 was the first Hyundai to cross 5 lakh cumulative sales in record time in India.",
    },

    "hyundai i20": {
        "brand": "Hyundai",
        "model": "i20",
        "years_sold": "2008–present",
        "category": "Premium Hatchback",
        "brief": (
            "i20 is Hyundai's flagship hatchback — premium, feature-loaded and "
            "a strong performer. The 3rd gen (2020) was a quantum leap in design "
            "and technology, offering a 1.0L turbo DCT combo in India."
        ),
        "variants": ["Magna", "Sportz", "Sportz IVT", "Asta", "Asta (O)", "Asta (O) Turbo DCT", "Asta (O) IVT"],
        "engine_options": {
            "1.2L Kappa2 (NA)": "1197 cc, 83 PS, 114 Nm",
            "1.0L T-GDi Turbo": "998 cc, 120 PS, 172 Nm",
            "1.5L U2 CRDi diesel": "1493 cc, 100 PS, 240 Nm (disc. 2023)",
        },
        "transmission": ["5-speed MT", "IVT (CVT)", "7-speed DCT (turbo)"],
        "mileage": "20.35 km/l (1.2L MT)",
        "safety": "3-star Global NCAP (2021)",
        "key_features": [
            "10.25-inch touchscreen",
            "Bose 7-speaker sound",
            "Wireless CarPlay/Android Auto",
            "Sunroof",
            "Ventilated seats",
            "BlueLink connected car (67 features)",
            "Rear wiper",
            "Air purifier",
        ],
        "price_range": "₹7.04 lakh – ₹13.10 lakh (ex-showroom, 2024)",
        "rivals": ["Maruti Baleno", "Tata Altroz", "Honda Jazz (disc.)", "VW Polo (disc.)"],
        "fun_facts": "i20 is manufactured at Hyundai's Chennai plant and exported to 65+ countries.",
    },

    "hyundai creta": {
        "brand": "Hyundai",
        "model": "Creta",
        "years_sold": "2015–present",
        "category": "Mid-size SUV",
        "brief": (
            "Creta is the car that truly defined and dominated India's mid-size SUV segment. "
            "Consistently a top-3 seller every month, the 2024 2nd generation brought "
            "panoramic display screens, ADAS suite and a hybrid option."
        ),
        "variants": ["E", "EX", "S", "S+", "SX", "SX Tech", "SX(O)", "SX(O) Turbo DCT"],
        "engine_options": {
            "1.5L MPi Petrol (NA)": "1497 cc, 115 PS, 144 Nm",
            "1.5L mHEV Petrol (Mild Hybrid)": "1497 cc, 115 PS – 2024 new",
            "1.5L U2 CRDi Diesel": "1493 cc, 116 PS, 250 Nm",
            "1.5L T-GDi Petrol Turbo": "1482 cc, 160 PS, 253 Nm",
        },
        "transmission": ["6-speed MT", "IVT", "6-speed AT", "7-speed DCT (turbo)"],
        "mileage": "17.4 km/l (1.5 petrol IVT)",
        "safety": "5-star IIHS Top Safety Pick (Korean spec); Indian spec NCAP pending 2024",
        "key_features": [
            "10.25-inch dual-panel panoramic display (2024)",
            "ADAS Level 2 (8 features)",
            "Ventilated & heated seats",
            "Bose premium audio",
            "Panoramic sunroof",
            "360 surround view",
            "BlueLink connected car",
            "Digital cluster",
        ],
        "price_range": "₹10.99 lakh – ₹20.15 lakh (ex-showroom, 2024)",
        "rivals": ["Kia Seltos", "Maruti Grand Vitara", "Honda Elevate", "Skoda Kushaq", "Volkswagen Taigun"],
        "fun_facts": "Creta sold 1 million units in India in record time — the fastest to reach that milestone in the segment.",
    },

    "hyundai venue": {
        "brand": "Hyundai",
        "model": "Venue",
        "years_sold": "2019–present",
        "category": "Sub-4m Compact SUV",
        "brief": (
            "Venue was the first connected car with eSIM (BlueLink) in India. "
            "The 2022 facelift added a digital cluster and ADAS. A strong performer "
            "against Nexon and Sonet."
        ),
        "variants": ["E", "S", "S+", "SX", "SX MT/IMT/DCT", "SX(O)"],
        "engine_options": {
            "1.2L Kappa2 NA": "1197 cc, 83 PS, 114 Nm",
            "1.0L T-GDi Turbo": "998 cc, 120 PS, 172 Nm",
            "1.5L U2 CRDi Diesel": "1493 cc, 100 PS, 240 Nm",
        },
        "transmission": ["5-speed MT", "6-speed iMT", "7-speed DCT", "6-speed MT (diesel)"],
        "mileage": "18.15 km/l (1.2L petrol)",
        "safety": "3-star Global NCAP",
        "key_features": [
            "8-inch infotainment with BlueLink",
            "Digital cluster",
            "ADAS (Level 1) – facelift",
            "Sunroof",
            "Wireless charging",
            "Air purifier",
        ],
        "price_range": "₹7.94 lakh – ₹13.47 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Nexon", "Kia Sonet", "Maruti Brezza", "Mahindra XUV300"],
        "fun_facts": "Venue was the first car in India to come factory-fitted with eSIM-based connected features.",
    },

    "hyundai verna": {
        "brand": "Hyundai",
        "model": "Verna",
        "years_sold": "2006–present",
        "category": "Sedan (C-Segment)",
        "brief": (
            "Verna has gone through 5 generations in India. The 2023 5th gen "
            "is the most dramatic yet — with a panoramic sunroof, ADAS, and "
            "a turbo-petrol only lineup (diesel dropped)."
        ),
        "variants": ["EX", "S", "S+", "SX", "SX Tech", "SX(O)", "SX(O) Turbo DCT"],
        "engine_options": {
            "1.5L MPi NA Petrol": "1497 cc, 115 PS, 144 Nm",
            "1.5L Turbo-GDi Petrol": "1482 cc, 160 PS, 253 Nm",
        },
        "transmission": ["6-speed MT", "IVT", "7-speed DCT (turbo)"],
        "mileage": "18 km/l (1.5 IVT)",
        "safety": "6-airbag standard on all variants",
        "key_features": [
            "10.25-inch panoramic display",
            "ADAS (8 features)",
            "Bose 8-speaker audio",
            "Ventilated front seats",
            "Panoramic sunroof",
            "Digital key",
            "Rear sunshade",
        ],
        "price_range": "₹10.90 lakh – ₹17.99 lakh (ex-showroom, 2024)",
        "rivals": ["Honda City", "VW Virtus", "Skoda Slavia", "Maruti Ciaz"],
        "fun_facts": "2023 Verna is India's first midsize sedan with a panoramic sunroof.",
    },

    "hyundai tucson": {
        "brand": "Hyundai",
        "model": "Tucson",
        "years_sold": "2005–2010 (Gen 1) | 2016–2021 (Gen 3) | 2022–present (Gen 4)",
        "category": "Premium Mid-size SUV",
        "brief": (
            "Tucson has had multiple innings in India. The 2022 4th gen is a full redesign "
            "with bold parametric design, ADAS, and an all-wheel drive option."
        ),
        "variants": ["Platinum", "Platinum (O)", "Signature", "Signature AWD"],
        "engine_options": {
            "2.0L MPi Petrol": "1999 cc, 156 PS, 192 Nm",
            "2.0L CRDi Diesel": "1995 cc, 186 PS, 416 Nm",
        },
        "transmission": ["6-speed AT (petrol)", "8-speed AT (diesel)"],
        "mileage": "14.08 km/l (petrol)",
        "safety": "ADAS Level 2 standard",
        "key_features": [
            "10.25-inch dual panoramic display",
            "Bose 8-speaker premium audio",
            "ADAS (8 features incl. LKA, RCTA)",
            "Ventilated & heated front seats",
            "AWD (diesel/top petrol)",
            "Panoramic sunroof",
            "Blind-view monitor",
        ],
        "price_range": "₹29.02 lakh – ₹34.99 lakh (ex-showroom, 2024)",
        "rivals": ["Jeep Compass", "Skoda Kodiaq", "Volkswagen Tiguan", "MG Hector Plus"],
        "fun_facts": "Tucson 4th gen is completely locally assembled in India, reducing costs significantly.",
    },

    "hyundai alcazar": {
        "brand": "Hyundai",
        "model": "Alcazar",
        "years_sold": "2021–present",
        "category": "6/7-seater SUV",
        "brief": (
            "Alcazar is the 3-row, long-wheelbase version of the Creta. "
            "The 2024 facelift aligns it with the new Creta's design language "
            "and adds the panoramic display and ADAS."
        ),
        "variants": ["Executive", "Prestige", "Prestige (O)", "Platinum", "Signature"],
        "engine_options": {
            "1.5L T-GDi Turbo Petrol": "1482 cc, 160 PS, 253 Nm",
            "1.5L U2 CRDi Diesel": "1493 cc, 116 PS, 250 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT", "7-speed DCT"],
        "mileage": "14.5 km/l (petrol AT)",
        "safety": "6 airbags standard",
        "key_features": ["Panoramic display (2024)", "ADAS", "Captain seats (6-seat)", "Bose audio", "Sunroof", "Wireless charging"],
        "price_range": "₹14.99 lakh – ₹21.99 lakh (ex-showroom, 2024)",
        "rivals": ["Kia Carens", "Tata Safari", "MG Hector Plus", "Mahindra XUV700 (lower trims)"],
        "fun_facts": "Alcazar is 150mm longer than Creta to accommodate the third row.",
    },

    "hyundai exter": {
        "brand": "Hyundai",
        "model": "Exter",
        "years_sold": "2023–present",
        "category": "Micro SUV (Sub-4m)",
        "brief": (
            "Exter is Hyundai's smallest SUV in India, positioned below Venue. "
            "It competes with Tata Punch in the micro-SUV space, offering an "
            "adventure-ready design and a CNG option."
        ),
        "variants": ["EX", "S", "S AMT", "S(O)", "SX", "SX(O)", "SX(O) Dual Tone"],
        "engine_options": {
            "1.2L Kappa2 Petrol": "1197 cc, 83 PS, 114 Nm",
            "1.2L CNG": "69 PS",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "19.4 km/l (MT petrol)",
        "safety": "3-star Global NCAP (2024)",
        "key_features": [
            "8-inch infotainment",
            "Dashcam (built-in)",
            "Voice-enabled electric sunroof",
            "BlueLink connected features",
            "Wireless charging",
            "Rear camera",
        ],
        "price_range": "₹6.13 lakh – ₹10.43 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Punch", "Maruti Fronx", "Nissan Magnite", "Renault Kiger"],
        "fun_facts": "Exter is India's first micro-SUV with a built-in dashcam.",
    },

    "hyundai ioniq 5": {
        "brand": "Hyundai",
        "model": "Ioniq 5",
        "years_sold": "2022–present",
        "category": "Electric SUV (Premium)",
        "brief": (
            "Ioniq 5 is Hyundai's flagship EV in India — a retro-futuristic crossover "
            "on the E-GMP platform. It features ultra-fast 800V charging and "
            "Vehicle-to-Load (V2L) technology."
        ),
        "variants": ["Standard Range AWD", "Long Range RWD", "Long Range AWD"],
        "engine_options": {
            "72.6 kWh Long Range RWD": "225 PS, 350 Nm – 631 km range (ARAI)",
            "72.6 kWh Long Range AWD": "305 PS, 605 Nm",
            "58 kWh Standard Range": "AWD only",
        },
        "transmission": ["Single-speed reduction gear (auto)"],
        "mileage": "631 km (ARAI, long range RWD)",
        "safety": "5-star Euro NCAP",
        "key_features": [
            "800V fast charging (10–80% in ~18 min with 350kW DC)",
            "V2L (Vehicle to Load) – power external devices",
            "12-inch dual screen (instrument + infotainment)",
            "Augmented Reality HUD",
            "Pixel LED headlights",
            "5-star Euro NCAP",
        ],
        "price_range": "₹44.95 lakh – ₹56.95 lakh (ex-showroom, 2024)",
        "rivals": ["Kia EV6", "Mercedes EQB", "BYD Atto 3", "MG ZS EV"],
        "fun_facts": "Ioniq 5 won World Car of the Year, World Electric Vehicle of the Year, and World Car Design of the Year in 2022.",
    },

    # ─────────────────────────────── TATA MOTORS ──────────────────────
    "tata indica": {
        "brand": "Tata Motors",
        "model": "Indica",
        "years_sold": "1998–2018",
        "category": "Hatchback",
        "brief": (
            "Indica was India's first truly indigenous passenger car, designed and "
            "engineered entirely in India. It offered diesel efficiency at a petrol price "
            "and was hugely popular in the taxi segment."
        ),
        "variants": ["DLX", "LX", "LS", "LXi", "LSi", "Xeta", "Vista (facelift from 2008)"],
        "engine_options": {
            "1.4L Diesel (Indica)": "68 PS, 135 Nm",
            "1.4L Petrol (Xeta)": "75 PS, 100 Nm",
            "1.3L Quadrajet Diesel (Vista)": "70/90 PS",
        },
        "transmission": ["5-speed MT"],
        "mileage": "20+ km/l (diesel)",
        "safety": "Not NCAP rated",
        "key_features": ["Spacious cabin (1+4 seating)","Diesel powertrain","Fleet/taxi favourite"],
        "price_range": "₹2.99 – ₹6.5 lakh (at time of sale)",
        "rivals": ["Maruti Zen", "Hyundai Santro", "Daewoo Matiz"],
        "fun_facts": "Indica's development cost was only $400 million — a fraction of what global OEMs spend.",
    },

    "tata nano": {
        "brand": "Tata Motors",
        "model": "Nano",
        "years_sold": "2009–2018",
        "category": "Microcar",
        "brief": (
            "Nano was marketed as the world's cheapest car at ₹1 lakh (base). "
            "Ratan Tata's dream of giving India a safe, affordable family car. "
            "Though commercially unsuccessful, it remains an engineering marvel."
        ),
        "variants": ["Std", "CX", "LX", "XM", "XMA", "XTA (AMT)", "Nano GenX"],
        "engine_options": {
            "0.6L 2-cyl Petrol": "624 cc, 38 PS, 51 Nm (rear engine, RWD)",
            "0.8L 3-cyl (GenX)": "793 cc, 38 PS",
        },
        "transmission": ["4-speed MT", "AMT (GenX)"],
        "mileage": "23.6 km/l",
        "safety": "Not NCAP rated",
        "key_features": ["Rear-engine layout", "Tubeless tyres", "AC (optional)", "Power steering (optional)"],
        "price_range": "₹1.0 – ₹2.5 lakh",
        "rivals": ["Maruti 800"],
        "fun_facts": "Nano's aluminium water-cooled engine is mounted in the rear — an unusual layout for India.",
    },

    "tata nexon": {
        "brand": "Tata Motors",
        "model": "Nexon",
        "years_sold": "2017–present",
        "category": "Sub-4m Compact SUV",
        "brief": (
            "Nexon is Tata's best-selling car and India's first 5-star Global NCAP SUV. "
            "Available in petrol, diesel and electric (Nexon EV), it is a comprehensive package."
        ),
        "variants": ["Smart", "Pure", "Creative", "Fearless", "Fearless+", "Accomplished", "Accomplished+"],
        "engine_options": {
            "1.2L Revotron Turbo Petrol": "1199 cc, 120 PS, 170 Nm",
            "1.5L Revotorq Diesel": "1497 cc, 115 PS, 260 Nm",
            "Nexon EV (30.2 kWh)": "129 PS, 245 Nm – ~312 km range",
            "Nexon EV Long Range (40.5 kWh)": "143 PS – ~465 km range (ARAI)",
        },
        "transmission": ["6-speed MT", "6-speed AMT", "7-speed DCA (DCT)"],
        "mileage": "17.01 km/l (petrol AMT), 24.08 km/l (diesel MT)",
        "safety": "5-star Global NCAP (2018 & 2023)",
        "key_features": [
            "10.25-inch floating touchscreen",
            "Wireless CarPlay/Android Auto",
            "Panoramic sunroof",
            "6 airbags",
            "ADAS (Level 2) – 2023 facelift",
            "JBL 9-speaker audio",
            "360 camera",
            "iRA connected car",
            "Digital cluster",
        ],
        "price_range": "₹8.10 lakh – ₹15.50 lakh (ICE) | ₹14.49 – ₹19.49 lakh (EV) (ex-showroom, 2024)",
        "rivals": ["Hyundai Venue", "Kia Sonet", "Maruti Brezza", "Mahindra XUV300"],
        "fun_facts": "Nexon EV is India's best-selling electric vehicle, a segment it pioneered in the mass market.",
    },

    "tata harrier": {
        "brand": "Tata Motors",
        "model": "Harrier",
        "years_sold": "2019–present",
        "category": "Mid-size SUV",
        "brief": (
            "Harrier is Tata's flagship mid-size SUV on the OMEGA arc platform "
            "(derived from Land Rover Discovery Sport). The 2023 facelift added "
            "ADAS, twin-screen layout and a more premium interior."
        ),
        "variants": ["Smart", "Pure", "Creative", "Fearless", "Fearless+", "Accomplished", "Accomplished+"],
        "engine_options": {
            "2.0L Kryotec Diesel": "1956 cc, 170 PS, 350 Nm",
        },
        "transmission": ["6-speed MT", "6-speed TA65 AT"],
        "mileage": "16.35 km/l (MT)",
        "safety": "5-star Global NCAP (2023)",
        "key_features": [
            "12.3-inch touchscreen + 10.25-inch digital cluster",
            "ADAS Level 2 (2023)",
            "JBL 9-speaker sound",
            "Panoramic sunroof",
            "6 airbags standard",
            "360 camera",
            "Air purifier",
            "Wireless charging",
            "Terrain response modes",
        ],
        "price_range": "₹14.99 lakh – ₹26.44 lakh (ex-showroom, 2024)",
        "rivals": ["MG Hector", "Jeep Compass", "Hyundai Tucson (lower trims)", "Mahindra XUV700 (lower trims)"],
        "fun_facts": "Harrier uses the 'OMEGA arc' platform derived from Jaguar Land Rover's D8 architecture.",
    },

    "tata safari": {
        "brand": "Tata Motors",
        "model": "Safari (New)",
        "years_sold": "2021–present (new gen) | 1998–2019 (old Safari)",
        "category": "7-seater Full-size SUV",
        "brief": (
            "The new Safari (2021) revived the legendary nameplate on a longer Harrier platform. "
            "It's a 3-row 6/7-seater SUV with identical engines to the Harrier."
        ),
        "variants": ["Smart", "Pure", "Creative", "Fearless", "Fearless+", "Accomplished", "Accomplished+"],
        "engine_options": {
            "2.0L Kryotec Diesel": "1956 cc, 170 PS, 350 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT"],
        "mileage": "14.08 km/l (AT)",
        "safety": "5-star Global NCAP (2023)",
        "key_features": [
            "12.3-inch infotainment",
            "ADAS Level 2",
            "JBL 9-speaker audio",
            "Panoramic sunroof",
            "Captain seats (6-seat option)",
            "6 airbags",
            "360 camera",
        ],
        "price_range": "₹15.49 lakh – ₹27.34 lakh (ex-showroom, 2024)",
        "rivals": ["MG Gloster", "Toyota Fortuner (different price)", "Hyundai Alcazar", "Mahindra XUV700"],
        "fun_facts": "Old Safari (1998–2019) was India's most iconic true-body-on-frame 4x4 SUV.",
    },

    "tata altroz": {
        "brand": "Tata Motors",
        "model": "Altroz",
        "years_sold": "2020–present",
        "category": "Premium Hatchback",
        "brief": (
            "Altroz is Tata's first 5-star NCAP premium hatchback. "
            "Positioned directly against Baleno and i20 with a focus on safety, "
            "it now also offers a turbo petrol and CNG option."
        ),
        "variants": ["XE", "XM", "XT", "XZ", "XZ+", "XZ+ Turbo", "XZ+ DT"],
        "engine_options": {
            "1.2L Revotron Petrol (NA)": "1199 cc, 86 PS, 113 Nm",
            "1.2L Revotron Turbo Petrol": "1199 cc, 110 PS, 140 Nm",
            "1.5L Revotorq Diesel": "1497 cc, 90 PS, 200 Nm",
            "1.2L CNG": "73.5 PS",
        },
        "transmission": ["5-speed MT", "6-speed DCT (turbo)"],
        "mileage": "19.88 km/l (NA petrol)",
        "safety": "5-star Global NCAP (2020)",
        "key_features": [
            "10.25-inch floating infotainment",
            "Arcade.ev connectivity",
            "Harman audio",
            "Digital cluster",
            "Sunroof (optional)",
            "Air purifier",
            "360 camera",
        ],
        "price_range": "₹6.60 lakh – ₹10.99 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai i20", "Maruti Baleno", "Honda Jazz (disc.)", "Toyota Glanza"],
        "fun_facts": "Altroz was the first Indian car to receive a 5-star NCAP rating in the premium hatchback category.",
    },

    "tata punch": {
        "brand": "Tata Motors",
        "model": "Punch",
        "years_sold": "2021–present",
        "category": "Micro SUV (Sub-4m)",
        "brief": (
            "Punch created the micro-SUV category in India. 5-star NCAP rated, "
            "it offers an SUV stance at hatchback pricing. Now also available "
            "in electric form (Punch EV, 2024)."
        ),
        "variants": ["Pure", "Adventure", "Accomplished", "Creative", "Creative+"],
        "engine_options": {
            "1.2L Revotron Petrol": "1199 cc, 86 PS, 113 Nm",
            "CNG": "73.5 PS",
            "Punch EV (25 kWh)": "122 PS – ~315 km range",
            "Punch EV Long Range (35 kWh)": "122 PS – ~421 km range",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "18.97 km/l (MT petrol)",
        "safety": "5-star Global NCAP (2021)",
        "key_features": [
            "7-inch/10.25-inch infotainment",
            "Digital cluster",
            "Connected car (iRA)",
            "Terrain modes (Eco, City, Sport, Traction — 2WD pseudo modes)",
            "6 airbags (top variants)",
        ],
        "price_range": "₹6.13 lakh – ₹9.49 lakh (ICE) | ₹10.99 – ₹15.49 lakh (EV) (ex-showroom, 2024)",
        "rivals": ["Hyundai Exter", "Maruti Fronx", "Renault Kiger", "Nissan Magnite"],
        "fun_facts": "Punch EV won 2024 Indian Car of the Year (ICOTY) award.",
    },

    "tata tiago": {
        "brand": "Tata Motors",
        "model": "Tiago",
        "years_sold": "2016–present",
        "category": "Hatchback",
        "brief": (
            "Tiago marked Tata's design renaissance with the IMPACT design language. "
            "It offers an impressive mix of style, features and safety for its price. "
            "A CNG and EV version are also available."
        ),
        "variants": ["XE", "XM", "XT", "XZ", "XZ+", "XZ+ Lux"],
        "engine_options": {
            "1.2L Revotron Petrol": "1199 cc, 86 PS, 113 Nm",
            "1.2L CNG": "73.5 PS",
            "Tiago EV (19.2 kWh / 24 kWh)": "75 PS – 250–315 km range",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "19.80 km/l",
        "safety": "4-star Global NCAP (2023)",
        "key_features": ["Harman audio", "Sunroof (optional)", "Digital cluster", "Wireless CarPlay"],
        "price_range": "₹5.60 lakh – ₹8.20 lakh (ICE) | ₹8.69 – ₹11.79 lakh (EV)",
        "rivals": ["Maruti WagonR", "Hyundai Grand i10 Nios", "Maruti Celerio"],
        "fun_facts": "Tiago EV, starting at ₹8.69 lakh, is the most affordable electric car in India.",
    },

    "tata tigor": {
        "brand": "Tata Motors",
        "model": "Tigor",
        "years_sold": "2017–present",
        "category": "Sub-4m Compact Sedan",
        "brief": (
            "Tigor is a notchback/sedan based on Tiago. Offers the style of a sedan "
            "in sub-4m footprint. Available in petrol, CNG and electric variants."
        ),
        "variants": ["XE", "XM", "XT", "XZ", "XZ+"],
        "engine_options": {
            "1.2L Revotron Petrol": "86 PS, 113 Nm",
            "CNG": "73.5 PS",
            "Tigor EV (26 kWh)": "75 PS – ~306 km range",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "19.70 km/l",
        "safety": "4-star Global NCAP",
        "key_features": ["Harman audio", "Automatic headlamps", "Digital cluster (top trims)"],
        "price_range": "₹6.30 lakh – ₹9.30 lakh (petrol/CNG)",
        "rivals": ["Maruti Dzire", "Honda Amaze", "Hyundai Aura"],
        "fun_facts": "Tigor EV has been widely adopted as an e-taxi / government fleet vehicle across Indian states.",
    },

    "tata curvv": {
        "brand": "Tata Motors",
        "model": "Curvv",
        "years_sold": "2024–present",
        "category": "Mid-size Coupe SUV",
        "brief": (
            "Curvv is Tata's first coupe-SUV, available in both ICE (petrol/diesel) "
            "and EV forms. It uses the Gen 2 platform, offering a 5-star safety promise, "
            "ADAS and a dramatic fastback design."
        ),
        "variants": ["Smart+", "Pure+", "Creative", "Accomplished", "Accomplished+"],
        "engine_options": {
            "1.2L Turbo Petrol (ICE)": "125 PS, 225 Nm",
            "1.5L Diesel (ICE)": "120 PS, 260 Nm",
            "Curvv EV (45 kWh)": "167 PS – ~502 km range",
            "Curvv EV (55 kWh)": "167 PS – ~585 km range",
        },
        "transmission": ["6-speed MT", "7-speed DCT (petrol)", "6-speed AT (diesel)"],
        "mileage": "~18 km/l (ICE estimate)",
        "safety": "5-star Global NCAP (2024, EV)",
        "key_features": [
            "12.3-inch infotainment + 10.25-inch cluster",
            "ADAS Level 2",
            "Panoramic sunroof",
            "JBL audio",
            "Ventilated seats",
            "360 camera",
            "V2L (EV)",
        ],
        "price_range": "₹9.99 lakh – ₹17.49 lakh (ICE) | ₹17.49 – ₹21.99 lakh (EV) (ex-showroom, 2024)",
        "rivals": ["Hyundai Creta", "Kia Seltos", "Maruti Grand Vitara", "Honda Elevate"],
        "fun_facts": "Curvv EV received 5-star NCAP before its ICE sibling — a reverse precedent in India.",
    },

    # ─────────────────────────────── MAHINDRA ─────────────────────────
    "mahindra scorpio": {
        "brand": "Mahindra",
        "model": "Scorpio / Scorpio Classic / Scorpio N",
        "years_sold": "2002–present",
        "category": "Full-size Body-on-Frame SUV",
        "brief": (
            "Scorpio is Mahindra's most iconic car — a tough, capable SUV that defined "
            "the segment in India. In 2022, the new Scorpio N launched alongside the "
            "original (renamed Scorpio Classic)."
        ),
        "variants": {
            "Scorpio Classic": ["S", "S11"],
            "Scorpio N": ["Z2", "Z4", "Z6", "Z8", "Z8 L", "Z6 4STAR", "Z8 4STAR", "Z8 L 4STAR"],
        },
        "engine_options": {
            "2.2L mHawk Diesel (Scorpio N)": "1997 cc, 175 PS, 370 Nm",
            "2.0L mStallion Turbo Petrol (Scorpio N)": "1997 cc, 203 PS, 380 Nm",
            "2.2L mHawk Diesel (Classic)": "132 PS, 300 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT"],
        "mileage": "15.2 km/l (diesel MT, Scorpio N)",
        "safety": "5-star Global NCAP (Scorpio N, 2022)",
        "key_features": [
            "4XPLOR 4WD terrain management (Scorpio N 4x4)",
            "AdrenoX connected infotainment (8-inch)",
            "Panoramic sunroof (Scorpio N)",
            "6 airbags",
            "360 camera (top trims)",
            "Wireless charging",
        ],
        "price_range": "₹13.09 lakh (Classic) | ₹13.99 – ₹24.48 lakh (Scorpio N) (ex-showroom, 2024)",
        "rivals": ["Tata Safari", "MG Gloster", "Toyota Fortuner (different price)"],
        "fun_facts": "Scorpio N received over 1 lakh bookings in just 30 minutes of opening, a record in India.",
    },

    "mahindra bolero": {
        "brand": "Mahindra",
        "model": "Bolero / Bolero Neo",
        "years_sold": "2000–present",
        "category": "Body-on-Frame SUV / Utility Vehicle",
        "brief": (
            "Bolero is India's best-selling UV (Utility Vehicle) in rural and semi-urban markets. "
            "Practical, robust, and with 7-9 seating, it's the go-to workhorse of small-town India. "
            "Bolero Neo is the rebadged TUV300 with modern styling."
        ),
        "variants": ["B2", "B4", "B6 (Opt)", "B6 (Opt) Plus", "N4", "N8", "N10", "N10 (O) — Neo"],
        "engine_options": {
            "1.5L mHawkD70 Diesel (Bolero)": "1493 cc, 75 PS, 210 Nm",
            "1.5L mHawk100 Diesel (Neo)": "1497 cc, 100 PS, 240 Nm",
        },
        "transmission": ["5-speed MT (Bolero)", "6-speed MT (Neo)"],
        "mileage": "16.04 km/l (Bolero)",
        "safety": "Not NCAP rated (Bolero)",
        "key_features": ["7/9-seater (Bolero)", "4WD option (neo top trim)", "Touchscreen (Neo)", "Rear AC"],
        "price_range": "₹9.28 – ₹10.27 lakh (Bolero) | ₹9.98 – ₹12.16 lakh (Neo) (ex-showroom, 2024)",
        "rivals": ["Mahindra Scorpio Classic", "Tata Sumo (disc.)", "Force Gurkha"],
        "fun_facts": "Bolero has been India's best-selling UV for over 15 years in semi-urban and rural markets.",
    },

    "mahindra xuv500": {
        "brand": "Mahindra",
        "model": "XUV500",
        "years_sold": "2011–2021",
        "category": "Mid-size SUV (7-seater)",
        "brief": (
            "XUV500 was Mahindra's first globally-styled, feature-rich SUV that brought "
            "7-seating, diesel power and features like GPS, BLIS to the masses. "
            "Discontinued in 2021 and replaced by XUV700."
        ),
        "variants": ["W4", "W6", "W8", "W8 (O)", "W10", "W10 AT"],
        "engine_options": {
            "2.2L mHawk Diesel": "2179 cc, 155 PS, 360 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT"],
        "mileage": "15.1 km/l",
        "safety": "Not NCAP rated formally",
        "key_features": ["7-seating", "Sunroof", "GPS", "BLIS (Blind Spot)", "Push-button start", "7-inch touchscreen"],
        "price_range": "₹13.77 – ₹19.57 lakh (at time of sale)",
        "rivals": ["Toyota Fortuner (lower spec)", "Ford Endeavour", "Tata Hexa"],
        "fun_facts": "XUV500 is India's first indigenously developed monocoque 7-seat SUV.",
    },

    "mahindra xuv700": {
        "brand": "Mahindra",
        "model": "XUV700",
        "years_sold": "2021–present",
        "category": "Full-size SUV (6/7-seater)",
        "brief": (
            "XUV700 is Mahindra's most advanced car ever. It packs segment-first ADAS, "
            "twin 10.25-inch screens, Dolby Atmos audio and diesel/petrol options. "
            "5-star NCAP rated and massively popular with long waiting periods."
        ),
        "variants": ["MX", "AX3", "AX3 L", "AX5", "AX5 L", "AX7", "AX7 L", "AX7 AWD"],
        "engine_options": {
            "2.0L mStallion Turbo Petrol": "1997 cc, 200 PS, 380 Nm",
            "2.2L mHawk Diesel": "1997 cc, 185/155 PS, 420/360 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT (petrol)", "6-speed AT (diesel)"],
        "mileage": "16.39 km/l (diesel MT)",
        "safety": "5-star Global NCAP (2022)",
        "key_features": [
            "Twin 10.25-inch screens (AdrenoX)",
            "Dolby Atmos 12-speaker sound",
            "ADAS Level 2 (7 features)",
            "AWD 4x4 option",
            "Panoramic sunroof",
            "7 airbags",
            "Driver drowsiness detection",
            "Wireless CarPlay/Android Auto",
            "Smart door handles",
        ],
        "price_range": "₹13.99 lakh – ₹26.99 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Safari", "Hyundai Alcazar", "MG Hector Plus", "Kia Carens"],
        "fun_facts": "XUV700 received 70,000 bookings in just 57 minutes of opening — setting an India record.",
    },

    "mahindra thar": {
        "brand": "Mahindra",
        "model": "Thar",
        "years_sold": "2010–present (Gen 2: 2020–)",
        "category": "Off-road 4x4 SUV",
        "brief": (
            "Thar is India's most loved off-roader. The 2020 2nd gen transformed it "
            "from a bare-bones jeep to a capable yet lifestyle vehicle with modern comforts. "
            "The 5-door Thar Roxx launched in 2024 expands the lineup."
        ),
        "variants": ["LX Hard Top", "LX Soft Top", "LX Convertible", "AX (off-road)", "Roxx MX/AX3L/AX5L/AX7L"],
        "engine_options": {
            "2.0L mStallion Turbo Petrol": "1997 cc, 150/130 PS (4x4/4x2)",
            "2.2L mHawk Diesel": "1997 cc, 130 PS, 300 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT"],
        "mileage": "15.2 km/l (diesel MT)",
        "safety": "4-star Global NCAP (2022, Thar) | 5-star (Thar Roxx 2024)",
        "key_features": [
            "4XPLOR 4WD with low-range transfer case",
            "Electronic Locking Rear Differential",
            "7-inch Adrenox infotainment",
            "Convertible/Removable roof options",
            "6-airbags (Roxx)",
            "Hill Hold & Descent Control",
            "Snorkel ready (AX)",
        ],
        "price_range": "₹11.35 lakh – ₹17.60 lakh (3-door) | ₹12.99 – ₹22.49 lakh (Roxx 5-door)",
        "rivals": ["Maruti Jimny", "Force Gurkha", "Jeep Wrangler (different price)"],
        "fun_facts": "Thar is the only car in India with a factory-equipped snorkel option available from dealership.",
    },

    "mahindra xuv300": {
        "brand": "Mahindra",
        "model": "XUV300",
        "years_sold": "2019–present",
        "category": "Sub-4m Compact SUV",
        "brief": (
            "XUV300 is Mahindra's compact SUV with class-leading safety. "
            "Built on a SsangYong T300 platform, it is the only sub-4m SUV with "
            "7 airbags as standard. Turbo diesel and petrol options available."
        ),
        "variants": ["W2", "W4", "W6", "W8", "W8 (O)", "S1", "S2", "S3", "S3+", "S4+"],
        "engine_options": {
            "1.2L mStallion Turbo Petrol": "1197 cc, 110 PS, 200 Nm",
            "1.5L mHawk Diesel": "1497 cc, 117 PS, 300 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AMT (petrol)"],
        "mileage": "17 km/l (petrol), 20 km/l (diesel)",
        "safety": "5-star Global NCAP (2019)",
        "key_features": ["7 airbags", "Sunroof", "Wireless charging", "Cruise control", "Steering-mounted controls"],
        "price_range": "₹7.99 lakh – ₹14.75 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Nexon", "Hyundai Venue", "Kia Sonet", "Maruti Brezza"],
        "fun_facts": "XUV300 is the only sub-4m SUV in India to offer 7 airbags as standard on top trims.",
    },

    "mahindra be6": {
        "brand": "Mahindra",
        "model": "BE 6",
        "years_sold": "2025–present",
        "category": "Electric Coupe SUV",
        "brief": (
            "BE 6 is Mahindra's flagship electric coupe SUV on the new INGLO platform. "
            "With a 59/79 kWh battery, 682 km claimed range, and Mahindra's most "
            "advanced tech ever, it's a game-changer for Indian EVs."
        ),
        "variants": ["Pack One", "Pack Two", "Pack Three"],
        "engine_options": {
            "59 kWh Battery": "231 PS, 380 Nm – ~535 km range",
            "79 kWh Battery": "286/350 PS, 380/380 Nm – ~682 km range",
        },
        "transmission": ["Single-speed auto (RWD)"],
        "mileage": "Up to 682 km range (MIDC)",
        "safety": "5-star Global NCAP (claimed)",
        "key_features": [
            "12.3-inch driver display + 12.3-inch co-driver display",
            "Harman audio system",
            "ADAS Level 2+",
            "175 kW fast charging (10–80% in ~20 min)",
            "V2L & V2V",
            "AI-powered infotainment (Google built-in)",
            "Augmented reality HUD",
            "OTA updates",
        ],
        "price_range": "₹18.90 lakh – ₹26.90 lakh (ex-showroom, 2025)",
        "rivals": ["Tata Curvv EV", "Hyundai Creta EV", "BYD Seal", "MG Windsor EV"],
        "fun_facts": "BE 6's INGLO platform was co-developed with Volkswagen Group and supports up to 800V charging.",
    },

    # ─────────────────────────────── HONDA ────────────────────────────
    "honda city": {
        "brand": "Honda",
        "model": "City",
        "years_sold": "1998–present",
        "category": "Mid-size Sedan (C-segment)",
        "brief": (
            "City is Honda's best-selling car in India and one of the most aspirational "
            "sedans ever. The 5th gen (2020) introduced a mild hybrid, large touchscreen "
            "and segment-best fit and finish."
        ),
        "variants": ["V", "VX", "ZX", "e:HEV (Hybrid)"],
        "engine_options": {
            "1.5L i-VTEC Petrol": "1498 cc, 121 PS, 145 Nm",
            "1.5L i-DTEC Diesel": "1498 cc, 100 PS, 200 Nm (disc. 2023)",
            "1.5L i-MMD Hybrid (e:HEV)": "1498 cc, 98 PS + 109 PS motor = 126 PS combined",
        },
        "transmission": ["6-speed MT", "CVT (petrol & hybrid)"],
        "mileage": "17.8 km/l (petrol MT) | 26.5 km/l (hybrid CVT, ARAI)",
        "safety": "4-star ASEAN NCAP (2020)",
        "key_features": [
            "8-inch infotainment with wireless CarPlay",
            "Honda Sensing ADAS (Hybrid only)",
            "Lane Watch camera",
            "Single-pane sunroof",
            "Remote engine start",
            "Ventilated seats (top trim)",
        ],
        "price_range": "₹11.65 lakh – ₹16.26 lakh (petrol) | ₹19.14 lakh (hybrid) (ex-showroom, 2024)",
        "rivals": ["Hyundai Verna", "VW Virtus", "Skoda Slavia", "Maruti Ciaz"],
        "fun_facts": "Honda City has been India's best-selling C-segment sedan for most years since its launch.",
    },

    "honda amaze": {
        "brand": "Honda",
        "model": "Amaze",
        "years_sold": "2013–present",
        "category": "Sub-4m Compact Sedan",
        "brief": (
            "Amaze is Honda's sub-4m sedan, unique for offering a CVT automatic with "
            "a diesel engine — the only such combination in its class at launch. "
            "The 3rd gen (2024) brings major design and feature upgrades."
        ),
        "variants": ["E", "S", "V", "VX"],
        "engine_options": {
            "1.2L i-VTEC Petrol": "90 PS, 110 Nm",
            "1.5L i-DTEC Diesel": "100 PS, 200 Nm",
        },
        "transmission": ["5-speed MT", "CVT (petrol & diesel)"],
        "mileage": "18.6 km/l (petrol CVT)",
        "safety": "4-star ASEAN NCAP",
        "key_features": ["8-inch touchscreen", "CarPlay/Android Auto", "Sunroof (2024)", "Digital cluster", "6 airbags (top)"],
        "price_range": "₹7.99 lakh – ₹12.99 lakh (ex-showroom, 2024)",
        "rivals": ["Maruti Dzire", "Hyundai Aura", "Tata Tigor"],
        "fun_facts": "Amaze was the first sub-4m sedan in India to offer a diesel CVT automatic.",
    },

    "honda elevate": {
        "brand": "Honda",
        "model": "Elevate",
        "years_sold": "2023–present",
        "category": "Mid-size SUV",
        "brief": (
            "Elevate is Honda's new mid-size SUV, co-developed in India for India. "
            "It slots between Venue and Creta segments but competes directly with Creta "
            "and Seltos on features and price."
        ),
        "variants": ["SV", "V", "VX", "ZX"],
        "engine_options": {
            "1.5L i-VTEC Petrol": "1498 cc, 121 PS, 145 Nm",
        },
        "transmission": ["6-speed MT", "CVT"],
        "mileage": "15.34 km/l (CVT)",
        "safety": "5-star ASEAN NCAP (2023)",
        "key_features": [
            "10.25-inch infotainment",
            "Honda Connect",
            "Lane Watch",
            "Sunroof",
            "6 airbags",
            "Wireless CarPlay/Android Auto",
            "Ventilated seats (top trim)",
        ],
        "price_range": "₹11.69 lakh – ₹16.97 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Creta", "Kia Seltos", "Maruti Grand Vitara", "Skoda Kushaq"],
        "fun_facts": "Elevate is the first Honda SUV designed and developed in India from the ground up.",
    },

    "honda jazz": {
        "brand": "Honda",
        "model": "Jazz",
        "years_sold": "2009–2014 (Gen 1) | 2015–2020 (Gen 2) | discontinued 2020",
        "category": "Premium Hatchback",
        "brief": (
            "Jazz was Honda's premium hatchback with the innovative Magic Seats "
            "that could fold in multiple configurations. Discontinued in India in 2020 "
            "due to slow sales after BS6 transition."
        ),
        "variants": ["S", "V", "VX", "ZX"],
        "engine_options": {
            "1.2L i-VTEC": "90 PS, 110 Nm",
            "1.5L i-DTEC Diesel": "100 PS (Gen 2)",
        },
        "transmission": ["5-speed MT", "CVT"],
        "mileage": "17.1 km/l",
        "safety": "Not formally rated (India)",
        "key_features": ["Magic Seat", "7-inch infotainment", "DigiPad 2.0", "Rear camera"],
        "price_range": "₹7.80 – ₹11.44 lakh (at time of sale)",
        "rivals": ["Hyundai i20", "Maruti Baleno", "VW Polo"],
        "fun_facts": "Jazz's 'Magic Seat' lets the rear floor fold up to carry tall objects like potted plants.",
    },

    # ─────────────────────────────── TOYOTA ───────────────────────────
    "toyota innova": {
        "brand": "Toyota",
        "model": "Innova / Innova Crysta / Innova HyCross",
        "years_sold": "2004–present",
        "category": "Premium MPV (7/8-seater)",
        "brief": (
            "Innova is India's most popular premium MPV and the backbone of the cab/taxi industry. "
            "The Crysta (2016) upleveled the experience significantly. "
            "InnovaHyCross (2023) introduced a strong hybrid in a new monocoque body."
        ),
        "variants": {
            "Innova Crysta (2016–)": ["GX", "VX", "ZX", "Touring Sport"],
            "Innova HyCross (2023–)": ["G", "GX", "VX", "ZX", "ZX(O)", "VX(O)"],
        },
        "engine_options": {
            "2.7L Petrol (Crysta)": "2694 cc, 166 PS, 245 Nm",
            "2.4L Diesel (Crysta)": "2393 cc, 150 PS, 360 Nm",
            "2.0L TNGA Petrol + e-motor (HyCross Hybrid)": "186 PS combined system",
        },
        "transmission": ["6-speed MT", "6-speed AT (Crysta)", "e-CVT (HyCross)"],
        "mileage": "11.99 km/l (Crysta diesel AT) | 21.1 km/l (HyCross hybrid)",
        "safety": "5-star ASEAN NCAP (Crysta, 2017)",
        "key_features": {
            "Crysta": ["8-inch infotainment", "Toyota Safety Sense (ZX)", "Captain seats", "Rear AC"],
            "HyCross": ["10.1-inch infotainment", "ADAS", "EV mode", "Panoramic sunroof", "Wireless charging", "7/8 seats"],
        },
        "price_range": "₹19.99 – ₹26.27 lakh (Crysta) | ₹19.77 – ₹31.99 lakh (HyCross) (ex-showroom, 2024)",
        "rivals": ["Kia Carnival", "Mahindra Marazzo", "Renault Triber (lower segment)"],
        "fun_facts": "Innova has been India's best-selling MPV for 20 consecutive years without interruption.",
    },

    "toyota fortuner": {
        "brand": "Toyota",
        "model": "Fortuner / Fortuner Legender / GR Sport",
        "years_sold": "2009–present",
        "category": "Body-on-Frame Full-size SUV (7-seater)",
        "brief": (
            "Fortuner is India's most aspirational mainstream SUV — a status symbol "
            "that combines on-road prestige with serious off-road ability. "
            "In production for 15 years with a loyal following."
        ),
        "variants": ["2WD MT/AT Diesel", "4WD AT Diesel", "Legender 2WD AT", "Legender 4WD AT", "GR Sport"],
        "engine_options": {
            "2.7L Petrol": "2694 cc, 166 PS, 245 Nm",
            "2.8L Diesel": "2755 cc, 204 PS, 500 Nm (AT) / 420 Nm (MT)",
        },
        "transmission": ["6-speed MT", "6-speed AT"],
        "mileage": "14.74 km/l (diesel AT)",
        "safety": "5-star ASEAN NCAP",
        "key_features": [
            "8-inch touchscreen (Legender: 9-inch)",
            "4WD with 2H/4H/4L",
            "KDSS (Kinetic Dynamic Suspension System) – 4WD top",
            "Multi-terrain select",
            "Crawl control",
            "Toyota Safety Sense (Legender)",
            "Ventilated seats",
        ],
        "price_range": "₹33.43 lakh – ₹51.53 lakh (ex-showroom, 2024)",
        "rivals": ["Ford Endeavour (disc.)", "Isuzu MU-X", "MG Gloster", "Jeep Grand Cherokee (different price)"],
        "fun_facts": "Fortuner holds ~60% market share in the premium 7-seat body-on-frame SUV segment in India.",
    },

    "toyota camry": {
        "brand": "Toyota",
        "model": "Camry Hybrid",
        "years_sold": "2002–present (current gen: 2019–)",
        "category": "Executive Sedan (D-segment)",
        "brief": (
            "Camry Hybrid is Toyota's executive sedan in India — a sophisticated "
            "combination of luxury, technology and excellent hybrid fuel economy. "
            "Sold via Toyota in India with CBU imports for some trims."
        ),
        "variants": ["Camry Hybrid (single variant)"],
        "engine_options": {
            "2.5L TNGA Petrol Hybrid": "2487 cc, 178 PS + 118 PS motor = 218 PS combined",
        },
        "transmission": ["e-CVT"],
        "mileage": "19.16 km/l (ARAI)",
        "safety": "5-star ANCAP",
        "key_features": [
            "9-inch infotainment",
            "JBL 9-speaker audio",
            "Ventilated front seats",
            "12.3-inch digital MID",
            "Head-up display",
            "Toyota Safety Sense (ADAS)",
            "Wireless charging",
        ],
        "price_range": "₹46.17 lakh – ₹48.87 lakh (ex-showroom, 2024)",
        "rivals": ["Honda Accord (disc.)", "Skoda Superb", "Volkswagen Passat (disc.)"],
        "fun_facts": "Camry Hybrid is the official car of many Indian bureaucrats and diplomats.",
    },

    "toyota glanza": {
        "brand": "Toyota",
        "model": "Glanza",
        "years_sold": "2019–present",
        "category": "Premium Hatchback",
        "brief": (
            "Glanza is a rebadged Maruti Baleno sold via Toyota's dealerships. "
            "Identical in specs but comes with Toyota's warranty and service network."
        ),
        "variants": ["E", "S", "G", "V"],
        "engine_options": {
            "1.2L DualJet K12N": "1197 cc, 90 PS, 113 Nm",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "22.35 km/l",
        "safety": "Same as Baleno",
        "key_features": ["Same as Baleno – SmartPlay Pro+", "Wireless CarPlay", "HUD", "360 camera"],
        "price_range": "₹6.73 lakh – ₹9.99 lakh (ex-showroom, 2024)",
        "rivals": ["Maruti Baleno", "Hyundai i20", "Tata Altroz"],
        "fun_facts": "Glanza was Toyota's first hatchback offering in India in over a decade.",
    },

    "toyota urban cruiser hyryder": {
        "brand": "Toyota",
        "model": "Urban Cruiser Hyryder",
        "years_sold": "2022–present",
        "category": "Mid-size SUV",
        "brief": (
            "Hyryder is Toyota's mid-size SUV, the rebadged cousin of Maruti Grand Vitara. "
            "Strong hybrid variant offers over 27 km/l, making it India's most fuel-efficient "
            "non-electric SUV. AWD available."
        ),
        "variants": ["E", "S", "G", "V", "G Hybrid", "V Hybrid"],
        "engine_options": {
            "1.5L K15C DualJet Mild Hybrid": "103 PS, 137 Nm",
            "1.5L Atkinson Strong Hybrid": "116 PS combined",
        },
        "transmission": ["5-speed MT", "6-speed AT", "e-CVT (hybrid)"],
        "mileage": "21.11 km/l (mild hybrid) | 27.97 km/l (strong hybrid)",
        "safety": "Same as Grand Vitara — 3-star NCAP",
        "key_features": ["Same as Grand Vitara", "SmartPlay Pro+", "AWD option", "Sunroof", "ADAS (top trims)"],
        "price_range": "₹11.00 lakh – ₹20.65 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Creta", "Kia Seltos", "Maruti Grand Vitara", "Honda Elevate"],
        "fun_facts": "Urban Cruiser Hyryder's strong hybrid system requires NO external charging — it self-charges.",
    },

    # ─────────────────────────────── KIA ──────────────────────────────
    "kia seltos": {
        "brand": "Kia",
        "model": "Seltos",
        "years_sold": "2019–present",
        "category": "Mid-size SUV",
        "brief": (
            "Seltos was Kia's launch product in India and immediately became a top seller. "
            "The 2023 facelift brought panoramic screens, ADAS and a DCT automatic. "
            "Kia's signature quality and feature list are its biggest selling points."
        ),
        "variants": ["EX", "HTK", "HTK+", "HTX", "HTX+", "GTX+", "X-Line"],
        "engine_options": {
            "1.5L MPi Petrol (NA)": "1497 cc, 115 PS, 144 Nm",
            "1.5L T-GDi Petrol (Turbo)": "1482 cc, 160 PS, 253 Nm",
            "1.5L CRDi Diesel": "1493 cc, 116 PS, 250 Nm",
        },
        "transmission": ["6-speed MT", "6-speed IVT (NA)", "7-speed DCT (turbo)", "6-speed AT (diesel)"],
        "mileage": "18.4 km/l (NA IVT)",
        "safety": "3-star Global NCAP",
        "key_features": [
            "10.25-inch dual panoramic display (2023)",
            "Bose 8-speaker audio",
            "ADAS Level 2",
            "Panoramic sunroof",
            "Ventilated seats",
            "360 surround view camera",
            "Kia Connect",
            "Wireless charging",
        ],
        "price_range": "₹10.89 lakh – ₹21.15 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Creta", "Maruti Grand Vitara", "Honda Elevate", "Skoda Kushaq"],
        "fun_facts": "Seltos created the 'Feature Wars' trend in Indian mid-size SUVs — each update adds more tech than rivals.",
    },

    "kia sonet": {
        "brand": "Kia",
        "model": "Sonet",
        "years_sold": "2020–present",
        "category": "Sub-4m Compact SUV",
        "brief": (
            "Sonet is Kia's compact SUV that set new benchmarks for features in the sub-4m segment. "
            "The 2024 facelift adds a dual-screen setup and updated ADAS."
        ),
        "variants": ["HTE", "HTK", "HTK+", "HTX", "HTX+", "GTX+"],
        "engine_options": {
            "1.2L Kappa Petrol": "83 PS, 115 Nm",
            "1.0L T-GDi Turbo Petrol": "120 PS, 172 Nm",
            "1.5L CRDi Diesel": "100 PS, 240 Nm",
        },
        "transmission": ["5-speed MT", "6-speed iMT", "7-speed DCT", "6-speed AT", "6-speed MT (diesel)"],
        "mileage": "18.3 km/l (1.2L MT)",
        "safety": "3-star Global NCAP",
        "key_features": [
            "10.25-inch touchscreen (2024 facelift)",
            "Bose 7-speaker audio",
            "ADAS (2024)",
            "Sunroof",
            "Wireless CarPlay",
            "Ventilated seats (top trim)",
        ],
        "price_range": "₹7.99 lakh – ₹15.99 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Venue", "Tata Nexon", "Maruti Brezza", "Mahindra XUV300"],
        "fun_facts": "Sonet was Kia's second India-specific product, developed with Indian customer data.",
    },

    "kia carens": {
        "brand": "Kia",
        "model": "Carens",
        "years_sold": "2022–present",
        "category": "MPV / 3-row SUV (6/7-seater)",
        "brief": (
            "Carens is a Kia-specific 3-row MPV that blends SUV styling with MPV practicality. "
            "Strong on features and safety, it's priced to compete with Alcazar and Safari."
        ),
        "variants": ["Premium", "Premium+", "Prestige", "Prestige+", "Luxury", "Luxury+"],
        "engine_options": {
            "1.5L MPi Petrol": "115 PS, 144 Nm",
            "1.4L T-GDi Turbo Petrol": "140 PS, 242 Nm",
            "1.5L CRDi Diesel": "116 PS, 250 Nm",
        },
        "transmission": ["6-speed MT", "6-speed IVT (NA)", "7-speed DCT (turbo)", "6-speed AT (diesel)"],
        "mileage": "17.4 km/l (petrol IVT)",
        "safety": "3-star Global NCAP",
        "key_features": [
            "10.25-inch infotainment",
            "Bose 8-speaker (top)",
            "6 airbags",
            "Sunroof",
            "Kia Connect",
            "ADAS (top variants)",
            "Captain seats (6-seater option)",
        ],
        "price_range": "₹10.52 lakh – ₹19.41 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Alcazar", "Tata Safari", "Mahindra XUV700 (lower)", "Maruti Invicto"],
        "fun_facts": "Carens received over 50,000 bookings in just 30 days of booking opening.",
    },

    "kia ev6": {
        "brand": "Kia",
        "model": "EV6",
        "years_sold": "2022–present",
        "category": "Premium Electric Crossover",
        "brief": (
            "EV6 is Kia's flagship EV in India — technologically advanced with 800V "
            "architecture, ultra-fast charging and available as GT-Line and dual-motor AWD."
        ),
        "variants": ["RWD Standard Range", "RWD Long Range", "GT-Line AWD"],
        "engine_options": {
            "58 kWh (Std Range RWD)": "226 PS",
            "77.4 kWh (Long Range RWD)": "229 PS – 708 km range",
            "77.4 kWh AWD": "325 PS",
        },
        "transmission": ["Single-speed auto"],
        "mileage": "708 km range (ARAI, LR RWD)",
        "safety": "5-star Euro NCAP",
        "key_features": [
            "800V charging (10–80% in ~18 min)",
            "V2L support",
            "12-inch curved dual display",
            "ADAS Level 2",
            "Augmented Reality HUD",
        ],
        "price_range": "₹60.97 lakh – ₹65.97 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Ioniq 5", "BMW iX1", "Volvo C40"],
        "fun_facts": "EV6 GT-Line can charge from 10–80% in just 18 minutes using a 350kW DC charger.",
    },

    # ─────────────────────────────── VOLKSWAGEN ───────────────────────
    "volkswagen polo": {
        "brand": "Volkswagen",
        "model": "Polo",
        "years_sold": "2010–2022",
        "category": "Premium Hatchback",
        "brief": (
            "Polo was VW's most popular car in India — sharp to drive, European quality "
            "and solid safety. Discontinued in 2022 after BS6 transition made it uneconomical. "
            "Fans still seek well-maintained used examples."
        ),
        "variants": ["Trendline", "Comfortline", "Highline", "GT TSI", "GT TDI"],
        "engine_options": {
            "1.0L MPI Petrol": "75 PS, 95 Nm",
            "1.2L TSI Turbo Petrol": "105 PS, 175 Nm (GT TSI)",
            "1.5L TDI Diesel": "110 PS, 250 Nm (GT TDI)",
        },
        "transmission": ["5-speed MT", "6-speed AT DSG"],
        "mileage": "17.39 km/l (TSI)",
        "safety": "4-star Euro NCAP",
        "key_features": ["Composition Media infotainment", "Electronic stability control", "DRL"],
        "price_range": "₹5.59 – ₹10.26 lakh (at time of sale)",
        "rivals": ["Hyundai i20", "Maruti Baleno", "Honda Jazz"],
        "fun_facts": "Polo GT TSI was the benchmark driver's hatchback in India — praised universally for handling.",
    },

    "volkswagen taigun": {
        "brand": "Volkswagen",
        "model": "Taigun",
        "years_sold": "2021–present",
        "category": "Mid-size SUV",
        "brief": (
            "Taigun is VW's mid-size SUV on MQB A0 IN platform (shared with Skoda Kushaq). "
            "Positioned as the premium alternative to Creta/Seltos with European dynamics."
        ),
        "variants": ["Comfortline", "Topline", "GT (TSI)", "GT Plus (TSI)"],
        "engine_options": {
            "1.0L TSI Petrol": "115 PS, 178 Nm",
            "1.5L TSI EVO Petrol": "150 PS, 250 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT", "7-speed DSG"],
        "mileage": "17.42 km/l (1.0L AT)",
        "safety": "5-star Global NCAP (2021)",
        "key_features": [
            "10-inch touchscreen (MIB3)",
            "10-inch digital cockpit (GT)",
            "Dynamic chassis control",
            "6 airbags",
            "Sunroof",
            "Wireless CarPlay",
        ],
        "price_range": "₹12.49 lakh – ₹19.59 lakh (ex-showroom, 2024)",
        "rivals": ["Hyundai Creta", "Kia Seltos", "Skoda Kushaq"],
        "fun_facts": "Taigun was specifically engineered for India — wider tracks, higher ground clearance vs global spec.",
    },

    "volkswagen virtus": {
        "brand": "Volkswagen",
        "model": "Virtus",
        "years_sold": "2022–present",
        "category": "Mid-size Sedan",
        "brief": (
            "Virtus replaced Vento as VW's India sedan on the modern MQB A0 IN platform. "
            "The GT Plus TSI variant is one of India's fastest sedans with 0-100 in 7.8 sec."
        ),
        "variants": ["Comfortline", "Topline", "GT (TSI)", "GT Plus (TSI)"],
        "engine_options": {
            "1.0L TSI Petrol": "115 PS, 178 Nm",
            "1.5L TSI EVO Petrol": "150 PS, 250 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT", "7-speed DSG"],
        "mileage": "19.89 km/l (1.0L AT)",
        "safety": "5-star Global NCAP (2022)",
        "key_features": ["10-inch MIB3 infotainment", "10-inch digital cockpit", "6 airbags", "Sunroof", "Ventilated seats (GT Plus)"],
        "price_range": "₹11.56 lakh – ₹19.10 lakh (ex-showroom, 2024)",
        "rivals": ["Skoda Slavia", "Honda City", "Hyundai Verna"],
        "fun_facts": "Virtus GT Plus with 150 PS DSG is one of very few sedans under ₹20 lakh that do 0-100 in under 8 seconds.",
    },

    # ─────────────────────────────── SKODA ────────────────────────────
    "skoda kushaq": {
        "brand": "Skoda",
        "model": "Kushaq",
        "years_sold": "2021–present",
        "category": "Mid-size SUV",
        "brief": (
            "Kushaq is Skoda's India-specific SUV — the brand's first car developed under "
            "Project India/INDIA 2.0. Premium European build quality meets Indian pricing."
        ),
        "variants": ["Active", "Ambition", "Style", "Monte Carlo"],
        "engine_options": {
            "1.0L TSI": "115 PS, 178 Nm",
            "1.5L TSI": "150 PS, 250 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT", "7-speed DSG"],
        "mileage": "18.36 km/l (1.0L AT)",
        "safety": "5-star Global NCAP (2021)",
        "key_features": [
            "10-inch Virtual Cockpit (optional)",
            "10-inch infotainment",
            "6 airbags",
            "Sunroof",
            "Wireless CarPlay",
            "KESSY keyless entry",
        ],
        "price_range": "₹11.89 lakh – ₹20.29 lakh (ex-showroom, 2024)",
        "rivals": ["VW Taigun", "Hyundai Creta", "Kia Seltos"],
        "fun_facts": "Kushaq's name means 'king' in Sanskrit — Skoda's tribute to India.",
    },

    "skoda slavia": {
        "brand": "Skoda",
        "model": "Slavia",
        "years_sold": "2022–present",
        "category": "Mid-size Sedan",
        "brief": (
            "Slavia is Skoda's MQB A0 IN-based sedan, replacing Rapid. "
            "Large boot (521L — biggest in class), premium build and refined driving dynamics."
        ),
        "variants": ["Active", "Ambition", "Style", "Monte Carlo"],
        "engine_options": {
            "1.0L TSI": "115 PS, 178 Nm",
            "1.5L TSI": "150 PS, 250 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT", "7-speed DSG"],
        "mileage": "19.45 km/l (1.0L AT)",
        "safety": "5-star Global NCAP (2022)",
        "key_features": ["10-inch infotainment", "10-inch Virtual Cockpit", "521L boot", "6 airbags", "Sunroof"],
        "price_range": "₹10.99 lakh – ₹18.79 lakh (ex-showroom, 2024)",
        "rivals": ["VW Virtus", "Honda City", "Hyundai Verna"],
        "fun_facts": "Slavia has the largest boot (521L) among all mid-size sedans in India.",
    },

    "skoda octavia": {
        "brand": "Skoda",
        "model": "Octavia",
        "years_sold": "2001–present",
        "category": "Executive Sedan (D-segment)",
        "brief": (
            "Octavia is Skoda's long-running executive sedan. The latest gen (2021) is "
            "a fully imported CBU with a 2.0L TSI engine and rich features. "
            "The RS 245 sportier variant was briefly available."
        ),
        "variants": ["Octavia (single variant)", "RS 245 (limited)"],
        "engine_options": {
            "2.0L TSI": "190 PS, 320 Nm",
        },
        "transmission": ["7-speed DSG"],
        "mileage": "15.79 km/l",
        "safety": "5-star Euro NCAP",
        "key_features": [
            "10-inch infotainment",
            "10-inch Virtual Cockpit",
            "ADAS Level 2",
            "Canton audio",
            "Wireless CarPlay",
            "Panoramic sunroof",
            "Ventilated seats",
        ],
        "price_range": "₹35.99 lakh (ex-showroom, 2024)",
        "rivals": ["Volkswagen Passat (disc.)", "Toyota Camry", "BMW 3 Series (premium)"],
        "fun_facts": "Octavia was the first truly modern European premium sedan available under ₹25 lakh in India (back in the 2000s).",
    },

    # ─────────────────────────────── MG MOTOR ─────────────────────────
    "mg hector": {
        "brand": "MG Motor",
        "model": "Hector / Hector Plus",
        "years_sold": "2019–present",
        "category": "Mid-size SUV (5/6/7-seater)",
        "brief": (
            "Hector was India's 'Internet Car' — packing the biggest screen and most connected "
            "features when launched. The 2024 Blackstorm edition gets a major design update "
            "with a large panoramic display."
        ),
        "variants": ["Style", "Super", "Smart Pro", "Sharp Pro", "Savvy Pro", "Sharp (Blackstorm)", "Savvy (Blackstorm)"],
        "engine_options": {
            "1.5L Turbo Petrol": "143 PS, 250 Nm",
            "1.5L Turbo Petrol Hybrid (MHEV)": "143 PS",
            "2.0L Diesel": "170 PS, 350 Nm (disc. 2023)",
        },
        "transmission": ["6-speed MT", "CVT"],
        "mileage": "15.81 km/l (petrol MT)",
        "safety": "Not NCAP rated",
        "key_features": [
            "14-inch (2023) / 35.56-cm panoramic (Blackstorm 2024) infotainment",
            "iSMART connected features",
            "6 airbags",
            "Panoramic sunroof",
            "Level 1 ADAS",
            "Wireless CarPlay",
        ],
        "price_range": "₹13.99 lakh – ₹21.99 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Harrier", "Jeep Compass", "Hyundai Tucson (lower)"],
        "fun_facts": "MG Hector's launch in 2019 triggered a 'feature war' in Indian SUVs with its massive 10.4-inch screen.",
    },

    "mg zs ev": {
        "brand": "MG Motor",
        "model": "ZS EV",
        "years_sold": "2020–present",
        "category": "Electric Compact SUV",
        "brief": (
            "ZS EV was India's most affordable mid-size electric SUV when launched. "
            "The 2023 facelift added a larger 50.3 kWh battery for ~461 km range."
        ),
        "variants": ["Excite Plus", "Exclusive Pro", "Essence Pro"],
        "engine_options": {
            "50.3 kWh Battery": "176 PS, 280 Nm – 461 km range (ARAI)",
        },
        "transmission": ["Single-speed auto"],
        "mileage": "461 km range (ARAI)",
        "safety": "Not NCAP rated",
        "key_features": ["10.1-inch infotainment", "ADAS", "8-year battery warranty", "50.3 kWh battery", "Wireless charging"],
        "price_range": "₹18.98 lakh – ₹25.20 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Nexon EV Long Range", "Hyundai Kona EV", "BYD Atto 3"],
        "fun_facts": "ZS EV pioneered affordable mid-size EVs in India before Nexon EV arrived.",
    },

    "mg windsor ev": {
        "brand": "MG Motor",
        "model": "Windsor EV",
        "years_sold": "2024–present",
        "category": "Electric Crossover / SUV",
        "brief": (
            "Windsor EV disrupted India's EV market with an innovative 'battery-as-a-service' "
            "(BaaS) model where you can buy the car without the battery and pay monthly subscription. "
            "Very competitive pricing."
        ),
        "variants": ["Excite", "Exclusive", "Essence"],
        "engine_options": {
            "38 kWh Battery": "136 PS, 200 Nm – 331 km range",
        },
        "transmission": ["Single-speed auto"],
        "mileage": "331 km range (ARAI)",
        "safety": "Not yet NCAP rated",
        "key_features": ["15.6-inch touchscreen", "Battery-as-a-service option", "V2L", "Reclining rear seats", "360 camera"],
        "price_range": "₹13.50 lakh (without battery) | ₹24 lakh (with battery) approx.",
        "rivals": ["Tata Curvv EV", "Mahindra BE 6", "Hyundai Creta EV"],
        "fun_facts": "Windsor EV became India's best-selling EV in its first month of sales, overtaking Nexon EV.",
    },

    "mg comet ev": {
        "brand": "MG Motor",
        "model": "Comet EV",
        "years_sold": "2023–present",
        "category": "Micro Electric Car",
        "brief": (
            "Comet EV is India's smallest and most affordable modern EV. "
            "Based on the Wuling Air EV from China, it's a 2-door city runabout "
            "ideal for urban commutes."
        ),
        "variants": ["Excite", "Exclusive"],
        "engine_options": {
            "17.3 kWh Battery": "42 PS, 110 Nm – 230 km range",
        },
        "transmission": ["Single-speed auto"],
        "mileage": "230 km range (ARAI)",
        "safety": "Not rated",
        "key_features": ["10.25-inch infotainment", "10.25-inch cluster", "4 colour customisations", "USB-C charging"],
        "price_range": "₹6.99 lakh – ₹9.99 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Tiago EV", "PMV Eas-E"],
        "fun_facts": "MG Comet EV has a 0.5m turning radius — it can literally turn within its own footprint.",
    },

    # ─────────────────────────────── RENAULT ──────────────────────────
    "renault kwid": {
        "brand": "Renault",
        "model": "Kwid",
        "years_sold": "2015–present",
        "category": "Micro Hatchback",
        "brief": (
            "Kwid disrupted the entry car market with SUV-inspired styling and a big touchscreen "
            "at a budget price point. Popular for its modern design and Renault's brand cache."
        ),
        "variants": ["Std", "RXE", "RXL", "RXT", "RXT (O)", "Climber"],
        "engine_options": {
            "0.8L SCe": "799 cc, 54 PS, 72 Nm",
            "1.0L SCe": "999 cc, 68 PS, 91 Nm",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "22.30 km/l (1.0L AMT)",
        "safety": "0-star Global NCAP (controversial; older test)",
        "key_features": ["8-inch MediaNAV touchscreen", "Digital instrument cluster", "Rear parking camera"],
        "price_range": "₹4.70 lakh – ₹6.85 lakh (ex-showroom, 2024)",
        "rivals": ["Maruti Alto K10", "Maruti S-Presso", "Tata Tiago"],
        "fun_facts": "Kwid's 0-star NCAP sparked debates about affordable car safety regulations in India.",
    },

    "renault kiger": {
        "brand": "Renault",
        "model": "Kiger",
        "years_sold": "2021–present",
        "category": "Sub-4m Compact SUV",
        "brief": (
            "Kiger is Renault's sub-4m SUV offering SUV styling and features at competitive prices. "
            "Turbo petrol option and CVT make it a complete package."
        ),
        "variants": ["RXE", "RXL", "RXT", "RXT (O)", "RXZ", "RXZ (O) Turbo CVT"],
        "engine_options": {
            "1.0L SCe NA": "72 PS, 96 Nm",
            "1.0L Tce Turbo": "100 PS, 160 Nm",
        },
        "transmission": ["5-speed MT", "5-speed AMT", "CVT (turbo)"],
        "mileage": "20.49 km/l (CVT)",
        "safety": "4-star Global NCAP (2021)",
        "key_features": ["8-inch MediaNAV", "Wireless CarPlay", "Sunroof", "360 camera (top)", "Wireless charging"],
        "price_range": "₹6.00 lakh – ₹11.05 lakh (ex-showroom, 2024)",
        "rivals": ["Nissan Magnite", "Tata Punch", "Hyundai Exter"],
        "fun_facts": "Kiger and Nissan Magnite share the same platform and engines — an alliance product.",
    },

    "renault duster": {
        "brand": "Renault",
        "model": "Duster",
        "years_sold": "2012–2022",
        "category": "Mid-size SUV",
        "brief": (
            "Duster was a cult favourite — a genuine off-road capable, value-priced SUV "
            "before the segment exploded. Discontinued in 2022 after poor sales post-BS6. "
            "A new generation is expected globally."
        ),
        "variants": ["85PS", "110PS", "130PS", "AWD"],
        "engine_options": {
            "1.5L K9K Diesel": "85/110 PS",
            "1.5L SCe Petrol": "106 PS",
            "1.3L TCe Turbo (BS6)": "156 PS (limited period)",
        },
        "transmission": ["5-speed MT", "6-speed AMT", "CVT", "6-speed AT (AWD)"],
        "mileage": "20.45 km/l (diesel)",
        "safety": "Not rated by NCAP (India spec)",
        "key_features": ["AWD option", "7-inch infotainment", "Cruise control", "Ground clearance 210mm"],
        "price_range": "₹7.99 – ₹14.83 lakh (at time of sale)",
        "rivals": ["Hyundai Creta", "Kia Seltos", "Maruti S-Cross"],
        "fun_facts": "Duster AWD was the only sub-₹15 lakh car with all-wheel drive in India for many years.",
    },

    # ─────────────────────────────── NISSAN ───────────────────────────
    "nissan magnite": {
        "brand": "Nissan",
        "model": "Magnite",
        "years_sold": "2020–present",
        "category": "Sub-4m Compact SUV",
        "brief": (
            "Magnite disrupted with aggressive pricing — a sub-₹5.5 lakh base price "
            "for an SUV with turbo petrol available. Alliance sibling of Renault Kiger."
        ),
        "variants": ["XE", "XL", "XV", "XV (O)", "XV Premium", "XV Premium (O)", "Turbo CVT variants"],
        "engine_options": {
            "1.0L NA Petrol": "72 PS, 96 Nm",
            "1.0L Turbo Petrol": "100 PS, 160 Nm",
        },
        "transmission": ["5-speed MT", "5-speed AMT", "CVT (turbo)"],
        "mileage": "20.87 km/l (CVT)",
        "safety": "4-star Global NCAP (2021)",
        "key_features": ["8-inch infotainment", "360 camera (top)", "Wireless CarPlay", "Wireless charging"],
        "price_range": "₹6.00 lakh – ₹11.55 lakh (ex-showroom, 2024)",
        "rivals": ["Renault Kiger", "Tata Punch", "Hyundai Exter"],
        "fun_facts": "Magnite was priced at ₹4.99 lakh (introductory), making it the cheapest SUV in India.",
    },

    # ─────────────────────────────── JEEP ─────────────────────────────
    "jeep compass": {
        "brand": "Jeep (Stellantis)",
        "model": "Compass",
        "years_sold": "2017–present",
        "category": "Premium Compact SUV",
        "brief": (
            "Compass is Jeep's best-selling car globally and in India. "
            "Made in Ranjangaon (Pune), it offers Jeep's trail-rated 4WD capability "
            "with modern premium features."
        ),
        "variants": ["Sport", "Sport (O)", "Longitude", "Longitude (O)", "Limited", "Limited (O)", "Model S", "Night Eagle"],
        "engine_options": {
            "1.4L MultiAir Turbo Petrol": "163 PS, 250 Nm",
            "2.0L Multijet II Diesel": "173 PS, 350 Nm",
        },
        "transmission": ["6-speed MT", "7-speed DCT (petrol)", "9-speed AT (diesel 4WD)"],
        "mileage": "16.53 km/l (diesel 4WD)",
        "safety": "5-star Euro NCAP (global model)",
        "key_features": [
            "10.1-inch Uconnect 5 infotainment",
            "Selec-Terrain 4WD (Trail Rated)",
            "Rain-sensing wipers",
            "Full LED headlamps",
            "Wireless CarPlay",
            "ADAS (Level 2) – facelift",
            "Meridian 14-speaker audio",
        ],
        "price_range": "₹19.99 lakh – ₹30.91 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Harrier", "Hyundai Tucson", "MG Hector", "Skoda Kodiaq (premium)"],
        "fun_facts": "Jeep Compass made in India is exported to 50+ countries including right-hand-drive markets.",
    },

    "jeep meridian": {
        "brand": "Jeep (Stellantis)",
        "model": "Meridian",
        "years_sold": "2022–present",
        "category": "Full-size Premium SUV (7-seater)",
        "brief": (
            "Meridian is Jeep's 7-seater SUV for India based on the Compass platform. "
            "It fills the gap for a premium 3-row Jeep in India between Compass and Wrangler."
        ),
        "variants": ["Longitude (O)", "Limited", "Limited (O)", "Overland"],
        "engine_options": {
            "2.0L Multijet II Diesel": "173 PS, 350 Nm",
        },
        "transmission": ["6-speed MT (2WD)", "9-speed AT (4WD)"],
        "mileage": "14.8 km/l",
        "safety": "6 airbags standard",
        "key_features": ["10.1-inch Uconnect 5", "Selec-Terrain 4WD", "3-row seating", "Captain seats (6-seat option)", "Meridian audio"],
        "price_range": "₹29.90 lakh – ₹36.95 lakh (ex-showroom, 2024)",
        "rivals": ["Toyota Fortuner", "MG Gloster", "Hyundai Tucson", "Skoda Kodiaq"],
        "fun_facts": "Meridian was developed specifically for emerging markets like India and South America.",
    },

    # ─────────────────────────────── FORD (discontinued) ──────────────
    "ford ecosport": {
        "brand": "Ford (exited India 2021)",
        "model": "EcoSport",
        "years_sold": "2013–2021",
        "category": "Sub-4m Compact SUV",
        "brief": (
            "EcoSport created the compact SUV craze in India before Creta and Brezza arrived. "
            "Ford exited India in September 2021, discontinuing all models."
        ),
        "variants": ["Ambiente", "Trend", "Trend+", "Titanium", "Titanium+", "S"],
        "engine_options": {
            "1.0L EcoBoost Turbo Petrol": "125 PS, 170 Nm",
            "1.5L Ti-VCT Petrol": "123 PS, 149 Nm",
            "1.5L TDCi Diesel": "100 PS, 215 Nm",
        },
        "transmission": ["5-speed MT", "6-speed AT"],
        "mileage": "17 km/l (diesel)",
        "safety": "Not rated by Global NCAP",
        "key_features": ["SYNC 3 infotainment", "Ford Pass connected features", "Tailgate-mounted spare wheel"],
        "price_range": "₹7.96 – ₹12.16 lakh (at time of sale)",
        "rivals": ["Maruti Brezza", "Hyundai Venue", "Tata Nexon"],
        "fun_facts": "EcoSport was India's first mini-SUV — it practically created the sub-4m SUV segment.",
    },

    "ford endeavour": {
        "brand": "Ford (exited India 2021)",
        "model": "Endeavour",
        "years_sold": "2003–2021",
        "category": "Body-on-Frame Full-size SUV",
        "brief": (
            "Endeavour was Ford's flagship SUV in India — a proper body-on-frame workhorse "
            "that competed with Fortuner. Loved for its powerful diesel and full-time 4WD. "
            "Discontinued when Ford exited India."
        ),
        "variants": ["Ambiente", "Trend", "Titanium", "Titanium+ 2WD/4WD"],
        "engine_options": {
            "2.0L EcoBlue Diesel (2nd gen)": "170/213 PS, 420/500 Nm",
            "3.2L TDCi Diesel (1st gen)": "200 PS, 470 Nm",
        },
        "transmission": ["10-speed AT"],
        "mileage": "14.07 km/l",
        "safety": "5-star ANCAP",
        "key_features": ["SYNC 3", "Terrain Management System (6 modes)", "Dynamic Stability Control", "Trailer Sway Control"],
        "price_range": "₹28.19 – ₹36.25 lakh (at time of sale)",
        "rivals": ["Toyota Fortuner", "Isuzu MU-X", "Mitsubishi Pajero Sport"],
        "fun_facts": "Endeavour with its 10-speed automatic was the most gear-step-rich SUV sold in India.",
    },

    # ─────────────────────────────── LUXURY SEGMENT ───────────────────
    "bmw 3 series": {
        "brand": "BMW",
        "model": "3 Series",
        "years_sold": "2005–present",
        "category": "Luxury Sports Sedan",
        "brief": (
            "3 Series is BMW's most iconic car in India — the benchmark sports sedan. "
            "Locally assembled in Chennai. Available in petrol and diesel options."
        ),
        "variants": ["320i Sport", "330i M Sport", "M340i xDrive"],
        "engine_options": {
            "2.0L TwinPower Turbo Petrol (320i)": "184 PS, 300 Nm",
            "2.0L TwinPower Turbo Petrol (330i)": "258 PS, 400 Nm",
            "3.0L TwinPower Turbo (M340i)": "374 PS, 500 Nm",
            "2.0L Diesel (320d)": "190 PS, 400 Nm",
        },
        "transmission": ["8-speed Steptronic AT"],
        "mileage": "14–16 km/l",
        "safety": "5-star Euro NCAP",
        "key_features": [
            "10.25-inch iDrive control display",
            "Wireless CarPlay",
            "Harman Kardon audio (optional)",
            "Adaptive M Suspension (M Sport)",
            "Sport+ driving mode",
            "Digital instrument cluster",
            "Gesture control",
        ],
        "price_range": "₹47.50 lakh – ₹73.90 lakh (ex-showroom, 2024)",
        "rivals": ["Mercedes-Benz C-Class", "Audi A4", "Volvo S60"],
        "fun_facts": "BMW 3 Series is locally assembled at BMW India's Chennai plant with over 50% localisation.",
    },

    "mercedes c-class": {
        "brand": "Mercedes-Benz",
        "model": "C-Class",
        "years_sold": "1995–present (current W206: 2022–)",
        "category": "Luxury Sedan",
        "brief": (
            "C-Class is Mercedes-Benz's most aspirational car in India. "
            "The current W206 generation features a revolutionary MBUX Hyperscreen "
            "option and is available as an MHEV too."
        ),
        "variants": ["C 200", "C 220d"],
        "engine_options": {
            "1.5L M254 Petrol MHEV (C200)": "204 PS, 300 Nm + EQ Boost",
            "2.0L OM654 Diesel MHEV (C220d)": "200 PS, 440 Nm",
        },
        "transmission": ["9-speed 9G-Tronic AT"],
        "mileage": "16.8 km/l",
        "safety": "5-star Euro NCAP",
        "key_features": [
            "MBUX (11.9-inch central + 12.3-inch driver display)",
            "Burmester sound system (optional)",
            "ADAS Level 2+",
            "Memory seats",
            "Ambient lighting (64 colours)",
        ],
        "price_range": "₹57.00 lakh – ₹63.50 lakh (ex-showroom, 2024)",
        "rivals": ["BMW 3 Series", "Audi A4", "Volvo S60"],
        "fun_facts": "Mercedes-Benz is the highest-selling luxury car brand in India.",
    },

    "audi q3": {
        "brand": "Audi",
        "model": "Q3",
        "years_sold": "2012–present (current: 2021–)",
        "category": "Luxury Compact SUV",
        "brief": (
            "Q3 is Audi's entry-point luxury SUV in India, locally assembled. "
            "The current gen features Audi's Virtual Cockpit and MQB platform."
        ),
        "variants": ["Premium", "Premium Plus", "Technology"],
        "engine_options": {
            "2.0L TFSI Petrol": "190 PS, 320 Nm",
        },
        "transmission": ["7-speed S Tronic DSG"],
        "mileage": "13.5 km/l",
        "safety": "5-star Euro NCAP",
        "key_features": [
            "10.1-inch MMI touchscreen",
            "Audi Virtual Cockpit (12.3-inch)",
            "Quattro AWD (optional)",
            "Bang & Olufsen audio",
            "Panoramic sunroof",
            "ADAS features",
        ],
        "price_range": "₹44.89 lakh – ₹57.89 lakh (ex-showroom, 2024)",
        "rivals": ["BMW X1", "Mercedes GLA", "Volvo XC40"],
        "fun_facts": "Q3 is Audi's most popular model in India — it introduced many buyers to the Audi brand.",
    },

    # ─────────────────────────────── BYD ──────────────────────────────
    "byd atto 3": {
        "brand": "BYD (Build Your Dreams)",
        "model": "Atto 3",
        "years_sold": "2023–present",
        "category": "Electric Mid-size SUV",
        "brief": (
            "Atto 3 is BYD's first car in India — a well-packaged electric SUV "
            "with Blade Battery tech, large range and segment-first features. "
            "Marks China's premium EV entry into India."
        ),
        "variants": ["Standard Range", "Extended Range"],
        "engine_options": {
            "49.92 kWh (Std)": "150 kW (204 PS) – 468 km range",
            "60.48 kWh (Extended)": "150 kW (204 PS) – 521 km range",
        },
        "transmission": ["Single-speed auto"],
        "mileage": "521 km range (ARAI)",
        "safety": "5-star ANCAP, Euro NCAP",
        "key_features": [
            "15.6-inch rotatable touchscreen",
            "BYD DiLink OS",
            "Blade Battery (LFP — very safe)",
            "ADAS Level 2",
            "Animated door panels",
            "Augmented reality HUD",
        ],
        "price_range": "₹24.99 lakh – ₹29.99 lakh (ex-showroom, 2024)",
        "rivals": ["MG ZS EV", "Tata Nexon EV LR", "Hyundai Ioniq 5 (premium)", "Kia EV6 (premium)"],
        "fun_facts": "BYD's Blade Battery uses lithium-iron-phosphate chemistry — it passed the 'nail penetration' test without fire.",
    },

    "byd seal": {
        "brand": "BYD",
        "model": "Seal",
        "years_sold": "2024–present",
        "category": "Electric Sports Sedan",
        "brief": (
            "Seal is BYD's flagship electric sedan in India — a sporty performance car "
            "with AWD and 523 PS in the top variant. Positions itself against Tesla Model 3."
        ),
        "variants": ["Dynamic", "Excellence", "Performance AWD"],
        "engine_options": {
            "82.56 kWh (RWD)": "313 PS – 650 km range",
            "82.56 kWh (AWD Performance)": "523 PS – 580 km range",
        },
        "transmission": ["Single-speed auto"],
        "mileage": "650 km range (CLTC, RWD)",
        "safety": "5-star Euro NCAP",
        "key_features": [
            "15.6-inch rotating touchscreen",
            "Intelligent Adaptive Suspension",
            "Vehicle-to-Load",
            "0-100 in 3.8s (AWD)",
            "Fast charging 150 kW",
        ],
        "price_range": "₹41.00 lakh – ₹53.00 lakh (ex-showroom, 2024)",
        "rivals": ["BMW i4", "Polestar 2", "Tesla Model 3"],
        "fun_facts": "BYD Seal AWD does 0-100 km/h in 3.8 seconds — faster than many sports cars at triple the price.",
    },

    # ─────────────────────────────── OTHERS ───────────────────────────
    "force gurkha": {
        "brand": "Force Motors",
        "model": "Gurkha",
        "years_sold": "2004–present (3rd gen: 2021–)",
        "category": "Off-road 4x4 SUV",
        "brief": (
            "Gurkha is India's serious off-roader — purpose-built for trails, "
            "not lifestyle. Now with BSVI compliance and 5-door option, it's more practical "
            "while retaining hardcore credentials."
        ),
        "variants": ["3-door 4x4", "5-door 4x4"],
        "engine_options": {
            "2.6L Mercedes-sourced Diesel": "2596 cc, 140 PS, 320 Nm",
        },
        "transmission": ["5-speed MT"],
        "mileage": "12 km/l",
        "safety": "Not rated",
        "key_features": [
            "Full-time 4WD with locking differentials (front + rear + centre)",
            "Solid axles (front & rear)",
            "Coil spring suspension",
            "Water wading 700mm",
            "7-inch infotainment",
        ],
        "price_range": "₹16.75 lakh – ₹17.50 lakh (ex-showroom, 2024)",
        "rivals": ["Mahindra Thar 5-door", "Maruti Jimny"],
        "fun_facts": "Gurkha's military-spec solid front axle with a locking differential is virtually unique under ₹20 lakh.",
    },

    "isuzu d-max v-cross": {
        "brand": "Isuzu",
        "model": "D-MAX V-Cross",
        "years_sold": "2016–present",
        "category": "Lifestyle Pickup Truck",
        "brief": (
            "V-Cross is India's only true lifestyle pickup truck sold by a mainstream brand. "
            "Built on Isuzu's body-on-frame platform, it offers genuine 4x4 with a practical "
            "load bay for adventure enthusiasts."
        ),
        "variants": ["Z-Prestige", "Z", "Hi-Lander"],
        "engine_options": {
            "1.9L Blue Power Diesel (3rd gen)": "163 PS, 360 Nm",
            "2.5L Blue Power Diesel (2nd gen)": "134 PS, 320 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT"],
        "mileage": "15.6 km/l",
        "safety": "5-star ASEAN NCAP (global model)",
        "key_features": ["4x4 with 2H/4H/4L", "9-inch infotainment", "360 camera (top)", "Load bed", "Tow capacity 3.5 tonnes"],
        "price_range": "₹20.25 lakh – ₹26.89 lakh (ex-showroom, 2024)",
        "rivals": ["Mahindra Scorpio N (loosely)", "Toyota Hilux"],
        "fun_facts": "V-Cross is the only pickup truck with double cab sold in India under ₹30 lakh.",
    },

    "toyota hilux": {
        "brand": "Toyota",
        "model": "Hilux",
        "years_sold": "2022–present",
        "category": "Pickup Truck",
        "brief": (
            "Hilux is Toyota's legendary pickup truck — one of the world's most capable and "
            "durable vehicles. India got it in 2022 as a premium lifestyle truck."
        ),
        "variants": ["Standard", "High"],
        "engine_options": {
            "2.8L GD-6 Diesel": "204 PS, 500 Nm",
        },
        "transmission": ["6-speed MT", "6-speed AT"],
        "mileage": "14.18 km/l",
        "safety": "5-star ANCAP",
        "key_features": [
            "4x4 with 2H/4H/4L",
            "Multi-terrain select (5 modes)",
            "Active traction control",
            "9-inch touchscreen",
            "360 camera",
            "Tow capacity 3.5 tonnes",
        ],
        "price_range": "₹30.40 lakh – ₹37.90 lakh (ex-showroom, 2024)",
        "rivals": ["Isuzu D-MAX V-Cross", "Mitsubishi Triton (not in India)"],
        "fun_facts": "Hilux has been 'killed' on Top Gear multiple times — drowned, burned, dropped from buildings — and still started.",
    },

    "volvo xc40": {
        "brand": "Volvo",
        "model": "XC40 / Recharge",
        "years_sold": "2018–present",
        "category": "Luxury Compact SUV / Electric SUV",
        "brief": (
            "XC40 is Volvo's entry luxury SUV in India — Swedish safety, minimalist design "
            "and advanced features. The fully electric Recharge version offers 418 km range."
        ),
        "variants": ["B3 Momentum", "B4 Plus", "B5 Ultimate", "Recharge Twin"],
        "engine_options": {
            "2.0L B3 Mild Hybrid Petrol": "163 PS, 265 Nm",
            "2.0L B4 Mild Hybrid Petrol": "197 PS, 300 Nm",
            "Electric Recharge (78 kWh AWD)": "408 PS, 660 Nm – 418 km range",
        },
        "transmission": ["8-speed Geartronic AT (ICE)", "Single-speed (EV)"],
        "mileage": "14.2 km/l (B4)",
        "safety": "5-star Euro NCAP",
        "key_features": [
            "9-inch Google Android Automotive OS (built-in)",
            "Harman Kardon audio",
            "Pixel LED headlights",
            "ADAS Level 2",
            "Wireless CarPlay",
        ],
        "price_range": "₹44.90 lakh – ₹75.90 lakh (ex-showroom, 2024)",
        "rivals": ["BMW X1", "Mercedes GLA", "Audi Q3", "Lexus UX"],
        "fun_facts": "XC40 was the first premium compact SUV in India to offer a fully electric powertrain.",
    },

    "maruti s-presso": {
        "brand": "Maruti Suzuki",
        "model": "S-Presso",
        "years_sold": "2019–present",
        "category": "Micro SUV-styled Hatchback",
        "brief": (
            "S-Presso is Maruti's SUV-inspired micro hatchback — a budget alternative "
            "to conventional entry hatchbacks with a tall stance and CNG option."
        ),
        "variants": ["Std", "LXi", "VXi", "VXi+", "VXi AMT", "CNG variants"],
        "engine_options": {
            "1.0L K10C DualJet": "67 PS, 89 Nm",
            "CNG": "56 PS",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "25.30 km/l (CNG: 32.73 km/kg)",
        "safety": "2-star Global NCAP",
        "key_features": ["7-inch SmartPlay Studio", "Wireless CarPlay", "Rear camera"],
        "price_range": "₹4.26 lakh – ₹6.72 lakh (ex-showroom, 2024)",
        "rivals": ["Maruti Alto K10", "Renault Kwid", "Datsun Redi-GO (disc.)"],
        "fun_facts": "S-Presso's high roof and SUV-inspired design made it one of Maruti's fastest-launched new models.",
    },

    "hyundai aura": {
        "brand": "Hyundai",
        "model": "Aura",
        "years_sold": "2020–present",
        "category": "Sub-4m Compact Sedan",
        "brief": (
            "Aura replaced the Xcent as Hyundai's sub-4m sedan. "
            "With a CNG option and a turbocharged engine on top trims, "
            "it is one of the most feature-loaded compact sedans."
        ),
        "variants": ["E", "S", "S AMT", "SX", "SX MT/AMT", "SX+", "SX+ Turbo DCT"],
        "engine_options": {
            "1.2L Kappa2": "83 PS, 114 Nm",
            "1.0L T-GDi Turbo": "100 PS, 172 Nm",
            "1.2L CNG": "69 PS",
        },
        "transmission": ["5-speed MT", "5-speed AMT", "7-speed DCT (turbo)"],
        "mileage": "20.5 km/l (petrol MT)",
        "safety": "3-star Global NCAP",
        "key_features": ["8-inch infotainment", "BlueLink", "Wireless CarPlay", "Rear camera"],
        "price_range": "₹6.49 lakh – ₹8.74 lakh (ex-showroom, 2024)",
        "rivals": ["Maruti Dzire", "Tata Tigor", "Honda Amaze"],
        "fun_facts": "Aura is the only sub-4m sedan with a turbo-petrol + DCT combination in India.",
    },

    "mahindra marazzo": {
        "brand": "Mahindra",
        "model": "Marazzo",
        "years_sold": "2018–present",
        "category": "Premium MPV (8-seater)",
        "brief": (
            "Marazzo was designed as a shark-inspired MPV with a focus on ride comfort "
            "and space. It offers the best ride quality in its class with a shark-like "
            "front design."
        ),
        "variants": ["M2", "M4", "M6", "M8"],
        "engine_options": {
            "1.5L mHawk100 Diesel": "123 PS, 300 Nm",
        },
        "transmission": ["6-speed MT"],
        "mileage": "17.99 km/l",
        "safety": "Not rated",
        "key_features": ["Shark-inspired design", "8-seater", "Sunroof", "7-inch infotainment", "Rear AC"],
        "price_range": "₹13.20 lakh – ₹16.58 lakh (ex-showroom, 2024)",
        "rivals": ["Kia Carens", "Toyota Innova Crysta (lower)", "Hyundai Alcazar"],
        "fun_facts": "Marazzo was co-designed with Pininfarina (Ferrari's design house) — a first for Mahindra.",
    },

    "citroen c3": {
        "brand": "Citroën",
        "model": "C3 / C3 Aircross",
        "years_sold": "2022–present",
        "category": "Compact Hatchback / Compact SUV",
        "brief": (
            "Citroën re-entered India in 2022 with the C3 hatchback, followed by the "
            "C3 Aircross 7-seater SUV. Known for comfortable ride quality and French flair."
        ),
        "variants": ["You", "Shine", "Feel", "C3 Aircross – You/Feel/Max"],
        "engine_options": {
            "1.2L PureTech Petrol (C3)": "82 PS, 115 Nm",
            "1.2L Turbo PureTech (C3)": "110 PS, 190 Nm",
            "1.5L Diesel (Aircross)": "110 PS, 250 Nm",
        },
        "transmission": ["5-speed MT", "6-speed AT (turbo)", "6-speed MT (diesel)"],
        "mileage": "19.80 km/l (petrol)",
        "safety": "Not rated",
        "key_features": ["10-inch infotainment", "Wireless CarPlay", "Comfort suspension", "Tri-colour exterior"],
        "price_range": "₹6.16 lakh – ₹10.49 lakh (C3) | ₹12.63 – ₹17.60 lakh (Aircross)",
        "rivals": ["Tata Punch", "Maruti Swift", "Nissan Magnite"],
        "fun_facts": "C3 offers 36 exterior personalisation combinations — the most customisable car in its class in India.",
    },

    "tata nexon ev": {
        "brand": "Tata Motors",
        "model": "Nexon EV",
        "years_sold": "2020–present",
        "category": "Electric Compact SUV",
        "brief": (
            "Nexon EV is India's best-selling electric car. The 2023 facelift (Gen 2) "
            "brought longer range, updated features and ADAS — setting a high bar "
            "for affordable EVs."
        ),
        "variants": ["Creative", "Fearless", "Fearless+", "Accomplished", "Accomplished+ LR", "Fearless+ LR"],
        "engine_options": {
            "30.2 kWh": "129 PS, 245 Nm – 312 km ARAI",
            "40.5 kWh LR": "143 PS, 215 Nm – 465 km ARAI",
        },
        "transmission": ["Single-speed auto"],
        "mileage": "465 km (LR ARAI)",
        "safety": "5-star Global NCAP",
        "key_features": [
            "10.25-inch infotainment",
            "ADAS Level 2",
            "JBL 9-speaker audio",
            "Wireless CarPlay",
            "V2L",
            "Panoramic sunroof",
            "OTA updates",
        ],
        "price_range": "₹14.49 lakh – ₹19.49 lakh (ex-showroom, 2024)",
        "rivals": ["MG ZS EV", "Hyundai Kona EV", "Mahindra XEV 9e (premium)"],
        "fun_facts": "Nexon EV holds the record for the highest EV sales in Indian automotive history.",
    },

    "maruti celerio": {
        "brand": "Maruti Suzuki",
        "model": "Celerio",
        "years_sold": "2014–present",
        "category": "Hatchback",
        "brief": (
            "Celerio was the first mass-market car in India with an AMT (Auto Gear Shift) "
            "automatic gearbox. The 2021 2nd gen brought a new platform and fuel-efficient engine."
        ),
        "variants": ["Lxi", "VXi", "ZXi", "ZXi+", "CNG variants"],
        "engine_options": {
            "1.0L K10C DualJet": "67 PS, 89 Nm",
            "CNG": "56 PS",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "26.68 km/l (MT ARAI) — India's most fuel-efficient petrol car",
        "safety": "1-star Global NCAP (2022)",
        "key_features": ["7-inch SmartPlay infotainment", "Wireless CarPlay", "ABS", "Dual airbags", "Rear camera"],
        "price_range": "₹5.37 lakh – ₹7.27 lakh (ex-showroom, 2024)",
        "rivals": ["Maruti WagonR", "Hyundai Grand i10 Nios", "Tata Tiago"],
        "fun_facts": "Celerio's 2021 engine is the most fuel-efficient petrol engine produced in India — 26.68 km/l.",
    },

    "maruti ignis": {
        "brand": "Maruti Suzuki",
        "model": "Ignis",
        "years_sold": "2017–present",
        "category": "Urban Micro SUV Hatchback",
        "brief": (
            "Ignis is Maruti's quirky urban crossover sold via NEXA. "
            "Targeted at young buyers with funky design, body-coloured bumpers "
            "and easy city maneuverability."
        ),
        "variants": ["Sigma", "Delta", "Zeta", "Alpha"],
        "engine_options": {
            "1.2L K12M": "83 PS, 113 Nm",
        },
        "transmission": ["5-speed MT", "5-speed AMT"],
        "mileage": "20.89 km/l",
        "safety": "Not rated",
        "key_features": ["7-inch SmartPlay infotainment", "Wireless CarPlay", "LED projector headlamps"],
        "price_range": "₹5.84 lakh – ₹8.29 lakh (ex-showroom, 2024)",
        "rivals": ["Tata Tiago", "Ford Figo (disc.)", "Maruti Swift"],
        "fun_facts": "Ignis is one of India's smallest SUV-inspired hatchbacks with the biggest cult following online.",
    },
}

# ══════════════════════════════════════════════════════════════════════
#  ALIASES  –  maps common names / spellings to canonical keys
# ══════════════════════════════════════════════════════════════════════

ALIASES = {
    "alto": "maruti alto",
    "alto k10": "maruti alto",
    "k10": "maruti alto",
    "wagon r": "maruti wagon r",
    "wagonr": "maruti wagon r",
    "swift": "maruti swift",
    "baleno": "maruti baleno",
    "dzire": "maruti dzire",
    "swift dzire": "maruti dzire",
    "brezza": "maruti vitara brezza",
    "vitara brezza": "maruti vitara brezza",
    "grand vitara": "maruti grand vitara",
    "ertiga": "maruti ertiga",
    "jimny": "maruti jimny",
    "fronx": "maruti fronx",
    "s-presso": "maruti s-presso",
    "spresso": "maruti s-presso",
    "celerio": "maruti celerio",
    "ignis": "maruti ignis",
    "santro": "hyundai santro",
    "i10": "hyundai i10",
    "grand i10": "hyundai i10",
    "grand i10 nios": "hyundai i10",
    "nios": "hyundai i10",
    "i20": "hyundai i20",
    "creta": "hyundai creta",
    "venue": "hyundai venue",
    "verna": "hyundai verna",
    "tucson": "hyundai tucson",
    "alcazar": "hyundai alcazar",
    "exter": "hyundai exter",
    "ioniq5": "hyundai ioniq 5",
    "ioniq 5": "hyundai ioniq 5",
    "aura": "hyundai aura",
    "indica": "tata indica",
    "vista": "tata indica",
    "nano": "tata nano",
    "nexon": "tata nexon",
    "nexon ev": "tata nexon ev",
    "harrier": "tata harrier",
    "safari": "tata safari",
    "altroz": "tata altroz",
    "punch": "tata punch",
    "punch ev": "tata punch",
    "tiago": "tata tiago",
    "tiago ev": "tata tiago",
    "tigor": "tata tigor",
    "curvv": "tata curvv",
    "curvv ev": "tata curvv",
    "scorpio": "mahindra scorpio",
    "scorpio n": "mahindra scorpio",
    "scorpio classic": "mahindra scorpio",
    "bolero": "mahindra bolero",
    "bolero neo": "mahindra bolero",
    "xuv500": "mahindra xuv500",
    "xuv 500": "mahindra xuv500",
    "xuv700": "mahindra xuv700",
    "xuv 700": "mahindra xuv700",
    "thar": "mahindra thar",
    "thar roxx": "mahindra thar",
    "xuv300": "mahindra xuv300",
    "xuv 300": "mahindra xuv300",
    "be6": "mahindra be6",
    "be 6": "mahindra be6",
    "marazzo": "mahindra marazzo",
    "city": "honda city",
    "amaze": "honda amaze",
    "elevate": "honda elevate",
    "jazz": "honda jazz",
    "innova": "toyota innova",
    "crysta": "toyota innova",
    "hycross": "toyota innova",
    "innova hycross": "toyota innova",
    "innova crysta": "toyota innova",
    "fortuner": "toyota fortuner",
    "camry": "toyota camry",
    "glanza": "toyota glanza",
    "hyryder": "toyota urban cruiser hyryder",
    "urban cruiser hyryder": "toyota urban cruiser hyryder",
    "seltos": "kia seltos",
    "sonet": "kia sonet",
    "carens": "kia carens",
    "ev6": "kia ev6",
    "polo": "volkswagen polo",
    "taigun": "volkswagen taigun",
    "virtus": "volkswagen virtus",
    "kushaq": "skoda kushaq",
    "slavia": "skoda slavia",
    "octavia": "skoda octavia",
    "hector": "mg hector",
    "hector plus": "mg hector",
    "zs ev": "mg zs ev",
    "windsor": "mg windsor ev",
    "windsor ev": "mg windsor ev",
    "comet ev": "mg comet ev",
    "comet": "mg comet ev",
    "kwid": "renault kwid",
    "kiger": "renault kiger",
    "duster": "renault duster",
    "magnite": "nissan magnite",
    "compass": "jeep compass",
    "meridian": "jeep meridian",
    "ecosport": "ford ecosport",
    "eco sport": "ford ecosport",
    "endeavour": "ford endeavour",
    "3 series": "bmw 3 series",
    "bmw3": "bmw 3 series",
    "c-class": "mercedes c-class",
    "c class": "mercedes c-class",
    "q3": "audi q3",
    "atto 3": "byd atto 3",
    "atto3": "byd atto 3",
    "seal": "byd seal",
    "gurkha": "force gurkha",
    "v-cross": "isuzu d-max v-cross",
    "vcross": "isuzu d-max v-cross",
    "d-max": "isuzu d-max v-cross",
    "hilux": "toyota hilux",
    "xc40": "volvo xc40",
    "c3": "citroen c3",
    "aircross": "citroen c3",
    "c3 aircross": "citroen c3",
}

# ══════════════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════

WRAP_WIDTH = 80


def wrap(text, indent=0):
    prefix = " " * indent
    return textwrap.fill(text, width=WRAP_WIDTH, subsequent_indent=prefix)


def banner():
    print("\n" + "═" * WRAP_WIDTH)
    print("  🚗  INDIA CARS LLM  — Your Expert on Indian Automobiles (2000–2026)")
    print("  Pre-trained | No API | Knowledge embedded in code")
    print("═" * WRAP_WIDTH)
    print(wrap(
        "Ask me anything about cars sold in India — variants, specs, engine options, "
        "features, prices, rivals. Type 'list' to see all cars, 'exit' to quit."
    ))
    print("═" * WRAP_WIDTH + "\n")


def fuzzy_find_car(query: str):
    """Try to find a car from the DB using aliases then fuzzy matching."""
    query_lower = query.lower().strip()

    # Direct alias check
    if query_lower in ALIASES:
        return ALIASES[query_lower], CAR_DB[ALIASES[query_lower]]

    # Direct key check
    if query_lower in CAR_DB:
        return query_lower, CAR_DB[query_lower]

    # Check if alias value matches
    for alias, key in ALIASES.items():
        if alias in query_lower or query_lower in alias:
            return key, CAR_DB[key]

    # Check if a DB key is a substring of query
    for key in CAR_DB:
        # e.g. "maruti swift" in "tell me about maruti swift"
        parts = key.split()
        if all(p in query_lower for p in parts):
            return key, CAR_DB[key]

    # Fuzzy match on aliases + db keys combined
    all_keys = list(ALIASES.keys()) + list(CAR_DB.keys())
    matches = difflib.get_close_matches(query_lower, all_keys, n=1, cutoff=0.55)
    if matches:
        hit = matches[0]
        canonical = ALIASES.get(hit, hit)
        if canonical in CAR_DB:
            return canonical, CAR_DB[canonical]

    return None, None


def detect_intent(query: str):
    """Detect what the user is asking about."""
    q = query.lower()
    if any(w in q for w in ["variant", "version", "trim", "grade"]):
        return "variants"
    if any(w in q for w in ["engine", "motor", "cc", "displacement", "cylinder", "torque", "power", "ps", "hp", "nm"]):
        return "engine"
    if any(w in q for w in ["feature", "technology", "tech", "infotainment", "screen", "airbag", "safety", "adas", "sunroof"]):
        return "features"
    if any(w in q for w in ["price", "cost", "lakh", "rupee", "expensive", "cheap", "affordable"]):
        return "price"
    if any(w in q for w in ["mileage", "fuel", "efficiency", "km/l", "kmpl", "economy", "range"]):
        return "mileage"
    if any(w in q for w in ["vs", "compare", "better", "difference between", "versus"]):
        return "compare"
    if any(w in q for w in ["transmission", "gear", "automatic", "manual", "amt", "dct", "cvt", "at"]):
        return "transmission"
    if any(w in q for w in ["competitor", "rival", "alternative", "against"]):
        return "rivals"
    if any(w in q for w in ["fact", "fun fact", "know", "interesting"]):
        return "funfact"
    return "full"


def format_car_full(key, car):
    """Format complete car info."""
    lines = []
    sep = "─" * WRAP_WIDTH
    lines.append(sep)
    lines.append(f"  🚘  {car['brand']}  {car['model']}  |  {car.get('category','')}")
    lines.append(f"  📅  On Sale: {car.get('years_sold','N/A')}")
    lines.append(sep)

    lines.append("\n📝  OVERVIEW")
    lines.append(wrap(car.get("brief", "No info available."), 4))

    lines.append("\n🔧  ENGINE OPTIONS")
    eng = car.get("engine_options", {})
    if isinstance(eng, dict):
        for name, spec in eng.items():
            lines.append(f"    • {name}: {spec}")
    else:
        lines.append(f"    {eng}")

    lines.append("\n⚙️  TRANSMISSION")
    trans = car.get("transmission", [])
    lines.append("    " + " | ".join(trans) if trans else "    N/A")

    lines.append("\n🏎️  VARIANTS")
    variants = car.get("variants", [])
    if isinstance(variants, list):
        lines.append("    " + " | ".join(variants))
    elif isinstance(variants, dict):
        for grp, v_list in variants.items():
            lines.append(f"    [{grp}]  " + " | ".join(v_list))

    lines.append("\n⛽  FUEL EFFICIENCY")
    lines.append(f"    {car.get('mileage', 'N/A')}")

    lines.append("\n🌟  KEY FEATURES")
    feats = car.get("key_features", [])
    if isinstance(feats, list):
        for f in feats:
            lines.append(f"    ✔ {f}")
    elif isinstance(feats, dict):
        for grp, flist in feats.items():
            lines.append(f"    [{grp}]")
            for f in flist:
                lines.append(f"      ✔ {f}")

    lines.append("\n🛡️  SAFETY")
    lines.append(f"    {car.get('safety', 'N/A')}")

    lines.append("\n💰  PRICE RANGE")
    lines.append(f"    {car.get('price_range', 'N/A')}")

    lines.append("\n🥊  RIVALS")
    rivals = car.get("rivals", [])
    lines.append("    " + " | ".join(rivals) if rivals else "    N/A")

    lines.append("\n💡  DID YOU KNOW?")
    lines.append(wrap(car.get("fun_facts", "N/A"), 4))

    lines.append("\n" + sep)
    return "\n".join(lines)


def format_car_section(key, car, section):
    """Format a specific section of car info."""
    sep = "─" * WRAP_WIDTH
    header = f"\n  🚘  {car['brand']} {car['model']}  —  "
    lines = [sep]

    if section == "variants":
        lines.append(header + "VARIANTS")
        lines.append(sep)
        variants = car.get("variants", [])
        if isinstance(variants, list):
            for i, v in enumerate(variants, 1):
                lines.append(f"  {i}. {v}")
        elif isinstance(variants, dict):
            for grp, vlist in variants.items():
                lines.append(f"\n  [{grp}]")
                for i, v in enumerate(vlist, 1):
                    lines.append(f"    {i}. {v}")

    elif section == "engine":
        lines.append(header + "ENGINE OPTIONS")
        lines.append(sep)
        eng = car.get("engine_options", {})
        if isinstance(eng, dict):
            for name, spec in eng.items():
                lines.append(f"  🔩 {name}")
                lines.append(f"       └─ {spec}")
        lines.append(f"\n  Transmission: {' | '.join(car.get('transmission', ['N/A']))}")

    elif section == "features":
        lines.append(header + "KEY FEATURES & SAFETY")
        lines.append(sep)
        feats = car.get("key_features", [])
        if isinstance(feats, list):
            for f in feats:
                lines.append(f"  ✔ {f}")
        elif isinstance(feats, dict):
            for grp, flist in feats.items():
                lines.append(f"\n  [{grp}]")
                for f in flist:
                    lines.append(f"    ✔ {f}")
        lines.append(f"\n  Safety Rating: {car.get('safety', 'N/A')}")

    elif section == "price":
        lines.append(header + "PRICING")
        lines.append(sep)
        lines.append(f"  💰 Price Range: {car.get('price_range', 'N/A')}")
        lines.append(f"  🥊 Rivals: {', '.join(car.get('rivals', []))}")

    elif section == "mileage":
        lines.append(header + "FUEL EFFICIENCY")
        lines.append(sep)
        lines.append(f"  ⛽ Mileage: {car.get('mileage', 'N/A')}")
        lines.append(f"  Engines:  {', '.join(car.get('engine_options', {}).keys())}")

    elif section == "transmission":
        lines.append(header + "TRANSMISSION")
        lines.append(sep)
        for t in car.get("transmission", ["N/A"]):
            lines.append(f"  ⚙️  {t}")

    elif section == "rivals":
        lines.append(header + "RIVALS / COMPETITORS")
        lines.append(sep)
        for r in car.get("rivals", ["N/A"]):
            lines.append(f"  🥊 {r}")

    elif section == "funfact":
        lines.append(header + "FUN FACT")
        lines.append(sep)
        lines.append(wrap("  💡 " + car.get("fun_facts", "N/A"), 5))

    else:
        return format_car_full(key, car)

    lines.append(sep)
    return "\n".join(lines)


def list_all_cars():
    """List all cars in DB."""
    brands = {}
    for key, car in CAR_DB.items():
        brand = car["brand"].split()[0]  # first word
        brands.setdefault(brand, []).append(f"{car['brand']} {car['model']}")

    lines = ["", "═" * WRAP_WIDTH, "  📋  COMPLETE INDIA CAR DATABASE (2000–2026)", "═" * WRAP_WIDTH]
    for brand in sorted(brands):
        lines.append(f"\n  🏷  {brand.upper()}")
        for car_name in brands[brand]:
            lines.append(f"       • {car_name}")
    lines.append("\n" + "═" * WRAP_WIDTH)
    lines.append(f"  Total: {len(CAR_DB)} models in knowledge base")
    lines.append("═" * WRAP_WIDTH)
    return "\n".join(lines)


def handle_compare(query: str):
    """Handle comparison queries."""
    # Try to find two cars in the query
    found_cars = []
    for alias, key in ALIASES.items():
        if alias in query.lower():
            if key not in [c[0] for c in found_cars]:
                found_cars.append((key, CAR_DB[key]))
        if len(found_cars) == 2:
            break
    if len(found_cars) < 2:
        for key, car in CAR_DB.items():
            if key in query.lower():
                if key not in [c[0] for c in found_cars]:
                    found_cars.append((key, car))
            if len(found_cars) == 2:
                break

    if len(found_cars) < 2:
        return ("  I could identify only one or no car in your comparison query. "
                "Please name both cars clearly, e.g. 'Compare Creta vs Seltos'")

    k1, c1 = found_cars[0]
    k2, c2 = found_cars[1]
    sep = "─" * WRAP_WIDTH

    lines = [
        "", sep,
        f"  ⚔️   {c1['brand']} {c1['model']}   VS   {c2['brand']} {c2['model']}",
        sep,
        f"{'Feature':<28} {'  ' + c1['model']:<25} {'  ' + c2['model']:<25}",
        "─" * WRAP_WIDTH,
        f"{'Category':<28} {c1.get('category','—')[:24]:<25} {c2.get('category','—')[:24]:<25}",
        f"{'Mileage':<28} {c1.get('mileage','—')[:24]:<25} {c2.get('mileage','—')[:24]:<25}",
        f"{'Price Range':<28} {c1.get('price_range','—')[:24]:<25} {c2.get('price_range','—')[:24]:<25}",
        f"{'Safety':<28} {c1.get('safety','—')[:24]:<25} {c2.get('safety','—')[:24]:<25}",
        "",
    ]

    lines.append("  ENGINES:")
    e1 = list(c1.get("engine_options", {}).keys())
    e2 = list(c2.get("engine_options", {}).keys())
    max_len = max(len(e1), len(e2))
    for i in range(max_len):
        a = e1[i] if i < len(e1) else "—"
        b = e2[i] if i < len(e2) else "—"
        lines.append(f"  {a[:38]:<40} {b[:38]:<38}")

    lines.append("")
    lines.append("  TRANSMISSION:")
    lines.append(f"  {', '.join(c1.get('transmission',[])):<40} {', '.join(c2.get('transmission',[]))}")

    lines.append(sep)
    return "\n".join(lines)


def respond(query: str) -> str:
    """Core response function — the 'LLM'."""
    query = query.strip()
    if not query:
        return "  Please ask me something about Indian cars! 🚗"

    ql = query.lower()

    # ── SPECIAL COMMANDS ──────────────────────────────────────────────
    if ql in ("list", "list all", "show all", "all cars", "car list"):
        return list_all_cars()

    if ql in ("help", "?", "commands"):
        return (
            "\n  💬  HOW TO USE\n"
            "  ─────────────────────────────────────────────────────\n"
            "  • Ask about any car:      'Tell me about Tata Nexon'\n"
            "  • Specific detail:        'Nexon variants' / 'Creta engine'\n"
            "  • Features:               'What features does i20 have?'\n"
            "  • Price:                  'How much is the Fortuner?'\n"
            "  • Mileage:                'Baleno mileage'\n"
            "  • Comparisons:            'Compare Creta vs Seltos'\n"
            "  • Fun facts:              'Fun fact about Scorpio'\n"
            "  • List all cars:          'list'\n"
            "  • Exit:                   'exit'\n"
            "  ─────────────────────────────────────────────────────\n"
        )

    # ── GREETING ──────────────────────────────────────────────────────
    if any(w in ql for w in ["hello", "hi", "hey", "namaste", "good morning", "good evening"]):
        return (
            "\n  🙏 Namaste! I'm your India Cars Expert — "
            "pre-trained on every major car sold in India from 2000 to 2026.\n"
            "  Ask me about any car's variants, specs, engines, features or price!\n"
        )

    # ── COMPARE ───────────────────────────────────────────────────────
    if "vs" in ql or "versus" in ql or "compare" in ql or "difference between" in ql:
        return handle_compare(query)

    # ── FIND CAR + INTENT ─────────────────────────────────────────────
    key, car = fuzzy_find_car(query)
    if car:
        intent = detect_intent(query)
        if intent == "full":
            return format_car_full(key, car)
        else:
            return format_car_section(key, car, intent)

    # ── BRAND-LEVEL QUERIES ───────────────────────────────────────────
    brand_map = {
        "maruti": "Maruti Suzuki", "suzuki": "Maruti Suzuki",
        "hyundai": "Hyundai", "tata": "Tata Motors",
        "mahindra": "Mahindra", "honda": "Honda",
        "toyota": "Toyota", "kia": "Kia",
        "volkswagen": "Volkswagen", "vw": "Volkswagen",
        "skoda": "Skoda", "mg": "MG Motor",
        "renault": "Renault", "nissan": "Nissan",
        "jeep": "Jeep", "ford": "Ford",
        "bmw": "BMW", "mercedes": "Mercedes-Benz",
        "audi": "Audi", "byd": "BYD",
        "volvo": "Volvo", "force": "Force Motors",
        "isuzu": "Isuzu", "citroen": "Citroën",
    }
    for b_key, b_name in brand_map.items():
        if b_key in ql:
            brand_cars = [(k, v) for k, v in CAR_DB.items() if b_name in v["brand"]]
            if brand_cars:
                lines = [f"\n  🏷  All {b_name} cars in my knowledge base:\n"]
                for k, v in brand_cars:
                    lines.append(f"   • {v['model']}  ({v.get('category','')})")
                lines.append(f"\n  💬 Ask me about any specific model for full details!\n")
                return "\n".join(lines)

    # ── GENERAL KNOWLEDGE QUERIES (non-car-specific) ──────────────────
    general = {
        "best selling": "India's top-selling cars include Maruti Suzuki Alto, WagonR, Baleno, Swift, Dzire and Tata Nexon — consistently in the monthly top-10.",
        "ev": "India's top EVs (2024): Tata Nexon EV, Tata Tiago EV, MG Windsor EV, Mahindra BE 6, Hyundai Creta EV, BYD Atto 3, MG ZS EV. Tata leads with ~70% EV market share.",
        "electric": "India's top EVs (2024): Tata Nexon EV, Tata Tiago EV, MG Windsor EV, Mahindra BE 6, Hyundai Creta EV, BYD Atto 3, MG ZS EV. Tata leads with ~70% EV market share.",
        "safest": "The safest cars in India by Global NCAP (5-star): Tata Nexon, Tata Punch, Tata Harrier, Tata Safari, VW Taigun, Skoda Kushaq, VW Virtus, Skoda Slavia, Mahindra XUV700, Mahindra Scorpio N, Mahindra Thar Roxx.",
        "cheapest": "The most affordable cars in India: Maruti Alto K10 (~₹3.5L), Maruti S-Presso (~₹4.3L), Renault Kwid (~₹4.7L), Tata Tiago (~₹5.6L).",
        "most fuel efficient": "India's most fuel-efficient cars: Maruti Celerio (26.68 km/l), Maruti Alto K10 (24.9 km/l), Maruti WagonR (24.43 km/l), Toyota Urban Cruiser Hyryder Hybrid (27.97 km/l).",
        "suv": "Popular SUVs in India: Maruti Brezza (sub-4m), Tata Nexon (sub-4m), Hyundai Creta (mid-size), Kia Seltos (mid-size), Mahindra XUV700 (full-size), Toyota Fortuner (premium).",
        "discontinued": "Cars discontinued in India: Ford (all models, 2021), Maruti Santro, Honda Jazz, VW Polo, Renault Duster, Mahindra XUV500, Tata Indica, Tata Nano, Chevrolet (all, 2017).",
        "hybrid": "Hybrid cars in India: Toyota Innova HyCross (strong hybrid), Maruti Grand Vitara (mild/strong hybrid), Toyota Urban Cruiser Hyryder (mild/strong hybrid), Honda City e:HEV (strong hybrid), Hyundai Verna (mild hybrid).",
    }
    for keyword, answer in general.items():
        if keyword in ql:
            return f"\n  💡  {wrap(answer, 6)}\n"

    # ── FALLBACK ──────────────────────────────────────────────────────
    return (
        "\n  🙏 I'm sorry, I don't have specific information about that in my knowledge base.\n\n"
        "  This could be because:\n"
        "   • The car may not be sold in India, or\n"
        "   • It might be too new/rare for my training data, or\n"
        "   • I might not recognise the name — try the full name (e.g. 'Hyundai Creta')\n\n"
        "  💬 Type 'list' to see all cars I know about, or 'help' for usage tips.\n"
    )


# ══════════════════════════════════════════════════════════════════════
#  MAIN CHAT LOOP
# ══════════════════════════════════════════════════════════════════════

def main():
    banner()
    history = []

    while True:
        try:
            user_input = input("  You  ▶  ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  👋 Thank you for using India Cars LLM. Drive safe! 🚗\n")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "bye", "goodbye"):
            print("\n  👋 Thank you for using India Cars LLM! Drive safe and happy motoring! 🚗\n")
            break

        # Maintain chat history (context for multi-turn)
        history.append({"role": "user", "text": user_input})

        response = respond(user_input)
        print(response)

        history.append({"role": "bot", "text": response})

        # Context-aware follow-up: remember last car discussed
        # (Simple context: if next message is vague, use last car key)
        last_car_key = None
        for h in reversed(history[:-2]):
            if h["role"] == "user":
                key, _ = fuzzy_find_car(h["text"])
                if key:
                    last_car_key = key
                    break


if __name__ == "__main__":
    main()
