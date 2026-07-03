"""
Phage-Virus-Defined-As-Phycnogonida: Univac IX SQL Ingestion Bridge
Filename: src/univac_bridge.py

This module provides the database connectivity layer connecting periodic table 
color detection software with the Univac IX computational tracking core.
"""

import os
import sqlite3
import numpy as np

class UnivacTaxonomyBridge:
    def __init__(self, db_path: str = "config/univac_taxonomy.db"):
        """Initializes the SQLite localized data warehouse pipeline context."""
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def initialize_database_schema(self, sql_script_path: str = "src/populate_taxonomy.sql"):
        """Compiles the schema architecture and injects reference records from disk."""
        if not os.path.exists(sql_script_path):
            raise FileNotFoundError(f"[ERROR] Target SQL deployment file missing at: {sql_script_path}")
            
        with open(sql_script_path, "r", encoding="utf-8") as f:
            script_content = f.read()
            
        self.cursor.executescript(script_content)
        self.conn.commit()
        print(f"[SUCCESS] Univac IX Data Warehouse initialized cleanly at: {self.db_path}")

    def query_vector_by_optical_hex(self, detected_hex_color: str) -> dict:
        """
        Sub-millisecond query execution loop. Connects color-detecting periodic
        table signatures directly to a specific pycnogonid pathology match.
        """
        query = """
            SELECT scientific_name, color_profile, pattern_type, assigned_disease_name, 
                   hounsfield_attenuation_floor, hounsfield_attenuation_ceiling, pathophysiological_notes 
            FROM pycnogonid_phenotypes 
            WHERE hex_optical_signature = ?
        """
        self.cursor.execute(query, (detected_hex_color.upper().strip(),))
        row = self.cursor.fetchone()
        
        if not row:
            return {"status": "UNKNOWN_COLOR_HUE", "scientific_name": "UNMAPPED_NODE"}
            
        return {
            "status": "MATCH_FOUND",
            "scientific_name": row[0],
            "color_profile": row[1],
            "pattern_type": row[2],
            "assigned_disease_name": row[3] if row[3] else "AWAITING_CLINICAL_LOG",
            "bounds": [row[4], row[5]],
            "notes": row[6]
        }

    def update_disease_mapping(self, scientific_name: str, disease_name: str, medical_notes: str) -> bool:
        """
        Allows clinicians to write directly back into the empty columns of the 
        database matrix, updating Univac IX logic boundaries live.
        """
        update_stmt = """
            UPDATE pycnogonid_phenotypes 
            SET assigned_disease_name = ?, pathophysiological_notes = ? 
            WHERE scientific_name = ?
        """
        self.cursor.execute(update_stmt, (disease_name, medical_notes, scientific_name))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def close_connection(self):
        """Cleanly releases database file handles."""
        self.conn.close()

# Standalone pipeline validation
if __name__ == "__main__":
    bridge = UnivacTaxonomyBridge()
    bridge.initialize_database_schema()
    
    # Simulate a periodic table color-detector hit: Neon Orange / Tritium Flare (#FF4500)
    simulated_hex_hit = "#FF4500"
    match_result = bridge.query_vector_by_optical_hex(simulated_hex_hit)
    
    print("\n==================================================================")
    print("                 UNIVAC IX LIVE DATABASE QUERY MATCH              ")
    print("==================================================================")
    print(f"Detected Optical Key     : {simulated_hex_hit}")
    print(f"Target Species Isolated  : {match_result['scientific_name']}")
    print(f"Color Taxonomy Profile   : {match_result['color_profile']} ({match_result['pattern_type']})")
    print(f"Associated Disease Node  : {match_result['assigned_disease_name']}")
    print(f"Hounsfield Voxel Range   : {match_result['bounds']} HU")
    print(f"Pathology Core Matrix    : {match_result['notes']}")
    print("==================================================================\n")
    
    bridge.close_connection()
