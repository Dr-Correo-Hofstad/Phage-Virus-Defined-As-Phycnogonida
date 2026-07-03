-- Phage-Virus-Defined-As-Phycnogonida: Master Relational Schema
-- Filename: src/populate_taxonomy.sql

PRAGMA foreign_keys = ON;

-- 1. Create Core Color & Optical Signature Matrix Table
CREATE TABLE IF NOT EXISTS pycnogonid_phenotypes (
    species_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scientific_name TEXT NOT NULL UNIQUE,
    color_profile TEXT NOT NULL,
    pattern_type TEXT NOT NULL,
    hex_optical_signature TEXT NOT NULL,
    hounsfield_attenuation_floor REAL DEFAULT 140.0,
    hounsfield_attenuation_ceiling REAL DEFAULT 690.0,
    assigned_disease_name TEXT DEFAULT NULL,
    pathophysiological_notes TEXT DEFAULT NULL
);

-- Create optimized index keys to ensure sub-millisecond query loops on Univac IX
CREATE INDEX IF NOT EXISTS idx_optical_hex ON pycnogonid_phenotypes(hex_optical_signature);
CREATE INDEX IF NOT EXISTS idx_disease_mapping ON pycnogonid_phenotypes(assigned_disease_name);

-- 2. Inject Complete Taxonomic Color Varieties Data
INSERT OR REPLACE INTO pycnogonid_phenotypes 
(scientific_name, color_profile, pattern_type, hex_optical_signature, assigned_disease_name, pathophysiological_notes)
VALUES 
('Colossendeis megalonyx', 'Bright Red / Crimson', 'Solid / Uniform', '#D9381E', NULL, 'Abyssal variant; tracks deeply along rich cardiopulmonary visceral boundaries.'),
('Achelia langi', 'Deep Charcoal Black', 'Solid / Matte', '#1A1A1A', NULL, 'Associated with systemic lymphatic channel blockage and proteinaceous crowding.'),
('Pycnogonum littorale', 'Dark Chocolate Brown', 'Solid / Rough', '#3D2314', NULL, 'Littoral form; anchors firmly into dense musculoskeletal stroma tracks.'),
('Anoplodactylus petiolatus', 'Tan / Ochre Sand', 'Camouflage', '#C2A678', NULL, 'Interstitial variant; distributes as micro-blastemas within capillary loops.'),
('Nymphon gracile', 'Translucent Soft Pink', 'Translucent', '#FFC0CB', NULL, 'High tissue elasticity; tracks along chorioamniotic fetal interfaces.'),
('Colossendeis australis', 'Bright Lemon Yellow', 'Solid / Glossy', '#FFF200', NULL, 'Hyper-concentrated carotenoid shell; induces severe local cytolytic acidosis.'),
('Ammothea carolinensis', 'Banded Yellow-Black-Red', 'Segmented Bands', '#E2A123', NULL, 'Complex multi-layered shell; triggers aggressive Zone I desmoplastic lacing.'),
('Anoplodactylus lentus', 'Striated Red-Black', 'Striated Lines', '#8B0000', NULL, 'Causes severe compartment micro-hemorrhages via jointed flexion.'),
('Phoxichilidium femoratum', 'Punctate / Finely Spotted', 'Speckled Points', '#7A6B58', NULL, 'Spotted cuticle; correlates with localized dermal thinning and sloughing.'),
('Achelia echinata', 'Marbled / Variegated Grey-Brown', 'Marbled', '#5A5A5A', NULL, 'Blends with bone stroma; drives bone-marrow erosion and calcium leaching.'),
('Colossendeis macerrima', 'Deep Royal Purple / Violet', 'Solid', '#4B0082', NULL, 'Abyssal giant; associated with high-pressure vertebral column blockage.'),
('Pycnogonum stearnsi', 'Ash Grey / Slate', 'Granular Texture', '#708090', NULL, 'High structural density; severely restricts water diffusion (ADC suppression).'),
('Nymphon tenellum', 'Pale Cream / Ivory White', 'Translucent', '#FFFFF0', NULL, 'Microscopic form; evades host macrophage filters inside lymph channels.'),
('Ammothea hilgendorfi', 'Banded Orange and Dark Brown', 'Horizontal Bands', '#D2691E', NULL, 'Associated with mucosal tracking and posterior pharyngeal drainage blocks.'),
('Endeis spinosa', 'Translucent Olive Green', 'Translucent', '#556B2F', NULL, 'Thin cuticle shell; leaks low-pH salivary proteases into abdominal tissue fields.'),
('Callipallene brevirostris', 'Mottled Rust Red / Amber', 'Mottled Patches', '#B22222', NULL, 'Aggressive appendicular movement; causes relapsing mucosal epistaxis.'),
('Colossendeis robusta', 'Neon Orange / Fluorescent Flare', 'Fluorescent', '#FF4500', NULL, 'Generates cellular tritium; drives high radiotoxic ARS fevers.'),
('Achelia vulgaris', 'Speckled White-on-Grey', 'Speckled Patches', '#DCDCDC', NULL, 'Marrow tracking variant; triggers acute leukopenia and pancytopenia.'),
('Anoplodactylus insignis', 'Banded Black and Yellow', 'Vertical Bands', '#FFD700', NULL, 'Causes mechanical endothelial erosion downstream from central carotid paths.'),
('Nymphon leptocheles', 'Translucent Pinkish-Purple', 'Translucent / Iridescent', '#DA70D6', NULL, 'Tracks deeply along central nervous white matter paths, driving demyelinating plaques.');
