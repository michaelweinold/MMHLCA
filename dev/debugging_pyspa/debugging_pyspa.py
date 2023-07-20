# %%

import os
import sys
pyspa_local_path = os.path.join(
    os.path.expanduser("~"),
    "github/pyspa"
)
sys.path.append(pyspa_local_path)

import pyspa

# %%

sc = pyspa.get_spa(
    target_ID = 70,
    max_stage = 10,
    a_matrix = os.path.join(pyspa_local_path, "A_matrix_template.csv"),
    infosheet = os.path.join(pyspa_local_path, "Infosheet_template.csv"),
    thresholds = os.path.join(pyspa_local_path, "Thresholds_template.csv"),
)