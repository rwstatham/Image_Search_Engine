# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:51:21 2024

@author: Robert Statham
"""

import os
import weaviate as wv

def init_client():
    WEAVIATE_URL = os.getenv('WEAVIATE_URL')
    if not WEAVIATE_URL:
        WEAVIATE_URL = 'http://localhost:8080'

    client = wv.Client(WEAVIATE_URL)
    if client.is_ready():
        print("Client connected successfully.")
    else:
        print("Error: Connection unsuccessful.")